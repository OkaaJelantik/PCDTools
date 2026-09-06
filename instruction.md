# Instruksi Operasi Titik - Updated

Update dari file OperasiTitik.md. Semua operasi di bawah perlu diimplementasiin di `helpers.py`.

## helpers.py - Semua Fungsi Operasi Titik

### Basic Operations (sudah ada):
1. **`grayscale(img)`** - Konversi RGB ke grayscale dengan average RGB
2. **`brightness(img, delta)`** - Tambah/kurang brightness dengan clamp 0-255
3. **`threshold(img, value)`** - Binary threshold (>=value → 255, else 0)

### New Point Operations:

4. **`negation(img)`**
   - Formula: output = 255 - pixel
   - Inverse warna (hitam jadi putih, putih jadi hitam)
   - Handle grayscale dan color images

5. **`gamma_correction(img, gamma)`**
   - Formula: output = 255 * (pixel/255)^(1/gamma)
   - gamma < 1 → lebih terang, gamma > 1 → lebih gelap
   - Normalize pixel ke 0-1, apply gamma, scale kembali ke 0-255

6. **`contrast_stretching(img, c_min=None, c_max=None, auto=True)`**
   - Formula: output = ((pixel - c_min) / (c_max - c_min)) * 255
   - Jika auto=True: auto-detect c_min dan c_max dari image
   - Jika auto=False: gunakan c_min/c_max yang diberikan
   - Clamp ke 0-255
   - Tarik range dinamis citra ke full 0-255

7. **`intensity_slicing(img, lower, upper, color_value=255)`**
   - Jika pixel dalam range [lower, upper]: set ke color_value (default 255)
   - Else: set ke 0
   - Highlight intensity range tertentu

8. **`bit_extraction(img, bit_position)`**
   - Extract bit ke-N dari setiap pixel
   - Jika bit = 1: output 255, jika bit = 0: output 0
   - Bitwise operation: `(pixel >> bit_position) & 1`

9. **`range_compression(img, c=10)`**
   - Formula: output = c * log10(1 + |pixel|)
   - Compress dynamic range menggunakan logaritm
   - Scale hasil ke 0-255

10. **`histogram_equalization(img)`**
    - Compute histogram, cumulative histogram
    - Map setiap gray level ke nilai baru berdasarkan CDF
    - Formula: new_value = round((255 * cumulative_freq) / total_pixels)
    - Return equalized image
    - Bisa pake cv2.equalizeHist() atau implement manual

### Image Arithmetic (butuh 2 images):

11. **`image_subtraction(img1, img2)`**
    - Formula: output = img1 - img2
    - Jika negatif: clamp ke 0
    - Kedua image harus same shape

12. **`image_averaging(img1, img2)`**
    - Formula: output = (img1 + img2) / 2
    - Round ke int
    - Kedua image harus same shape

---

## show_result() - Tetap sama
```python
def show_result(before, after, title="Result", patch_size=8):
    # 2x2 grid: [before, after] top row, [histogram, pixel chunk] bottom
    # Sama seperti sebelumnya
```

---

## tugas.ipynb - Updated Structure

### Cell 1: Setup
```python
from helpers import *
import cv2
import numpy as np
from ipywidgets import interact, FloatSlider, IntSlider
%matplotlib widget
print("✅ Environment Ready!")
```

### Cell 2: Create/Load Test Image
```python
# Create gradient test image
test_img = np.zeros((256, 256, 3), dtype=np.uint8)
for i in range(256):
    test_img[:, i] = [i, i, i]
```

### Cell 3-5: Basic Operations (sudah ada)
```python
# Grayscale, Brightness, Threshold
```

### Cell 6: Negation
```python
neg_result = negation(test_img)
show_result(test_img, neg_result, "Negation")
```

### Cell 7: Interactive Gamma Correction
```python
@interact(gamma=(0.2, 3.0, 0.1))
def adjust_gamma(gamma):
    gamma_img = gamma_correction(test_img, gamma)
    show_result(test_img, gamma_img, f"Gamma {gamma:.1f}")
```

### Cell 8: Interactive Contrast Stretching
```python
@interact(auto=[True, False])
def adjust_contrast(auto):
    contrast_img = contrast_stretching(test_img, auto=auto)
    show_result(test_img, contrast_img, f"Contrast Stretching (auto={auto})")
```

### Cell 9: Interactive Intensity Slicing
```python
@interact(lower=(0, 255, 10), upper=(0, 255, 10))
def slice_intensity(lower, upper):
    if lower > upper:
        lower, upper = upper, lower
    sliced = intensity_slicing(test_img, lower, upper)
    show_result(test_img, sliced, f"Intensity Slicing [{lower}-{upper}]")
```

### Cell 10: Interactive Bit Extraction
```python
@interact(bit=(0, 7, 1))
def extract_bit(bit):
    bit_img = bit_extraction(test_img, bit)
    show_result(test_img, bit_img, f"Bit Extraction (Bit {bit})")
```

### Cell 11: Interactive Range Compression
```python
@interact(c=(1, 20, 1))
def compress_range(c):
    compressed = range_compression(test_img, c)
    show_result(test_img, compressed, f"Range Compression (c={c})")
```

### Cell 12: Histogram Equalization
```python
equalized = histogram_equalization(test_img)
show_result(test_img, equalized, "Histogram Equalization")
```

### Cell 13: Image Subtraction (2 images)
```python
# Buat 2 test images
img1 = np.full((256, 256, 3), 100, dtype=np.uint8)
img2 = np.full((256, 256, 3), 50, dtype=np.uint8)
result_sub = image_subtraction(img1, img2)
# Tampilkan side-by-side atau dengan show_result
```

### Cell 14: Image Averaging
```python
result_avg = image_averaging(img1, img2)
# Tampilkan hasil
```

---

## Priority Implementation
1. ✅ Grayscale, Brightness, Threshold (sudah ada)
2. ✅ Negation, Gamma Correction, Contrast Stretching
3. ✅ Intensity Slicing, Bit Extraction
4. ✅ Range Compression, Histogram Equalization
5. ✅ Image Subtraction, Image Averaging

---

## Notes
- Semua operasi handle both grayscale (H,W) dan color (H,W,3)
- Output selalu uint8, range 0-255
- Clipping otomatis di setiap operasi
- `show_result()` visualisasi before/after + histogram + pixel chunk
- Histogram equalization bisa manual atau `cv2.equalizeHist()`
