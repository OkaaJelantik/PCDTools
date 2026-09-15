"""
Histogram Operations
"""

import numpy as np

def _equalize_channel(channel):
    """Helper: equalize a single grayscale channel."""
    channel = np.asarray(channel, dtype=np.uint8)
    h, w = channel.shape
    total_pixels = h * w

    hist = np.bincount(channel.ravel(), minlength=256).astype(np.int64)
    cum_hist = np.cumsum(hist)
    lut = np.round((255.0 * cum_hist) / total_pixels).astype(np.uint8)
    return lut[channel]


def histogram_equalization(img):
    """
    Histogram equalization.
    Handle grayscale dan color (apply per channel).
    """
    img = np.asarray(img, dtype=np.uint8)
    if img.ndim == 2:
        return _equalize_channel(img)
    else:
        channels = [_equalize_channel(img[:, :, c]) for c in range(img.shape[2])]
        return np.stack(channels, axis=2).astype(np.uint8)


def histogram_matching(img, reference):
    """
    Histogram matching: adjust image histogram to match reference.
    """
    img = np.asarray(img, dtype=np.uint8)
    ref = np.asarray(reference, dtype=np.uint8)
    
    if img.ndim == 2:
        return _histogram_matching_channel(img, ref)
    else:
        channels = []
        for c in range(img.shape[2]):
            img_ch = img[:, :, c]
            ref_ch = ref[:, :, c]
            matched = _histogram_matching_channel(img_ch, ref_ch)
            channels.append(matched)
        return np.stack(channels, axis=2).astype(np.uint8)


def _histogram_matching_channel(img_ch, ref_ch):
    """Helper: histogram matching for a single channel."""
    img_ch = np.asarray(img_ch, dtype=np.uint8)
    ref_ch = np.asarray(ref_ch, dtype=np.uint8)
    
    # Cumulative distribution functions
    hist_img = np.bincount(img_ch.ravel(), minlength=256).astype(np.float64)
    hist_ref = np.bincount(ref_ch.ravel(), minlength=256).astype(np.float64)
    
    cdf_img = np.cumsum(hist_img) / hist_img.sum()
    cdf_ref = np.cumsum(hist_ref) / hist_ref.sum()
    
    # Mapping
    lut = np.zeros(256, dtype=np.uint8)
    for i in range(256):
        # Find closest CDF value in reference
        diff = np.abs(cdf_ref - cdf_img[i])
        lut[i] = np.argmin(diff)
    
    return lut[img_ch]
