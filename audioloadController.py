import pygame
import soundfile as sf


pygame.init()

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