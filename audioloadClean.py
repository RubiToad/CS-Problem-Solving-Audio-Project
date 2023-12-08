# Clean metadata, and
from os import path
from pydub import utils, AudioSegment
from pydub.playback import play
import os
# from audioload import is_wav # This is a circular import
from Convert import is_wav


def debugg(fstring):
    print(fstring)  # TODO: comment out December 10, the due date of the project.
    # pass


def convert_1chan(filepath):
    debugg(f"convert_1chan filepath: {filepath}\n")

#    AudioSegment.converter = "~/ffmpeg/ffmpeg-2023-12-07-git-f89cff96d0-full_build/bin/ffmpeg.exe"
#    utils.get_prober_name = get_prober_name

    if is_1chan(filepath) != 1:
        debugg("is_1chan false")
        raw_audio = AudioSegment.from_file(  # TODO: Don't copy-paste this raw_audio call from is_1chan.
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
    if is_wav(filepath):
        debugg(f"is_1chan: {filepath}")
        raw_audio = AudioSegment.from_file( # TODO: This line throws FileNotFoundError for mp3 files.
            filepath,
            format="wav"
        )
        # Reduce channels to one
        return 1 == raw_audio.channels  # ?1:0
        pass
