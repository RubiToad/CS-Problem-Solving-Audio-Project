import os
import shutil
import soundfile as sf
    # Accidentally typed "sfc"

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
        play_file(filepath)


def is_wav(filepath):
    _, file_extension = os.path.splitext(filepath)
        # Doesn't it waste space to make an unused underscore variable?
    return file_extension.lower() == '.wav'



def wav_convert(filepath):
    wav_filepath = filepath.replace(os.path.splitext(filepath)[1], '.wav')
    shutil.copyfile(filepath, wav_filepath) # from=filepath, to=wav_filepath
    return wav_filepath