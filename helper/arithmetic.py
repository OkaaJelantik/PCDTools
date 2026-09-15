"""
arithmetic.py - Image Arithmetic
"""

import numpy as np

def image_subtraction(img1, img2):
    """Subtraction: output = img1 - img2, clamp ke 0."""
    img1 = np.asarray(img1, dtype=np.float64)
    img2 = np.asarray(img2, dtype=np.float64)
    result = img1 - img2
    return np.clip(result, 0, 255).astype(np.uint8)

def image_addition(img1, img2):
    """Penjumlahan dua citra: output = img1 + img2, clamp 0-255."""
    img1 = np.asarray(img1, dtype=np.float64)
    img2 = np.asarray(img2, dtype=np.float64)
    result = img1 + img2
    return np.clip(result, 0, 255).astype(np.uint8)

def image_multiplication(img, k):
    """Perkalian citra dengan konstanta: output = img * k."""
    img = np.asarray(img, dtype=np.float64)
    result = img * k
    return np.clip(result, 0, 255).astype(np.uint8)


def image_division(img1, img2):
    """Pembagian dua citra: output = img1 / img2, hindari division by zero."""
    img1 = np.asarray(img1, dtype=np.float64)
    img2 = np.asarray(img2, dtype=np.float64)
    img2 = np.where(img2 == 0, 1, img2)
    result = img1 / img2
    return np.clip(result, 0, 255).astype(np.uint8)


def image_blending(img1, img2, p=0.5):
    """Pencampuran dua citra dengan parameter p (0-1)."""
    img1 = np.asarray(img1, dtype=np.float64)
    img2 = np.asarray(img2, dtype=np.float64)
    result = (p * img1) + ((1 - p) * img2)
    return np.clip(result, 0, 255).astype(np.uint8)


def logical_and(img1, img2):
    """Operasi logika AND (bitwise)."""
    img1 = np.asarray(img1, dtype=np.uint8)
    img2 = np.asarray(img2, dtype=np.uint8)
    return np.bitwise_and(img1, img2)


def logical_or(img1, img2):
    """Operasi logika OR (bitwise)."""
    img1 = np.asarray(img1, dtype=np.uint8)
    img2 = np.asarray(img2, dtype=np.uint8)
    return np.bitwise_or(img1, img2)


def logical_xor(img1, img2):
    """Operasi logika XOR (bitwise)."""
    img1 = np.asarray(img1, dtype=np.uint8)
    img2 = np.asarray(img2, dtype=np.uint8)
    return np.bitwise_xor(img1, img2)


def logical_not(img):
    """Operasi logika NOT (bitwise invert)."""
    img = np.asarray(img, dtype=np.uint8)
    return np.bitwise_not(img)


def bitshift_right(img, n):
    """Bitshift right sebesar n bit (setara pembagian 2^n)."""
    img = np.asarray(img, dtype=np.uint8)
    result = img >> n
    return result.astype(np.uint8)


def bitshift_left(img, n):
    """Bitshift left sebesar n bit (setara perkalian 2^n)."""
    img = np.asarray(img, dtype=np.uint8)
    result = (img << n).astype(np.uint8)
    return result


def image_averaging(img1, img2):
    """Averaging: output = (img1 + img2) / 2, round ke int."""
    img1 = np.asarray(img1, dtype=np.float64)
    img2 = np.asarray(img2, dtype=np.float64)
    result = (img1 + img2) / 2.0
    return np.clip(np.round(result), 0, 255).astype(np.uint8)
