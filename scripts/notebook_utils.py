import scipy
import matplotlib.pyplot as plt
import numpy as np

""" Plots fast fourier transformation of provided audio file
array_like: audio_sample: Audio File
float: sampling_rate: Sampling rate in Hz
[opt] headline: Headline of plots
"""
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


def plot_spectrogram(samples, sample_rate, stride_ms=10.0, window_ms=20.0, max_freq=None, eps=1e-14):
    stride_size = int(0.001 * sample_rate * stride_ms)
    window_size = int(0.001 * sample_rate * window_ms)

    # Extract strided windows
    truncate_size = (len(samples) - window_size) % stride_size
    samples = samples[:len(samples) - truncate_size]
    nshape = (window_size, (len(samples) - window_size) // stride_size + 1)
    nstrides = (samples.strides[0], samples.strides[0] * stride_size)
    windows = np.lib.stride_tricks.as_strided(samples, shape = nshape, strides = nstrides)
    
    assert np.all(windows[:, 1] == samples[stride_size:(stride_size + window_size)])

    # Window weighting, squared Fast Fourier Transform (fft), scaling
    weighting = np.hanning(window_size)[:, None]
    
    fft = np.fft.rfft(windows * weighting, axis=0)
    fft = np.absolute(fft)
    fft = fft**2
    
    scale = np.sum(weighting**2) * sample_rate
    fft[1:-1, :] *= (2.0 / scale)
    fft[(0, -1), :] /= scale
    
    # Prepare fft frequency list
    freqs = float(sample_rate) / window_size * np.arange(fft.shape[0])
    if max_freq is None: max_freq = max(samples)
    
    # Compute spectrogram feature
    ind = np.where(freqs <= max_freq)[0][-1] + 1
    specgram = np.log(fft[:ind, :] + eps)

    return windows, specgram
