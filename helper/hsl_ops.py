"""
hsl_ops.py - HSL & Color Operations
"""

import numpy as np

def rgb_to_hsl(img):
    """
    Konversi RGB ke HSL.
    Returns: (h, s, l) masing-masing dalam range [0, 1]
    """
    img = np.asarray(img, dtype=np.float64) / 255.0
    if img.ndim == 2:
        img = np.stack([img, img, img], axis=2)
    
    r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    
    max_val = np.max(img, axis=2)
    min_val = np.min(img, axis=2)
    diff = max_val - min_val
    
    # Lightness
    l = (max_val + min_val) / 2.0
    
    # Saturation
    s = np.zeros_like(l)
    mask = diff != 0
    s[mask] = diff[mask] / (1.0 - np.abs(2.0 * l[mask] - 1.0))
    
    # Hue
    h = np.zeros_like(l)
    mask = diff != 0
    
    # Red channel is max
    mask_r = (max_val == r) & mask
    h[mask_r] = ((g[mask_r] - b[mask_r]) / diff[mask_r]) % 6.0
    
    # Green channel is max
    mask_g = (max_val == g) & mask
    h[mask_g] = ((b[mask_g] - r[mask_g]) / diff[mask_g]) + 2.0
    
    # Blue channel is max
    mask_b = (max_val == b) & mask
    h[mask_b] = ((r[mask_b] - g[mask_b]) / diff[mask_b]) + 4.0
    
    h = (h / 6.0) % 1.0
    
    return h, s, l


def hsl_to_rgb(h, s, l):
    """
    Konversi HSL ke RGB.
    h, s, l: masing-masing dalam range [0, 1]
    Returns: RGB array dalam range [0, 255]
    """
    h = np.asarray(h, dtype=np.float64)
    s = np.asarray(s, dtype=np.float64)
    l = np.asarray(l, dtype=np.float64)
    
    # Shape handling
    shape = h.shape
    h = h.flatten()
    s = s.flatten()
    l = l.flatten()
    
    c = (1.0 - np.abs(2.0 * l - 1.0)) * s
    x = c * (1.0 - np.abs((h * 6.0) % 2.0 - 1.0))
    m = l - c / 2.0
    
    # Initialize
    r = np.zeros_like(h)
    g = np.zeros_like(h)
    b = np.zeros_like(h)
    
    # 6 sectors
    mask = (h < 1/6)
    r[mask] = c[mask]
    g[mask] = x[mask]
    
    mask = (h >= 1/6) & (h < 2/6)
    r[mask] = x[mask]
    g[mask] = c[mask]
    
    mask = (h >= 2/6) & (h < 3/6)
    g[mask] = c[mask]
    b[mask] = x[mask]
    
    mask = (h >= 3/6) & (h < 4/6)
    g[mask] = x[mask]
    b[mask] = c[mask]
    
    mask = (h >= 4/6) & (h < 5/6)
    r[mask] = x[mask]
    b[mask] = c[mask]
    
    mask = (h >= 5/6)
    r[mask] = c[mask]
    b[mask] = x[mask]
    
    # Add m
    r += m
    g += m
    b += m
    
    # Reshape back
    r = r.reshape(shape)
    g = g.reshape(shape)
    b = b.reshape(shape)
    
    result = np.stack([r, g, b], axis=2) * 255.0
    return np.clip(result, 0, 255).astype(np.uint8)


def adjust_hue(img, hue_shift):
    """
    Adjust hue of an image.
    hue_shift: shift in degrees (-180 to 180)
    """
    img = np.asarray(img, dtype=np.uint8)
    if img.ndim == 2:
        img = np.stack([img, img, img], axis=2)
    
    h, s, l = rgb_to_hsl(img)
    h = (h + hue_shift / 360.0) % 1.0
    
    return hsl_to_rgb(h, s, l)


def adjust_saturation(img, saturation_factor):
    """
    Adjust saturation of an image.
    saturation_factor: multiplier > 0 (1.0 = no change)
    """
    img = np.asarray(img, dtype=np.uint8)
    if img.ndim == 2:
        img = np.stack([img, img, img], axis=2)
    
    h, s, l = rgb_to_hsl(img)
    s = np.clip(s * saturation_factor, 0, 1)
    
    return hsl_to_rgb(h, s, l)


def adjust_lightness(img, lightness_shift):
    """
    Adjust lightness of an image.
    lightness_shift: shift in range [-1.0, 1.0] (-1 = black, 1 = white)
    """
    img = np.asarray(img, dtype=np.uint8)
    if img.ndim == 2:
        img = np.stack([img, img, img], axis=2)
    
    h, s, l = rgb_to_hsl(img)
    l = np.clip(l + lightness_shift, 0, 1)
    
    return hsl_to_rgb(h, s, l)


def adjust_hsl(img, hue_shift=0, saturation_factor=1.0, lightness_shift=0):
    """
    Adjust all HSL parameters at once.
    hue_shift: shift in degrees (-180 to 180)
    saturation_factor: multiplier (0 to inf)
    lightness_shift: shift (-1.0 to 1.0)
    """
    img = np.asarray(img, dtype=np.uint8)
    if img.ndim == 2:
        img = np.stack([img, img, img], axis=2)
    
    h, s, l = rgb_to_hsl(img)
    h = (h + hue_shift / 360.0) % 1.0
    s = np.clip(s * saturation_factor, 0, 1)
    l = np.clip(l + lightness_shift, 0, 1)
    
    return hsl_to_rgb(h, s, l)
