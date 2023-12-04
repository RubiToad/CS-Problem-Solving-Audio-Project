import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pygame # Audio can also be played with the pydub library
import os
import shutil
import soundfile as sf
    # Accidentally typed "sfc"
from audioloadClean import *
# from audioloadController import *
# from audioloadModel import *
# from audioloadView import *

root = tk.Tk()
root.title("Media Player")
root.geometry("300x200")

pygame.init()

# pydubLogger()

def browse_file():
    filepath = filedialog.askopenfilename(
        filetypes=[("mp3 files", ".mp3"), ("Video Files", ".mp4"), (".wav files", ".wav"), (".ogg files", ".ogg")])
    if filepath:
        if not is_wav(filepath):
            print("File is not WAV. Converting to WAV...")
            filepath = wav_convert(filepath)
            if is_wav(filepath):
                print("File is now WAV")
                filepath = convert_1chan(filepath)
        else:
            print("File is WAV")
            filepath = convert_1chan(filepath)
        play_file(filepath)


def is_wav(filepath):
    file_extension = os.path.splitext(filepath)[1]
        # Doesn't it waste space to make an unused underscore variable?
    return file_extension.lower() == '.wav'

def wav_convert(filepath):
    wav_filepath = filepath.replace(os.path.splitext(filepath)[1], '.wav')
    shutil.copyfile(filepath, wav_filepath) # from=filepath, to=wav_filepath
    return wav_filepath


def play_file(filepath):
    audio_data, sample_rate = sf.read(filepath, dtype='int16')
    pygame.mixer.Sound(audio_data).play()


def pause_file():
    pygame.mixer.pause()


def resume_file():
    pygame.mixer.unpause()


def stop_file():
    pygame.mixer.stop()


def about_us():
    messagebox.showinfo("About Media Player",
                        "A simple media player program created in Python using Tkinter and Pygame.")


browse_button = tk.Button(root, text="Load Audio File", command=browse_file)
browse_button.pack()

pause_button = tk.Button(root, text="Pause", command=pause_file)
pause_button.pack()

resume_button = tk.Button(root, text="Resume", command=resume_file)
resume_button.pack()

stop_button = tk.Button(root, text="Stop", command=stop_file)
stop_button.pack()

about_us_button = tk.Button(root, text="About Media Player", command=about_us)
about_us_button.pack()

# root.mainloop()
