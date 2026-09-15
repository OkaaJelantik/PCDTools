"""
display.py - Display Helpers
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2
from .utils import find_high_variance_patch, make_format_coord

def show_result(before, after, title="Result", formula=None, patch_size=8, patch_coord=None):
    """
    Visualisasi before/after dengan ID unik dari judul.
    """
    fig_id = title.split('(')[0].split('[')[0].strip()
    plt.close(fig_id)  # <-- Hapus figure lama dengan ID ini
    
    fig = plt.figure(fig_id, figsize=(12, 8))
    fig.clear()
    fig.suptitle(title, fontsize=16)
    
    axes = fig.subplots(2, 3)
    # Tampilkan formula jika ada
    if formula:
        fig.text(0.5, 0.02, f"Rumus: {formula}", ha='center', fontsize=12,
             style='italic', bbox=dict(facecolor='lightyellow', alpha=0.8, boxstyle='round,pad=0.5'))
        # Perbaikan: pakai fig.tight_layout, tambah h_pad (spasi vertikal antar baris)
        fig.tight_layout(rect=[0, 0.12, 1, 0.95], pad=1.5, h_pad=3.0, w_pad=1.5)
    else:
        # Perbaikan: tambah h_pad biar baris atas dan bawah gak dempet
        fig.tight_layout(pad=1.5, h_pad=3.0, w_pad=1.5)

    before = np.asarray(before, dtype=np.uint8)
    after = np.asarray(after, dtype=np.uint8)

    # Auto-detect patch coordinate dari before image
    if patch_coord is None:
        patch_coord = find_high_variance_patch(before, patch_size)
    y, x = patch_coord

    images_data = [('Before', before), ('After', after)]

    for row, (label, img) in enumerate(images_data):
        # Prepare display and grayscale versions
        if img.ndim == 3:
            img_display = img
            img_gray = np.mean(img, axis=2).astype(np.uint8)
        else:
            img_display = img
            img_gray = img

        # --- Kolom 0: Gambar ---
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

        # --- Kolom 1: Histogram ---
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

        # --- Kolom 2: Pixel Patch Heatmap ---
        ax_patch = axes[row, 2]
        ps_h = min(patch_size, img_gray.shape[0] - y)
        ps_w = min(patch_size, img_gray.shape[1] - x)
        patch = img_gray[y:y+ps_h, x:x+ps_w].astype(int)

        ax_patch.imshow(patch, cmap='viridis', aspect='equal', vmin=0, vmax=255)
        for r in range(ps_h):
            for c in range(ps_w):
                val = patch[r, c]
                text_color = 'white' if val < 128 else 'black'
                ax_patch.text(c, r, str(val), ha='center', va='center',
                              fontsize=7, color=text_color)

        ax_patch.set_title(f"{label} Pixel Patch ({ps_h}x{ps_w})")
        ax_patch.set_xticks([])
        ax_patch.set_yticks([])

    plt.show()


def show_hsl_components(img, title="HSL Components"):
    """
    Tampilkan komponen HSL (Hue, Saturation, Lightness) dari sebuah gambar.
    """
    from .hsl_ops import rgb_to_hsl
    
    img = np.asarray(img, dtype=np.uint8)
    if img.ndim == 2:
        img = np.stack([img, img, img], axis=2)
    
    h, s, l = rgb_to_hsl(img)
    
    # Convert each component to visual representation
    hue_vis = (h * 180).astype(np.uint8)  # HSV hue range 0-180
    sat_vis = (s * 255).astype(np.uint8)
    light_vis = (l * 255).astype(np.uint8)
    
    # For hue, use color map
    hue_rgb = cv2.cvtColor(np.stack([hue_vis, np.ones_like(hue_vis)*255, np.ones_like(hue_vis)*255], axis=2).astype(np.uint8), cv2.COLOR_HSV2RGB)
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 8))
    fig.suptitle(title, fontsize=16)
    
    # Original
    axes[0, 0].imshow(img)
    axes[0, 0].set_title("Original Image")
    axes[0, 0].axis('off')
    
    # Hue
    axes[0, 1].imshow(hue_rgb)
    axes[0, 1].set_title("Hue Component")
    axes[0, 1].axis('off')
    
    # Saturation
    axes[0, 2].imshow(sat_vis, cmap='gray', vmin=0, vmax=255)
    axes[0, 2].set_title("Saturation Component")
    axes[0, 2].axis('off')
    
    # Lightness
    axes[1, 0].imshow(light_vis, cmap='gray', vmin=0, vmax=255)
    axes[1, 0].set_title("Lightness Component")
    axes[1, 0].axis('off')
    
    # RGB Histogram
    axes[1, 1].set_title("RGB Histogram")
    axes[1, 1].set_xlabel("Intensity")
    axes[1, 1].set_ylabel("Frequency")
    axes[1, 1].set_xlim([0, 256])
    colors = ('red', 'green', 'blue')
    labels_ch = ('R', 'G', 'B')
    for i, (col, lbl_ch) in enumerate(zip(colors, labels_ch)):
        hist_vals = np.bincount(img[:, :, i].ravel(), minlength=256)
        axes[1, 1].plot(hist_vals, color=col, label=lbl_ch, linewidth=0.8)
    axes[1, 1].legend(loc='upper right')
    
    # HSL Histograms
    axes[1, 2].set_title("HSL Histograms")
    axes[1, 2].set_xlabel("Value")
    axes[1, 2].set_ylabel("Frequency")
    axes[1, 2].hist(h.flatten(), bins=32, alpha=0.5, label='Hue', color='red')
    axes[1, 2].hist(s.flatten(), bins=32, alpha=0.5, label='Saturation', color='green')
    axes[1, 2].hist(l.flatten(), bins=32, alpha=0.5, label='Lightness', color='blue')
    axes[1, 2].legend(loc='upper right')
    
    plt.tight_layout()
    plt.show()
