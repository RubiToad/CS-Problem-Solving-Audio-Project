import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pygame  # Audio can also be played with the pydub library
import os
import shutil
import soundfile as sf
import matplotlib.pyplot as plt  # For frequencies
import scipy.io
from scipy.io import wavfile  # For frequencies
import numpy as np  # For frequencies
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from audioloadClean import convert_1chan
from frequencies import compute_frequencies # Only need the one function

root = tk.Tk()  # For tkinter
root.title("Media Player")
root.geometry("300x350")

pygame.init()  # For media player

filepath = 0  # For browse_file

canvas_frame = tk.Frame(root)
canvas_frame.pack(pady=10)
fig, ax = plt.subplots(figsize=(4.8, 1.5), tight_layout=True)  # for display_time_waveform
canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
canvas.get_tk_widget().pack()

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
        else:
            print("File is WAV")
        filepath = convert_1chan(filepath)  # convert_1chan includes is_1chan check
        display_time_waveform(filepath)
        compute_frequencies(filepath)

        play_file(filepath)


def display_time_waveform(filepath):
    # Uses soundfile, numpy, and matplotlib
    # Plots waveform by time
    audio_data, sample_rate = sf.read(filepath, dtype='int16')
    audio_data = audio_data / np.max(np.abs(audio_data), axis=0)

    duration = len(audio_data) / sample_rate
    time_values = np.linspace(0., duration, len(audio_data))

    ax.clear()
    ax.plot(time_values, audio_data, color="blue", linewidth=2)
    ax.axhline(y=0, color='gray', linestyle='--', linewidth=1)
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Amplitude')

    canvas.draw()

    duration_text = f"Duration: {duration:.2f} seconds" + "\n" + filepath
    canvas.get_tk_widget().delete("duration_label")
    duration_label = tk.Label(root, text=duration_text, font=('Helvetica', 10), fg="black", bd=5)
    duration_label.pack(pady=10)
    duration_label.bind("<Configure>", lambda e: canvas.draw())


def is_wav(filepath):
    file_extension = os.path.splitext(filepath)[1]
    return file_extension.lower() == '.wav'


def wav_convert(filepath):
    wav_filepath = filepath.replace(os.path.splitext(filepath)[1], '.wav')
    shutil.copyfile(filepath, wav_filepath)  # from=filepath, to=wav_filepath
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
