# import matplotlib.pyplot as plt # Frequencies
# from L26
# from scipy.io import wavfile # Frequencies
# import numpy as np # Frequencies
from audioload import *
from audioloadClean import debugg

def find_target_frequency(freqs):
    for x in freqs:
        if x > 1000:
            break
        return x

# you can choose a frequency that you want to check
def frequency_check(filepath):
    sample_rate, data = wavfile.read(filepath)
    spectrum, freqs, t, im = plt.specgram(data, Fs=sample_rate,
                                          NFFT=1024, cmap=plt.get_cmap('autumn_r'))
    debugg(f'freqs {freqs[:10]}')
    target_frequency = find_target_frequency(freqs)
    debugg(f'target_frequency {target_frequency}')
    index_of_frequency = np.where(freqs == target_frequency) [0] [0]
    debugg(f'index_of_frequency {index_of_frequency}')
    # find a sound data for a particular frequency

    data_for_frequency = spectrum[index_of_frequency]
    debugg(f'data_for_frequency {data_for_frequency[:10]}')

    # change a digital signal for a value in decibels

    data_in_db_fun = 10 * np.log10(data_for_frequency)
    return data_in_db_fun

def find_nearest_value(array, value):
    array = np.asarray(array)
    debugg(f'array {array[:10]}')
    idx = (np.abs(array - value)).argmin()
    debugg(f'idx {idx}')
    debugg(f'array[idx] {array[idx]}')
    return array[idx]

def compute_frequencies(filepath):
    data_in_db = frequency_check(filepath)
