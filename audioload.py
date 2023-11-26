import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pygame

root = tk.Tk()
root.title("Media Player")
root.geometry("300x200")

pygame.init()

def browse_file():
    filepath = filedialog.askopenfilename(filetypes=[("mp3 files", "*.mp3"), ("Video Files", "*.mp4"), (".wav files", "*.wav"), (".ogg files", "*.ogg")])
    play_file(filepath)

def play_file(filepath):
    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play()

def pause_file():
    pygame.mixer.music.pause()

def resume_file():
    pygame.mixer.music.unpause()

def stop_file():
    pygame.mixer.music.stop()

def about_us():
    messagebox.showinfo("About Media Player", "A simple media player program created in Python using Tkinter and Pygame.")

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

root.mainloop()