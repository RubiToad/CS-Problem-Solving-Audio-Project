# A model for computing frequencies
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

from main import debugg


def compute_frequencies(filepath):  # main
    sample_rate, data = wavfile.read(filepath)
    spectrum, freqs, t, im = plt.specgram(data, Fs=sample_rate,
                                          NFFT=1024, cmap=plt.get_cmap('autumn_r'))  # L25 Slide 14

    data_in_db = frequency_check(spectrum, freqs)
    debugg(f'data_in_db {data_in_db[:10]}')
    plt.figure()
    # plot reverb time on grid
    plt.plot(t, data_in_db, linewidth=1, alpha=0.7, color='#004bc6')
    plt.xlabel('Time (s)')
    plt.ylabel('Power (dB)')

    # find an index of a max value
    index_of_max = np.argmax(data_in_db)
    # Find maximum value of dB's (decibel is logarithmic) in array
    value_of_max = data_in_db[index_of_max]
    plt.plot(t[index_of_max], data_in_db[index_of_max], 'go')

    # slice array from a max value
    # Slice data and time arrays to location of maximum value
    sliced_array = data_in_db[index_of_max:]
    debugg(f'sliced_array {sliced_array[:10]}')
    # Find value which is Max -5dB (avoids measuring actual impulse)
    value_of_max_less_5 = value_of_max - 5
    value_of_max_less_5 = find_nearest_value(sliced_array, value_of_max_less_5)

    index_of_max_less_5 = np.where(data_in_db == value_of_max_less_5)
    plt.plot(t[index_of_max_less_5], data_in_db[index_of_max_less_5], 'yo')

    # slice array from a max -5dB
    value_of_max_less_25 = value_of_max - 25
    value_of_max_less_25 = find_nearest_value(sliced_array, value_of_max_less_25)
    index_of_max_less_25 = np.where(data_in_db == value_of_max_less_25)

    plt.plot(t[index_of_max_less_25], data_in_db[index_of_max_less_25], 'ro')
    # Calculate RT20 as time it takes amplitude to drop from max (less 5dB) to max (less 25dB)
    rt20 = (t[index_of_max_less_5] - t[index_of_max_less_25])[0]
    debugg(f'rt20= {rt20}')
    # extrapolate rt20 to rt60
    rt60 = 3 * rt20

    # Benjamin decided not to set optional limits on the plot. The line below is what I would have done.
    # plt.xlim(0, ((round(abs(rt60), 2)) * 1.5))
    plt.grid()  # show grid
    plt.show()  # show plots

    print(f'The RT60 reverb time at freq {int(find_target_frequency(freqs))} is {round(abs(rt60), 2)} seconds')


def find_target_frequency(freqs):
    for x in freqs:
        if x > 1000:
            break
        return x


# In class, Mr. Navarro said you could use 250 for low, 1000 for mid, and 5000 for high.
def find_low_frequency(freqs):
    for x in freqs:
        if x > 250:
            break
        return x


def find_high_frequency(freqs):
    for x in freqs:
        if x > 5000:
            break
        return x


# you can choose a frequency that you want to check
def frequency_check(spectrum, freqs):  # Data returned will vary based in freqs. Is necessary for graphs.
    # identify a frequency to check
    debugg(f'freqs= {freqs}')
    debugg(f'freqs {freqs[:10]}')
    target_frequency = find_target_frequency(freqs)
    debugg(f'target_frequency {target_frequency}')
    index_of_frequency = np.where(freqs == target_frequency)[0][0]
    debugg(f'index_of_frequency {index_of_frequency}')
    # find a sound data for a particular frequency

    data_for_frequency = spectrum[index_of_frequency]
    debugg(f'data_for_frequency {data_for_frequency[:10]}')

    # change a digital signal for a value in decibels

    data_in_db_fun = 10 * np.log10(data_for_frequency)
    return data_in_db_fun


# Pass in sliced array list and value (dB)
def find_nearest_value(array, value):
    debugg(f'array {array[:10]}')
    array = np.asarray(array)
    debugg(f'array {array[:10]}')

    # Convert input into array. Return indices of min values along an axis
    idx = (np.abs(array - value)).argmin()
    debugg(f'idx {idx}')
    debugg(f'array[idx] {array[idx]}')
    return array[idx]
