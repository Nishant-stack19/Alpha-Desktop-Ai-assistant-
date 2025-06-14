import pvporcupine
import pyaudio
import struct
import os

# Path to your assistant script
ASSISTANT_COMMAND = r'start "" cmd /k "cd /d C:\Users\Admin\Desktop\Ai Assistance && venv\Scripts\activate && python assistant\main.py"'

def listen_for_wake_word():
# This makes the path dynamic
    KEYWORD_PATH = os.path.join(os.path.dirname(__file__), "wake_up_alpha.ppn")

# for getting the access key go to https://picovoice.ai/platform/porcupine/ and create an account
    # Replace with your own access key
    porcupine = pvporcupine.create(
        access_key="Enter your own access key",
        keyword_paths=[KEYWORD_PATH]
    )
# ACCESS_KEY = "UZ4P6h5Nf0wW2Pc+60VVb7gqSCW7MAYUhocNe0dHLP8yGEj17adDFg=="
# porcupine = pvporcupine.create(access_key=ACCESS_KEY, keywords=["alexa"])

    pa = pyaudio.PyAudio()
    stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    print("Listening for wake word...")

    try:
        while True:
            pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            keyword_index = porcupine.process(pcm)
            if keyword_index >= 0:
                print("Wake word detected!")
                os.system(ASSISTANT_COMMAND)
                break

    finally:
        stream.stop_stream()
        stream.close()
        pa.terminate()
        porcupine.delete()

if __name__ == "__main__":
    listen_for_wake_word()
