import scipy
import librosa
import numpy as np
import matplotlib.pyplot as plt

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


def plot_mel_filters(sr, n_fft=2048, n_mels=128, hop_length=512):

    mel = librosa.filters.mel(sr=sr, n_fft=n_fft, n_mels=n_mels)
    
    plt.figure(figsize=(15, 4))
    plt.subplot(1, 3, 1)
    librosa.display.specshow(mel, sr=sr, hop_length=hop_length, x_axis='linear')
    plt.ylabel('Mel Filter')
    plt.colorbar()
    plt.title('Filter Bank (Hz => mels)')

    plt.subplot(1, 3, 2)
    mel_10 = librosa.filters.mel(sr=sr, n_fft=n_fft, n_mels=10)
    librosa.display.specshow(mel_10, sr=sr, hop_length=hop_length, x_axis='linear')
    plt.ylabel('Mel Filter')
    plt.colorbar()
    plt.title('Filter Bank w/ 10 mels')

    plt.subplot(1, 3, 3)
    idxs_to_plot = [0, 9, 49, 99, 127]
    for i in idxs_to_plot:
        plt.plot(mel[i])
    plt.legend(labels=[f'{i+1}' for i in idxs_to_plot])
    plt.title('Triangular Filters')

    return plt.tight_layout()


def plot_mel(sample, sr, n_fft=2048, hop_length=512, n_mels=128):
    S = librosa.feature.melspectrogram(sample, sr=sr, n_fft=n_fft, hop_length=hop_length, n_mels=n_mels)
    S_DB = librosa.power_to_db(S, ref=np.max)
    librosa.display.specshow(S_DB, sr=sr, hop_length=hop_length, x_axis='time', y_axis='mel')
    
    return plt.colorbar(format='%+2.0f dB')