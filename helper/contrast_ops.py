"""
contrast_ops.py - Contrast Operations
"""

import numpy as np
import cv2

def contrast_adjustment(img, factor):
    """
    Adjust contrast with factor > 0.
    factor=1.0: no change
    factor<1.0: decrease contrast
    factor>1.0: increase contrast
    Formula: output = 128 + (pixel - 128) * factor
    """
    img = np.asarray(img, dtype=np.float64)
    if img.ndim == 3:
        result = 128.0 + (img - 128.0) * factor
    else:
        result = 128.0 + (img - 128.0) * factor
    return np.clip(result, 0, 255).astype(np.uint8)


def contrast_linear(img, slope=1.0, intercept=0):
    """
    Linear contrast adjustment: output = slope * pixel + intercept
    """
    img = np.asarray(img, dtype=np.float64)
    result = img * slope + intercept
    return np.clip(result, 0, 255).astype(np.uint8)


def adaptive_contrast(img, kernel_size=8, clip_limit=2.0):
    """
    Adaptive contrast using CLAHE (Contrast Limited Adaptive Histogram Equalization).
    Requires OpenCV.
    """
    img = np.asarray(img, dtype=np.uint8)
    
    if img.ndim == 2:
        clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=(kernel_size, kernel_size))
        return clahe.apply(img)
    else:
        # Convert to LAB, apply CLAHE on L channel, convert back
        lab = cv2.cvtColor(img, cv2.COLOR_RGB2LAB)
        l, a, b = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=(kernel_size, kernel_size))
        l_eq = clahe.apply(l)
        lab_eq = cv2.merge([l_eq, a, b])
        return cv2.cvtColor(lab_eq, cv2.COLOR_LAB2RGB)
