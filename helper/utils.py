"""
utils.py - Utility Functions
"""

import numpy as np
import cv2

_patch_cache = {}

def find_high_variance_patch(img, patch_size=8):
    """
    Cari region dengan variance tertinggi di dalam image dengan caching instan.
    """
    # Key cache berdasarkan shape, nilai sudut, dan patch_size
    img_arr = np.asarray(img)
    img_key = (img_arr.shape, float(img_arr[0, 0].flat[0]), float(img_arr[-1, -1].flat[0]), patch_size)
    if img_key in _patch_cache:
        return _patch_cache[img_key]

    if img_arr.ndim == 3:
        gray = cv2.cvtColor(img_arr, cv2.COLOR_RGB2GRAY)
    else:
        gray = img_arr

    h, w = gray.shape
    max_variance = -1.0
    best_coord = (0, 0)

    # Stride adaptif agar pencarian cepat bahkan pada gambar resolusi tinggi
    stride = max(patch_size // 2, int(min(h, w) / 128))
    stride = max(1, stride)

    for y in range(0, h - patch_size + 1, stride):
        for x in range(0, w - patch_size + 1, stride):
            patch = gray[y:y+patch_size, x:x+patch_size]
            variance = np.var(patch)
            if variance > max_variance:
                max_variance = variance
                best_coord = (y, x)

    _patch_cache[img_key] = best_coord
    return best_coord


def make_format_coord(target_img):
    def format_coord(x_val, y_val):
        c = int(round(x_val))
        r = int(round(y_val))
        if 0 <= r < target_img.shape[0] and 0 <= c < target_img.shape[1]:
            val = target_img[r, c]
            if target_img.ndim == 3:
                return f"x={c}, y={r} | RGB=({int(val[0])}, {int(val[1])}, {int(val[2])})"
            else:
                return f"x={c}, y={r} | Gray={int(val)}"
        return f"x={x_val:.0f}, y={y_val:.0f}"
    return format_coord
