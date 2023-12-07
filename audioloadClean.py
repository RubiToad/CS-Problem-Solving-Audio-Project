# Imports for cleaning meta-data
# From L26
##
from os import path
from pydub import AudioSegment  # Allegedly unused, yet the code breaks without it
from pydub.playback import play
from audioload import *


def pydub_logger():
    # Pydub comes with its own logger.
    import logging

    l = logging.getLogger("pydub.converter")
    l.setLevel(logging.DEBUG)
    l.addHandler(logging.StreamHandler())


def debugg(fstring):
    print(fstring)  # comment out December 10
    # pass


def convert_1chan(filepath):
    debugg("convert_1chan")
    # TODO: if is_wav(filepath):  # comment out for prod
    if is_1chan(filepath) != 1:
        debugg("is_1chan false")
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
        mono_wav.export(dst, format="wav")

        # Debug. Remove in prod.
        mono_wav_audio = AudioSegment.from_file(dst, format="wav")
        channel_count = mono_wav_audio.channels
        debugg(f"Channel count after convert_1chan: {channel_count}")

        return dst
    else:
        debugg("is_1chan true")
        return filepath


def is_1chan(filepath):
    # TODO: if is_wav(filepath): # comment out for prod
    raw_audio = AudioSegment.from_file(
        filepath,
        format="wav"
    )
    # Reduce channels to one
    return 1 == raw_audio.channels  # ?1:0
    pass
