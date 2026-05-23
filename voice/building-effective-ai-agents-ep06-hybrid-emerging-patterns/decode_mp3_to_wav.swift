import AVFoundation
import Foundation

guard CommandLine.arguments.count == 3 else {
    fputs("usage: decode_mp3_to_wav.swift input.mp3 output.wav\n", stderr)
    exit(2)
}

let inputURL = URL(fileURLWithPath: CommandLine.arguments[1])
let outputURL = URL(fileURLWithPath: CommandLine.arguments[2])

let inputFile = try AVAudioFile(forReading: inputURL)
let outputFormat = AVAudioFormat(
    commonFormat: .pcmFormatInt16,
    sampleRate: inputFile.fileFormat.sampleRate,
    channels: inputFile.fileFormat.channelCount,
    interleaved: true
)!
let outputFile = try AVAudioFile(forWriting: outputURL, settings: outputFormat.settings)

let frameCapacity = AVAudioFrameCount(min(inputFile.length, 4096))
let buffer = AVAudioPCMBuffer(pcmFormat: inputFile.processingFormat, frameCapacity: frameCapacity)!

while inputFile.framePosition < inputFile.length {
    try inputFile.read(into: buffer)
    if buffer.frameLength == 0 {
        break
    }
    try outputFile.write(from: buffer)
}
