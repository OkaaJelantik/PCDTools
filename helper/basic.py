"""
Basic Operations
"""

import numpy as np

def grayscale(img):
    """Konversi RGB ke grayscale dengan average RGB. Handle jika sudah grayscale."""
    img = np.asarray(img, dtype=np.float64)
    if img.ndim == 2:
        return img.astype(np.uint8)
    gray = (img[:, :, 0] + img[:, :, 1] + img[:, :, 2]) / 3.0
    return np.clip(gray, 0, 255).astype(np.uint8)


def brightness(img, delta):
    """Tambah/kurang brightness dengan clamp 0-255."""
    img = np.asarray(img, dtype=np.float64)
    result = img + delta
    return np.clip(result, 0, 255).astype(np.uint8)


def threshold(img, value):
    """Binary threshold: >= value → 255, else 0."""
    img = np.asarray(img, dtype=np.float64)
    result = np.where(img >= value, 255, 0)
    return result.astype(np.uint8)
