"""
Point Operations
"""

import numpy as np

def negation(img):
    """Negasi: output = 255 - pixel."""
    img = np.asarray(img, dtype=np.float64)
    result = 255.0 - img
    return np.clip(result, 0, 255).astype(np.uint8)


def gamma_correction(img, gamma):
    """
    Koreksi gamma: output = 255 * (pixel/255)^(1/gamma)
    Normalize pixel ke 0-1, apply gamma, scale ke 0-255.
    """
    img = np.asarray(img, dtype=np.float64)
    normalized = img / 255.0
    corrected = np.power(normalized, 1.0 / gamma)
    result = corrected * 255.0
    return np.clip(result, 0, 255).astype(np.uint8)


def contrast_stretching(img, c_min=None, c_max=None, auto=True):
    """
    Contrast stretching: output = ((pixel - c_min) / (c_max - c_min)) * 255
    Jika auto=True: auto-detect c_min dan c_max dari image.
    Jika auto=False: gunakan c_min/c_max yang diberikan.
    """
    img = np.asarray(img, dtype=np.float64)
    if auto:
        c_min = img.min()
        c_max = img.max()
    else:
        if c_min is None:
            c_min = img.min()
        if c_max is None:
            c_max = img.max()

    if c_max == c_min:
        return np.zeros_like(img, dtype=np.uint8)

    result = ((img - c_min) / (c_max - c_min)) * 255.0
    return np.clip(result, 0, 255).astype(np.uint8)


def intensity_slicing(img, lower, upper, color_value=255):
    """
    Jika pixel dalam range [lower, upper]: set ke color_value, else: set ke 0.
    """
    img = np.asarray(img, dtype=np.float64)
    result = np.where((img >= lower) & (img <= upper), color_value, 0)
    return result.astype(np.uint8)


def bit_extraction(img, bit_position):
    """
    Bitwise operation: (pixel >> bit_position) & 1
    Jika bit = 1: output 255, jika bit = 0: output 0.
    """
    img = np.asarray(img, dtype=np.uint8)
    bits = (img >> bit_position) & 1
    result = np.where(bits == 1, 255, 0)
    return result.astype(np.uint8)


extract_bit = bit_extraction


def range_compression(img, c=10):
    """
    Dynamic range compression: output = c * log10(1 + |pixel|)
    Scale hasil ke 0-255.
    """
    img = np.asarray(img, dtype=np.float64)
    compressed = c * np.log10(1.0 + np.abs(img))
    c_min = compressed.min()
    c_max = compressed.max()
    if c_max == c_min:
        return np.zeros_like(img, dtype=np.uint8)
    result = ((compressed - c_min) / (c_max - c_min)) * 255.0
    return np.clip(result, 0, 255).astype(np.uint8)
