import AppKit
import AVFoundation
import Foundation

let root = URL(fileURLWithPath: FileManager.default.currentDirectoryPath)
    .appendingPathComponent("douyin/building-effective-ai-agents")
let frameManifestURL = root.appendingPathComponent("frame_manifest.json")
let audioManifestURL = root.appendingPathComponent("audio_manifest.json")
let silentURL = root.appendingPathComponent("video.silent.mov")
let outputURL = root.appendingPathComponent("video.mp4")

struct FrameItem {
    let file: String
    let duration: Double
}

struct AudioItem {
    let file: String
    let duration: Double
}

func loadJSON(_ url: URL) throws -> Any {
    let data = try Data(contentsOf: url)
    return try JSONSerialization.jsonObject(with: data)
}

func loadFrames() throws -> [FrameItem] {
    let json = try loadJSON(frameManifestURL) as! [String: Any]
    let frames = json["frames"] as! [[String: Any]]
    return frames.map {
        FrameItem(file: $0["file"] as! String, duration: $0["duration"] as! Double)
    }
}

func loadAudio() throws -> [AudioItem] {
    let json = try loadJSON(audioManifestURL) as! [String: Any]
    let chunks = json["chunks"] as! [[String: Any]]
    return chunks.map {
        AudioItem(file: $0["file"] as! String, duration: $0["duration"] as! Double)
    }
}

func makePixelBuffer(from imageURL: URL, width: Int, height: Int) throws -> CVPixelBuffer {
    guard let image = NSImage(contentsOf: imageURL) else {
        throw NSError(domain: "render", code: 1, userInfo: [NSLocalizedDescriptionKey: "Cannot load image \(imageURL.path)"])
    }
    var buffer: CVPixelBuffer?
    let attrs: [String: Any] = [
        kCVPixelBufferCGImageCompatibilityKey as String: true,
        kCVPixelBufferCGBitmapContextCompatibilityKey as String: true,
        kCVPixelBufferPixelFormatTypeKey as String: kCVPixelFormatType_32ARGB
    ]
    CVPixelBufferCreate(kCFAllocatorDefault, width, height, kCVPixelFormatType_32ARGB, attrs as CFDictionary, &buffer)
    guard let pixelBuffer = buffer else {
        throw NSError(domain: "render", code: 2, userInfo: [NSLocalizedDescriptionKey: "Cannot create pixel buffer"])
    }

    CVPixelBufferLockBaseAddress(pixelBuffer, [])
    defer { CVPixelBufferUnlockBaseAddress(pixelBuffer, []) }
    guard let context = CGContext(
        data: CVPixelBufferGetBaseAddress(pixelBuffer),
        width: width,
        height: height,
        bitsPerComponent: 8,
        bytesPerRow: CVPixelBufferGetBytesPerRow(pixelBuffer),
        space: CGColorSpaceCreateDeviceRGB(),
        bitmapInfo: CGImageAlphaInfo.noneSkipFirst.rawValue
    ) else {
        throw NSError(domain: "render", code: 3, userInfo: [NSLocalizedDescriptionKey: "Cannot create context"])
    }

    NSGraphicsContext.saveGraphicsState()
    NSGraphicsContext.current = NSGraphicsContext(cgContext: context, flipped: false)
    image.draw(in: NSRect(x: 0, y: 0, width: width, height: height))
    NSGraphicsContext.restoreGraphicsState()
    return pixelBuffer
}

func renderSilentVideo(frames: [FrameItem], durations: [Double], url: URL, fileType: AVFileType) throws {
    try? FileManager.default.removeItem(at: url)
    let writer = try AVAssetWriter(outputURL: url, fileType: fileType)
    let settings: [String: Any] = [
        AVVideoCodecKey: AVVideoCodecType.h264,
        AVVideoWidthKey: 1920,
        AVVideoHeightKey: 1080,
        AVVideoCompressionPropertiesKey: [
            AVVideoAverageBitRateKey: 10_000_000,
            AVVideoProfileLevelKey: AVVideoProfileLevelH264High41
        ]
    ]
    let input = AVAssetWriterInput(mediaType: .video, outputSettings: settings)
    input.expectsMediaDataInRealTime = false
    let adaptor = AVAssetWriterInputPixelBufferAdaptor(
        assetWriterInput: input,
        sourcePixelBufferAttributes: [
            kCVPixelBufferPixelFormatTypeKey as String: kCVPixelFormatType_32ARGB,
            kCVPixelBufferWidthKey as String: 1920,
            kCVPixelBufferHeightKey as String: 1080
        ]
    )
    writer.add(input)
    writer.startWriting()
    writer.startSession(atSourceTime: .zero)

    let fps: Int32 = 30
    var frameIndex: Int64 = 0
    for (idx, frame) in frames.enumerated() {
        let imageURL = root.appendingPathComponent(frame.file)
        let buffer = try makePixelBuffer(from: imageURL, width: 1920, height: 1080)
        let count = max(1, Int((durations[idx] * Double(fps)).rounded()))
        for _ in 0..<count {
            while !input.isReadyForMoreMediaData {
                Thread.sleep(forTimeInterval: 0.002)
            }
            let time = CMTime(value: frameIndex, timescale: fps)
            adaptor.append(buffer, withPresentationTime: time)
            frameIndex += 1
        }
    }

    input.markAsFinished()
    let group = DispatchGroup()
    group.enter()
    writer.finishWriting {
        group.leave()
    }
    group.wait()
    if writer.status != .completed {
        throw writer.error ?? NSError(domain: "render", code: 4, userInfo: [NSLocalizedDescriptionKey: "Silent writer failed"])
    }
}

func muxAudio(frames: [FrameItem], audio: [AudioItem]) throws {
    try? FileManager.default.removeItem(at: outputURL)
    let composition = AVMutableComposition()
    let videoAsset = AVAsset(url: silentURL)
    guard let videoTrack = try awaitTrack(videoAsset, mediaType: .video) else {
        throw NSError(domain: "render", code: 5, userInfo: [NSLocalizedDescriptionKey: "No video track"])
    }
    let videoCompTrack = composition.addMutableTrack(withMediaType: .video, preferredTrackID: kCMPersistentTrackID_Invalid)!
    try videoCompTrack.insertTimeRange(CMTimeRange(start: .zero, duration: videoAsset.duration), of: videoTrack, at: .zero)

    let audioCompTrack = composition.addMutableTrack(withMediaType: .audio, preferredTrackID: kCMPersistentTrackID_Invalid)!
    var cursor = CMTime.zero
    for item in audio {
        let asset = AVAsset(url: root.appendingPathComponent(item.file))
        guard let track = try awaitTrack(asset, mediaType: .audio) else { continue }
        try audioCompTrack.insertTimeRange(CMTimeRange(start: .zero, duration: asset.duration), of: track, at: cursor)
        cursor = CMTimeAdd(cursor, asset.duration)
    }

    guard let exporter = AVAssetExportSession(asset: composition, presetName: AVAssetExportPresetHighestQuality) else {
        throw NSError(domain: "render", code: 6, userInfo: [NSLocalizedDescriptionKey: "Cannot create exporter"])
    }
    exporter.outputURL = outputURL
    exporter.outputFileType = .mp4
    exporter.shouldOptimizeForNetworkUse = true

    let group = DispatchGroup()
    group.enter()
    exporter.exportAsynchronously {
        group.leave()
    }
    group.wait()
    if exporter.status != .completed {
        throw exporter.error ?? NSError(domain: "render", code: 7, userInfo: [NSLocalizedDescriptionKey: "Export failed"])
    }
}

func awaitTrack(_ asset: AVAsset, mediaType: AVMediaType) throws -> AVAssetTrack? {
    if #available(macOS 13.0, *) {
        let semaphore = DispatchSemaphore(value: 0)
        var tracks: [AVAssetTrack] = []
        var loadError: Error?
        Task {
            do {
                tracks = try await asset.loadTracks(withMediaType: mediaType)
            } catch {
                loadError = error
            }
            semaphore.signal()
        }
        semaphore.wait()
        if let loadError { throw loadError }
        return tracks.first
    } else {
        return asset.tracks(withMediaType: mediaType).first
    }
}

do {
    let frames = try loadFrames()
    let audio = FileManager.default.fileExists(atPath: audioManifestURL.path) ? try loadAudio() : []
    let durations = audio.count == frames.count ? audio.map { $0.duration } : frames.map { $0.duration }
    let audioTotal = audio.map { $0.duration }.reduce(0, +)
    if audio.count == frames.count && audioTotal > 1.0 {
        try renderSilentVideo(frames: frames, durations: durations, url: silentURL, fileType: .mov)
        try muxAudio(frames: frames, audio: audio)
    } else {
        try renderSilentVideo(frames: frames, durations: frames.map { $0.duration }, url: outputURL, fileType: .mp4)
    }
    print(outputURL.path)
} catch {
    fputs("render_video.swift failed: \(error)\n", stderr)
    exit(1)
}
