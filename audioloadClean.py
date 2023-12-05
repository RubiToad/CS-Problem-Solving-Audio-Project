# Imports for cleaning meta-data
##
from os import path
from pydub import AudioSegment
from pydub.playback import play
from audioload import *


def pydub_logger():
    # Pydub comes with its own logger.
    import logging

    l = logging.getLogger("pydub.converter")
    l.setLevel(logging.DEBUG)
    l.addHandler(logging.StreamHandler())

def debugg(fstring):
    print(fstring) # comment out December 10
    # pass

def convert_1chan(filepath):
    debugg("convert_1chan")
    if is_wav(filepath):  # comment out for prod
        debugg("is_wav")
        raw_audio = AudioSegment.from_file(
            filepath,
            format="wav"  # only execute AFTER converting to .wav
        )
        # Reduce channels to one
        channel_count = raw_audio.channels
        debugg(f"Channel count before convert_1chan: {channel_count}")
        mono_wav = raw_audio.set_channels(1)

        # Export
        dst = str(os.path.splitext(filepath)[0] + "_mono.wav")
        mono_wav.export(dst,format="wav")

        # Debug. Remove in prod.
        mono_wav_audio = AudioSegment.from_file(dst, format = "wav")
        channel_count = mono_wav_audio.channels
        debugg(f"Channel count after convert_1chan: {channel_count}")

        return dst
    else:
        pass
