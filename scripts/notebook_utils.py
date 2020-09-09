import scipy
import matplotlib.pyplot as plt
import numpy as np


def plot_fft(audio_sample, sampling_rate, headline='headline'):
    n = len(audio_sample)
    T = 1 / sampling_rate

    yf = scipy.fft.fft(audio_sample)
    xf = np.linspace(0.0, 1.0 / (2.0*T), n//2)

    _, ax = plt.subplots()
    ax.plot(xf, 2.0/n * np.abs(yf[:n//2]))
    plt.grid()
    plt.title(headline)
    plt.xlabel("frequency")
    plt.ylabel("magnitude")
    return plt.show()
