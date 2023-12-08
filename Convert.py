# Prevent circular import between audioload.py and audioloadClean.py
import os
import shutil


def is_wav(filepath):
    file_extension = os.path.splitext(filepath)[1]
    return file_extension.lower() == '.wav'


def wav_convert(filepath):
    wav_filepath = filepath.replace(os.path.splitext(filepath)[1], '.wav')
    shutil.copyfile(filepath, wav_filepath)  # from=filepath, to=wav_filepath
    return wav_filepath
