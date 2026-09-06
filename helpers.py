"""
helpers.py - Fungsi-fungsi pengolahan citra digital untuk proyek PCD
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2


# ---------------------------------------------------------------------------
# Basic Operations
# ---------------------------------------------------------------------------

def grayscale(img):
    """Konversi RGB ke grayscale dengan average RGB. Handle jika sudah grayscale."""
    img = np.array(img, dtype=np.float64)
    if img.ndim == 2:
        return img.astype(np.uint8)
    gray = (img[:, :, 0] + img[:, :, 1] + img[:, :, 2]) / 3.0
    return np.clip(gray, 0, 255).astype(np.uint8)


def brightness(img, delta):
    """Tambah/kurang brightness dengan clamp 0-255."""
    img = np.array(img, dtype=np.float64)
    result = img + delta
    return np.clip(result, 0, 255).astype(np.uint8)


def threshold(img, value):
    """Binary threshold: >= value → 255, else 0."""
    img = np.array(img, dtype=np.float64)
    result = np.where(img >= value, 255, 0)
    return result.astype(np.uint8)


# ---------------------------------------------------------------------------
# New Point Operations
# ---------------------------------------------------------------------------

def negation(img):
    """Negasi: output = 255 - pixel. Handle grayscale dan color images."""
    img = np.array(img, dtype=np.float64)
    result = 255.0 - img
    return np.clip(result, 0, 255).astype(np.uint8)


def gamma_correction(img, gamma):
    """
    Koreksi gamma: output = 255 * (pixel/255)^(1/gamma)
    Normalize pixel ke 0-1, apply gamma, scale ke 0-255.
    """
    img = np.array(img, dtype=np.float64)
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
    img = np.array(img, dtype=np.float64)
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
    img = np.array(img, dtype=np.float64)
    result = np.where((img >= lower) & (img <= upper), color_value, 0)
    return result.astype(np.uint8)


def bit_extraction(img, bit_position):
    """
    Bitwise operation: (pixel >> bit_position) & 1
    Jika bit = 1: output 255, jika bit = 0: output 0.
    """
    img = np.array(img, dtype=np.uint8)
    bits = (img >> bit_position) & 1
    result = np.where(bits == 1, 255, 0)
    return result.astype(np.uint8)


extract_bit = bit_extraction


def range_compression(img, c=10):
    """
    Dynamic range compression: output = c * log10(1 + |pixel|)
    Scale hasil ke 0-255.
    """
    img = np.array(img, dtype=np.float64)
    compressed = c * np.log10(1.0 + np.abs(img))
    c_min = compressed.min()
    c_max = compressed.max()
    if c_max == c_min:
        return np.zeros_like(img, dtype=np.uint8)
    result = ((compressed - c_min) / (c_max - c_min)) * 255.0
    return np.clip(result, 0, 255).astype(np.uint8)


def _equalize_channel(channel):
    """Helper: equalize a single grayscale channel."""
    channel = np.array(channel, dtype=np.uint8)
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
    img = np.array(img, dtype=np.uint8)
    if img.ndim == 2:
        return _equalize_channel(img)
    else:
        channels = [_equalize_channel(img[:, :, c]) for c in range(img.shape[2])]
        return np.stack(channels, axis=2).astype(np.uint8)


# ---------------------------------------------------------------------------
# Image Arithmetic
# ---------------------------------------------------------------------------

def image_subtraction(img1, img2):
    """Subtraction: output = img1 - img2, clamp ke 0."""
    img1 = np.array(img1, dtype=np.float64)
    img2 = np.array(img2, dtype=np.float64)
    result = img1 - img2
    return np.clip(result, 0, 255).astype(np.uint8)


def image_averaging(img1, img2):
    """Averaging: output = (img1 + img2) / 2, round ke int."""
    img1 = np.array(img1, dtype=np.float64)
    img2 = np.array(img2, dtype=np.float64)
    result = (img1 + img2) / 2.0
    return np.clip(np.round(result), 0, 255).astype(np.uint8)


# ---------------------------------------------------------------------------
# Display Helper
# ---------------------------------------------------------------------------

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


def show_result(before, after, title="Result", patch_size=8, patch_coord=None):
    """
    Visualisasi before/after, masing-masing dengan histogram dan pixel patch sendiri.

    Layout (2 rows x 3 cols):
        Row 1: [Before Image]     [Before Histogram]  [Before Patch]
        Row 2: [After Image]      [After Histogram]   [After Patch]

    Args:
        before: image sebelum operasi
        after: image sesudah operasi
        title: judul keseluruhan
        patch_size: ukuran patch pixel (default 8x8)
        patch_coord: (y, x) koordinat patch manual. Jika None, auto-detect
                     patch dengan variance tertinggi dari 'before' image.
                     Koordinat yang sama dipakai untuk 'after' biar konsisten.
    """
    fig_id = title.split('(')[0].split('[')[0].strip()
    plt.close(fig_id)
    fig, axes = plt.subplots(2, 3, figsize=(15, 10), num=fig_id)
    fig.canvas.header_visible = False
    fig.suptitle(title, fontsize=16)

    before = np.array(before, dtype=np.uint8)
    after = np.array(after, dtype=np.uint8)

    # Auto-detect patch coordinate dari before image
    if patch_coord is None:
        patch_coord = find_high_variance_patch(before, patch_size)
    y, x = patch_coord

    images_data = [('Before', before), ('After', after)]

    for row, (label, img) in enumerate(images_data):
        # Prepare display and grayscale versions
        if img.ndim == 3:
            img_display = img  # assume RGB already
            img_gray = np.mean(img, axis=2).astype(np.uint8)
        else:
            img_display = img
            img_gray = img

        # --- Col 0: Image with red rectangle showing patch location ---
        ax_img = axes[row, 0]
        if img.ndim == 2:
            ax_img.imshow(img_display, cmap='gray', vmin=0, vmax=255)
        else:
            ax_img.imshow(img_display)
        ax_img.format_coord = make_format_coord(img)
        ax_img.set_title(f"{label} Image")
        ax_img.axis('off')
        rect = plt.Rectangle((x, y), patch_size, patch_size,
                              edgecolor='red', facecolor='none', linewidth=2)
        ax_img.add_patch(rect)

        # --- Col 1: Histogram ---
        ax_hist = axes[row, 1]
        ax_hist.set_title(f"{label} Histogram")
        ax_hist.set_xlabel("Intensity")
        ax_hist.set_ylabel("Frequency")
        ax_hist.set_xlim([0, 256])
        if img.ndim == 2:
            ax_hist.plot(np.bincount(img_gray.ravel(), minlength=256),
                        color='steelblue', linewidth=0.8)
        else:
            colors = ('red', 'green', 'blue')
            labels_ch = ('R', 'G', 'B')
            for i, (col, lbl_ch) in enumerate(zip(colors, labels_ch)):
                hist_vals = np.bincount(img[:, :, i].ravel(), minlength=256)
                ax_hist.plot(hist_vals, color=col, label=lbl_ch, linewidth=0.8)
            ax_hist.legend(loc='upper right')

        # --- Col 2: Pixel Patch Heatmap (grayscale values) ---
        ax_patch = axes[row, 2]
        ps_h = min(patch_size, img_gray.shape[0] - y)
        ps_w = min(patch_size, img_gray.shape[1] - x)
        patch = img_gray[y:y+ps_h, x:x+ps_w].astype(int)

        # Heatmap menggunakan matplotlib imshow (kompatibel 100% dengan widget/ipympl)
        ax_patch.imshow(patch, cmap='viridis', aspect='equal', vmin=0, vmax=255)
        for r in range(ps_h):
            for c in range(ps_w):
                val = patch[r, c]
                # Text color putih untuk nilai gelap, hitam untuk nilai terang
                text_color = 'white' if val < 128 else 'black'
                ax_patch.text(c, r, str(val), ha='center', va='center',
                              fontsize=7, color=text_color)

        ax_patch.set_title(f"{label} Pixel Patch ({ps_h}x{ps_w})")
        ax_patch.set_xticks([])
        ax_patch.set_yticks([])

    plt.tight_layout()
    plt.show()
