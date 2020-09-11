from scipy.signal import butter, lfilter


def butterworth(sample, sr, btype, co, order=5):
    """
    Applies a Butterworth lowpass filter to a provided audio sample.
    
    In general, low-pass filters passes signals with a frequency lower 
    than a specified cutoff frequency and attenuates signals with 
    frequencies higher than the cutoff frequency.

    Parameters
    ----------

    sample : int > 0 [scalar]
        audio sample

    sr : int > 0 [scalar]
        sampling rate of the provided sample

    btype : str
        band

    co : int > 0 [scalar]
        cutoff frequency for the filter

    order : int > 0 [scalar], optional
        filter order


    Returns
    ----------

    filtered_sample : array
        filtered audio sample
    """

    # calculates Nyquist frequency
    nyq = 0.5 * sr

    # critical frequency or frequencies as a scalar
    low = co / nyq

    # numerator and denominator of the filter coefficients
    b, a = butter(order, low, btype=btype, analog=False)

    return lfilter(b, a, sample)