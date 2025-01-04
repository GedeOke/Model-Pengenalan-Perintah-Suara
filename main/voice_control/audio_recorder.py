import pyaudio
import numpy as np

class AudioRecorder:
    def __init__(self, buffer_size=3200, format=pyaudio.paInt16, channels=1, rate=16000):
        self.buffer_size = buffer_size
        self.format = format
        self.channels = channels
        self.rate = rate
        self.audio_interface = pyaudio.PyAudio()
        self.stream = None

    def start_recording(self):
        self.stream = self.audio_interface.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.buffer_size
        )

    def stop_recording(self):
        self.stream.stop_stream()
        self.stream.close()

    def record_audio(self, duration=1):
        self.start_recording()
        audio_frames = []

        total_frames = int(self.rate / self.buffer_size * duration)
        for _ in range(total_frames):
            frame_data = self.stream.read(self.buffer_size)
            audio_frames.append(frame_data)

        self.stop_recording()

        audio_data = np.frombuffer(b''.join(audio_frames), dtype=np.int16)
        return audio_data

    def terminate(self):
        self.audio_interface.terminate()

if __name__ == "__main__":
    recorder = AudioRecorder()
    audio_data = recorder.record_audio(duration=1)
    print("Captured Audio Data:", audio_data)
    recorder.terminate()
