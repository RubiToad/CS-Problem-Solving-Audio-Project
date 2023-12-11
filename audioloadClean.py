# A model for cleaning meta-data
from pydub import AudioSegment
import os
# from audioload import is_wav # This could be a circular import
from ConvertSciPy import is_wav, compute_wav
from main import debugg  # Refactored into main.py module for easier user input


# convert_1chan includes is_1chan check
def convert_1chan(filepath):
    debugg(f"convert_1chan filepath: {filepath}\n")
    if is_wav(filepath):  # comment out for prod
        raw_audio = convert_raw_audio(filepath=filepath)
        if raw_audio.channels != 1:
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
    else:
        debugg('Convert to wav BEFORE calling convert_1chan! Here, I\'ll convert it for you.')
        filepath = compute_wav(filepath)
        return convert_1chan(filepath)


def convert_raw_audio(filepath):  # Once called is_1chan(filepath)
    if is_wav(filepath):
        debugg(f"convert_raw_audio: {filepath}")
        raw_audio = AudioSegment.from_file(  # TODO: This line throws CouldntDecodeError for non-test files.
            filepath,
            format="wav"
        )
        # Reduce channels to one
        return raw_audio
