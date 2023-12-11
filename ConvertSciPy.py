# Prevent potential circular import between audioload.py and audioloadClean.py
import os
import shutil  # TODO: Replace with Pydub.
from main import debugg


def compute_wav(filepath):
    debugg(f"File name before wav conversion: {os.path.basename(filepath)}")
    if not is_wav(filepath):
        print("File is not WAV. Converting to WAV...")
        wav_filepath = wav_convert(filepath)
        if is_wav(filepath):
            print("File is now WAV")

    else:
        print("File is WAV")
        wav_filepath = filepath
    debugg(f"File name after wav conversion: {os.path.basename(wav_filepath)}")
    return wav_filepath


def is_wav(filepath):
    file_extension = os.path.splitext(filepath)[1]
    return file_extension.lower() == '.wav'


def wav_convert(filepath):
    wav_filepath = filepath.replace(os.path.splitext(filepath)[1], '.wav')
    shutil.copyfile(filepath, wav_filepath)
    return wav_filepath
