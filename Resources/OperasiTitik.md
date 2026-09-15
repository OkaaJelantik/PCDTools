<!-- Slide number: 1 -->
# OPERASI TITIK PADA IMAGE ENHANCEMENT

<!-- Slide number: 2 -->
# pendahuluan
Perbaikan citra bertujuan untuk meningkatkan kualitas tampilan citra untuk pandangan manusia atau untuk mengkonversi suatu citra agar memiliki format yang lebih baik sehingga citra tersebut menjadi lebih mudah diolah dengan mesin (komputer)

Peningkatan kualitas citra merupakan langkah pra pengolahan yang penting sebelum melakukan proses analisis dan representasi citra

Perbaikan terhadap suatu citra dapat dilakukan dengan operasi titik (point operation), operasi spasial (spatial operation), operasi geometri (geometric operation) dan operasi aritmatika (arithmatic operation)

Pembahasan hanya dilakukan terhadap operasi titik

<!-- Slide number: 3 -->
# Operasi titik
Operasi titik dilakukan dengan mengoperasikan piksel, tanpa memperhatikan konsep tetangga (neighborhood), sehingga lebih mudah dilakukan

Operasi titik biasanya digambarkan dalam bentuk histogram citra

<!-- Slide number: 4 -->
# Histogram citra
Histogram adalah grafik yang menunjukkan frekuensi kemunculan setiap nilai gradasi warna

Histogram menampilkan banyaknya piksel dalam suatu citra yang dikelompokkan berdasarkan level nilai intensitas piksel yang berbeda

Histogram citra ditampilkan dalam grafik dua dimensi (2D), dengan sumbu x menyatakan nilai intensitas piksel dan sumbu y menyatakan frekuensi kemunculan suatu nilai intensitas piksel

<!-- Slide number: 5 -->
# Jenis citra

Citra Biner
Memiliki hanya 2 kemungkinan warna yaitu hitam dan putih
Citra Gray scale
Memiliki warna hitam,  keabuan dan  putih
Citra warna (8bit)
Memiliki jumlah warna maksimum 256 warna
Citra warna (16 bit)
Memiliki 65.536 warna
Citra warna (24 bit)
Memiliki 16.777.216 warna

<!-- Slide number: 6 -->
# Citra grayscale
Peningkatan kualitas citra dapat dilakukan melalui transformasi intensitas citra, yaitu besar intensitas setiap piksel pada citra diubah, tetapi dengan posisi piksel yang tetap

Transformasi ini dapat dilakukan dengan menggunakan fungsi transformasi skala keabuan atau Gray-Scale Transformation Function

Fungsi ini memetakan fungsi input fi(x,y) yang bertindak sebagai citra input menjadi fungsi output fo(x,y) yang bertindak sebagai citra output

<!-- Slide number: 7 -->
Citra warna dapat diubah menjadi citra grayscale dengan cara menghitung rata-rata elemen warna Red, Green dan Blue (RGB)

Secara matematis, dapat ditulis sebagai berikut:

<!-- Slide number: 8 -->
Contoh Kasus:

	Diketahui citra warna 7 bit (128 warna) dengan ukuran 3 x 3  akan diubah menjadi citra grayscale
| R = 50 G = 65 B = 50 | R = 40 G = 40 B = 55 | R = 90 G = 60 B = 90 |
| --- | --- | --- |
| R = 40 G = 80 B = 30 | R = 50 G = 80 B = 50 | R = 40 G = 90 B = 80 |
| R = 80 G = 60 B = 40 | R = 70 G = 70 B = 70 | R = 80 G = 90 B = 70 |

<!-- Slide number: 9 -->
Proses Transformasi Grayscale:

Posisi (0,0)	= (50 + 65 + 50) / 3 = 55
Posisi (0,1)	= (40 + 40 + 50) / 3 = 45
Posisi (0,2)	= (90 + 60 + 90) / 3 = 80
Posisi (1,0)	= (40 + 80 + 30) / 3 = 50
Posisi (1,1)	= (50 + 80 + 50) / 3 = 60
Posisi (1,2)	= (40 + 90 + 80) / 3 = 70
Posisi (2,0)	= (80 + 60 + 40) / 3 = 60
Posisi (2,1)	= (70 + 70 + 70) / 3 = 70
Posisi (2,2)	= (80 + 90 + 70) / 3 = 80

Matriks Grayscale:

![](Picture4.jpg)

<!-- Slide number: 10 -->
Histogram Citra Grayscale:

![](Picture1.jpg)

![](Picture7.jpg)

<!-- Slide number: 11 -->
# Brightness adjustment
Tingkat kecerahan suatu citra dapat dilihat dari histogramnya

Semakin tinggi tingkat kecerahan suatu citra maka konsentrasi nilai piksel pada histogram akan bergeser ke sisi kanan, sebaliknya semakin rendah tingkat kecerahan suatu citra maka konsentrasi nilai piksel pada histogram akan bergeser ke sisi kiri

Untuk mengontrol nilai warna citra agar diperoleh tingkat kecerahan sesuai dengan yang diinginkan, maka dapat menggunakan fungsi sebagai berikut

	U’ adalah citra setelah operasi, U adalah citra sebelum operasi dan c adalah konstanta penyesuaian

![](Picture3.jpg)

<!-- Slide number: 12 -->
Apabila nilai piksel setelah operasi melebihi nilai maksimum intensitas, maka nilai piksel akan dijadikan nilai maksimum intensitas

Apabila nilai piksel setelah operasi lebih kecil dari nol, maka nilai piksel akan dijadikan nol

Contoh Kasus:

	Pada citra grayscale sebelumnya, akan dilakukan proses peningkatan kecerahan, dengan nilai peningkatan sebesar:
			c = 50

<!-- Slide number: 13 -->
Proses Peningkatan Kecerahan:

Posisi (0,0)	=  55 + 50 = 105
Posisi (0,1)	=  45 + 50 =  95
Posisi (0,2)	=  80 + 50 = 130
Posisi (1,0)	=  50 + 50 = 100
Posisi (1,1)	=  60 + 50 = 110
Posisi (1,2)	=  70 + 50 = 120
Posisi (2,0)	=  60 + 50 = 110
Posisi (2,1)	=  70 + 50 = 120
Posisi (2,2)	=  80 + 50 = 130

Matriks Citra Hasil :

![](Picture2.jpg)

<!-- Slide number: 14 -->
Histogram Citra Hasil:

![](Picture6.jpg)

<!-- Slide number: 15 -->

# Negation
Negasi adalah proses pemetaan nilai piksel suatu citra

Pada citra biner, piksel hitam dijadikan putih dan piksel putih dijadikan hitam

Pada citra grayscale, nilai maksimum piksel dikurangi dengan nilai piksel yang sedang diproses

Secara matematis dapat ditulis sebagai berikut

	U’ adalah citra setelah operasi, U adalah citra sebelum operasi, l adalah nilai bit dari gray level

![](Picture5.jpg)

<!-- Slide number: 16 -->
Contoh Kasus:
	Pada citra grayscale sebelumnya, akan dilakukan proses negasi

Posisi (0,0)	=  255 – 55 = 200
Posisi (0,1)	=  255 – 45 = 210
Posisi (0,2)	=  255 – 80 = 175
Posisi (1,0)	=  255 – 50 = 200
Posisi (1,1)	=  255 – 60 = 195
Posisi (1,2)	=  255 – 70 = 185
Posisi (2,0)	=  255 – 60 = 195
Posisi (2,1)	=  255 – 70 = 185
Posisi (2,2)	=  255 – 80 = 175

Matriks Citra Hasil:

![](Picture1.jpg)

<!-- Slide number: 17 -->
Histogram Citra Hasil:

![](Picture1.jpg)

<!-- Slide number: 18 -->
# Koreksi gamma
Brightness suatu citra dapat diperbaiki dengan menggunakan koreksi gamma
Bentuk umum dari transformasi gamma adalah:

	U’ adalah citra setelah operasi, U adalah citra sebelum operasi dan  adalah faktor koreksi gamma (0 <  < 1)

Semakin kecil faktor koreksi, maka citra output akan semakin terang

Semakin tinggi faktor koreksi, maka citra output akan mendekati citra asli

![](Picture3.jpg)

<!-- Slide number: 19 -->

Contoh Kasus:
	Pada citra grayscale sebelumnya, akan dilakukan proses koreksi gamma, dengan nilai gamma :  = 0.8

Posisi (0,0)	=  551/0.8	 = 150
Posisi (0,1)	=  451/0.8	 = 117
Posisi (0,2)	=  801/0.8	 = 239
Posisi (1,0)	=  501/0.8	 = 133
Posisi (1,1)	=  601/0.8	 = 167
Posisi (1,2)	=  701/0.8	 = 202
Posisi (2,0)	=  601/0.8	 = 167
Posisi (2,1)	=  701/0.8	 = 202
Posisi (2,2)	=  801/0.8	 = 239

Matriks Citra Hasil:

![](Picture1.jpg)

<!-- Slide number: 20 -->

Histogram Citra Hasil:

![](Picture2.jpg)

<!-- Slide number: 21 -->
# Contrast stretching
Teknik untuk memperbaiki kontras citra terutama citra yang memiliki kontras rendah
Pada perenggangan kontras, setiap piksel pada citra U ditransformasi dengan menggunakan fungsi berikut

o(i,j) adalah piksel sesudah ditransformasi pada koordinat (i,j), u(i,j) adalah piksel sebelum ditransformasi pada koordinat (i,j), c adalah nilai minimum dari piksel pada citra input, d adalah nilai maksimum dari piksel pada citra input, dan L adalah nilai grayscale maksimum
Jika nilai piksel lebih kecil dari 0 maka akan dijadikan 0, dan jika nilai piksel lebih besar dari L maka akan dijadikan L

<!-- Slide number: 22 -->

Masalah : jika nilai piksel terlalu tinggi dan terlalu rendah, tetapi jumlah piksel tersebut sangat sedikit

Solusi : menggunakan p% piksel < c dan q% piksel > d

![](Picture5.jpg)

<!-- Slide number: 23 -->

Contoh Kasus 1:

	Pada citra grayscale sebelumnya, akan dilakukan proses contrast stretching. Nilai piksel minimum (c)= 45, nilai piksel maksimum (d)= 80, dan nilai grayscale maksimum (L) = 255

Posisi (0,0)	=  ((55 – 45)/(80 – 45)) * (255) = 73
Posisi (0,1)	=  ((45 – 45)/(80 – 45)) * (255) = 0
Posisi (0,2)	=  ((80 – 45)/(80 – 45)) * (255) = 255
Posisi (1,0)	=  ((50 – 45)/(80 – 45)) * (255)  = 36
Posisi (1,1)	=  ((60 – 45)/(80 – 45)) * (255)  = 109
Posisi (1,2)	=  ((70 – 45)/(80 – 45)) * (255) = 181
Posisi (2,0)	=  ((65 – 45)/(80 – 45)) * (255) = 109
Posisi (2,1)	=  ((70 – 45)/(80 – 45)) * (255) = 181
Posisi (2,2)	=  ((80 – 45)/(80 – 45)) * (255) = 255

Matriks Citra Hasil:

![](Picture2.jpg)

<!-- Slide number: 24 -->

Histogram Citra Hasil:

![](Picture2.jpg)

<!-- Slide number: 25 -->

Contoh Kasus 2:

	Pada citra grayscale sebelumnya, akan dilakukan proses contrast stretching dengan menaikkan persentasi c sebesar 20% dan d sebesar 10%.
	Nilai piksel minimum (c)= 45 + (20%*45) = 45 + 9 = 54
	Nilai piksel maksimum (d)= 80 – (10%*80) = 80 – 8 = 72
	Nilai grayscale maksimum (L) = 255

<!-- Slide number: 26 -->

Posisi (0,0)	=  ((55 – 54)/(72 – 54)) * (255)  = 14, karena 54 ≤ 55 ≤ 72
Posisi (0,1)	=  0 , karena 45 < 54
Posisi (0,2)	=  255, karena 80 > 72
Posisi (1,0)	=  0 , karena 50 < 54
Posisi (1,1)	=  ((60 – 54)/(72 – 54)) * (255) = 85, karena 54 ≤ 60 ≤ 72
Posisi (1,2)	=  ((70 – 54)/(72 – 54)) * (255)  = 226, karena 54 ≤ 70 ≤ 72
Posisi (2,0)	=  ((65 – 54)/(72 – 54)) * (255) = 155, karena 50 ≤ 65 ≤ 72
Posisi (2,1)	=  ((70 – 54)/(72 – 54)) * (255) = 226, karena 50 ≤ 70 ≤ 72
Posisi (2,2)	=  255, karena 80 > 72

Matriks Citra Hasil:

![](Picture3.jpg)

<!-- Slide number: 27 -->

Histogram Citra Hasil:

![](Picture1.jpg)

<!-- Slide number: 28 -->
# Intensity slicing
Berguna ketika ingin menonjolkan intensitas (gray level) tertentu pada citra

Pendekatan pertama: memberi nilai tinggi pada rentangan nilai intensitas yang ingin ditonjolkan dan nilai intensitas yang lainnya diberi nilai rendah
Dipilih jika latar belakang ingin diabaikan
Dapat ditulis:

![](Picture5.jpg)

<!-- Slide number: 29 -->

Pendekatan kedua: memberi nilai tinggi pada rentangan nilai intensitas yang ingin ditonjolkan dan nilai intensitas yang lainnya tetap dipertahankan
Dipilih jika latar belakang ingin dipertahankan
Dapat ditulis:

	dengan a dan b menyatakan nilai batas bawah dan atas intensitas yang mau ditonjolkan

![](Picture3.jpg)

<!-- Slide number: 30 -->

Contoh Kasus 1:

	Pada citra grayscale sebelumnya, akan dilakukan proses intensity slicing pada interval  60 – 70 dengan memberikan nilai rendah pada piksel diluar interval

Posisi (0,0)	=  0, karena 55 diluar interval 60 - 70
Posisi (0,1)	=  0, karena 45 diluar interval 60 - 70
Posisi (0,2)	=  0, karena 80 diluar interval 60 - 70
Posisi (1,0)	=  0, karena 50 diluar interval 60 - 70
Posisi (1,1)	=  255, karena 60 didalam interval 60 - 70
Posisi (1,2)	=  255, karena 70 didalam interval 60 - 70
Posisi (2,0)	=  255, karena 65 didalam interval 60 - 70
Posisi (2,1)	=  255, karena 70 didalam interval 60 - 70
Posisi (2,2) =  0, karena 80 diluar interval 60 – 70

<!-- Slide number: 31 -->

Matriks Citra Hasil:

![](Picture1.jpg)

<!-- Slide number: 32 -->

Histogram Citra Hasil:

![](Picture1.jpg)

<!-- Slide number: 33 -->

Contoh Kasus 2:

	Pada citra grayscale sebelumnya, akan dilakukan proses intensity slicing pada interval  60 – 70 dengan mempertahankan nilai piksel pada piksel diluar interval

Posisi (0,0)	=  55, karena 55 diluar interval 60 - 70
Posisi (0,1)	=  45, karena 45 diluar interval 60 - 70
Posisi (0,2)	=  80, karena 80 diluar interval 60 - 70
Posisi (1,0)	=  50, karena 50 diluar interval 60 - 70
Posisi (1,1)	=  255, karena 60 didalam interval 60 - 70
Posisi (1,2)	=  255, karena 70 didalam interval 60 - 70
Posisi (2,0)	=  255, karena 65 didalam interval 60 - 70
Posisi (2,1)	=  255, karena 70 didalam interval 60 - 70
Posisi (2,2) 	=  80, karena 80 diluar interval 60 – 70

<!-- Slide number: 34 -->

Matriks Citra Hasil:

![](Picture1.jpg)

<!-- Slide number: 35 -->

Histogram Citra Hasil:

![](Picture1.jpg)

<!-- Slide number: 36 -->
# BIT EXTRACTION
Metode memisahkan beberapa bit dari piksel untuk menghasilkan nilai piksel yang baru
Setiap piksel pada citra dapat dinyatakan dengan komposisi bit sebagai berikut:

Nilai piksel baru dapat diperoleh dengan:

	dengan:

![](Picture6.jpg)

![](Picture1.jpg)

![](Picture3.jpg)

![](Picture8.jpg)

<!-- Slide number: 37 -->

Contoh Kasus:
	Pada citra grayscale sebelumnya, akan dilakukan proses ekstraksi bit, pada bit ke-6

Posisi (0,0)	=  55	= 00110111  0, karena bit ke-6 bernilai 0
Posisi (0,1)	=  45	= 00101101  0, karena bit ke-6 bernilai 0
Posisi (0,2)	=  80	= 01010000  255, karena bit ke-6 bernilai 1
Posisi (1,0)	=  50	= 00110010  0, karena bit ke-6 bernilai 0
Posisi (1,1)	=  60	= 00111100  0, karena bit ke-6 bernilai 0
Posisi (1,2)	=  70	= 01000110  255, karena bit ke-6 bernilai 1
Posisi (2,0)	=  60	= 00111100  0, karena bit ke-6 bernilai 0
Posisi (2,1)	=  70	= 01000110  255, karena bit ke-6 bernilai 1
Posisi (2,2)	=  80	= 01010000  255, karena bit ke-6 bernilai 1

Matriks Citra Hasil:

![](Picture3.jpg)

<!-- Slide number: 38 -->

Histogram Citra Hasil:

![](Picture2.jpg)

<!-- Slide number: 39 -->
# RANGE COMPRESSION
Metode untuk memampatkan rentangan dinamis piksel suatu citra
Disebut juga dengan Metode Transformasi Logaritmik
Notasi:

Dengan o dan u menyatakan nilai piksel setelah dan sebelum diproses, c merupakan faktor penskalaan

![](Picture1.jpg)

<!-- Slide number: 40 -->

Contoh Kasus:
	Pada citra grayscale sebelumnya, akan dilakukan proses range compression, dengan nilai c = 10

Posisi (0,0)	=  10 * log10  (1 + |55|) = 17
Posisi (0,1)	=  10 * log10  (1 + |45|) = 17
Posisi (0,2)	=  10 * log10  (1 + |80|) = 19
Posisi (1,0)	=  10 * log10  (1 + |50|) = 17
Posisi (1,1)	=  10 * log10  (1 + |60|) = 18
Posisi (1,2)	=  10 * log10  (1 + |70|) = 19
Posisi (2,0)	=  10 * log10  (1 + |60|) = 18
Posisi (2,1)	=  10 * log10  (1 + |70|) = 19
Posisi (2,2)	=  10 * log10  (1 + |80|) = 19

Matriks Citra Hasil:

![](Picture2.jpg)

<!-- Slide number: 41 -->

Histogram Citra Hasil:

![](Picture2.jpg)

<!-- Slide number: 42 -->

# HISTOGRAM EQUALIZATION
Metode untuk melakukan distribusi ulang terhadap distribusi intensitas dari histogram awal
Distribusi awal terhadap histogram awal dilakukan dengan memetakan setiap nilai piksel pada histogram awal menjadi nilai piksel baru
Notasi:

n(g) adalah nilai piksel baru, N adalah banyaknya piksel pada citra, g adalah nilai gray level awal yang nilainya dari 1..L, L adalah nilai gray level maksimum, c(g) adalah banyaknya piksel yang memiliki nilai sama dengan g atau kurang, h(g) adalah histogram awal

![](Picture1.jpg)

<!-- Slide number: 43 -->

Pada matriks grayscale:

Diperoleh:

![](Picture4.jpg)

![](Picture1.jpg)

![](Picture7.jpg)

<!-- Slide number: 44 -->

Dilakukan proses ekualisasi histogram:

Perhitungan cg dan ng, untuk g = 45 dan hg = 1
		cg	= cg + hg
			= 0 + 1 = 1
		ng 	= max(0, round[(255)*(1/9)] )
			= max(0,28) = 28
Perhitungan cg dan ng, untuk g = 50 dan hg = 1
		cg	= cg + hg
			= 1 + 1 = 2
		ng 	= max(0, round[(255)*(2/9)] )
			= max(0,56) = 56
Perhitungan cg, untuk g = 55 dan hg = 1
		cg	= cg + hg
			= 2 + 1 = 3
		ng 	= max(0, round[(255)*(3/9)] )
			= max(0,85) = 85

<!-- Slide number: 45 -->

Perhitungan cg dan ng, untuk g = 60 dan hg = 2
		cg	= cg + hg
			= 3 + 2 = 5
		ng 	= max(0, round[(255)*(5/9)] )
			= max(0,141) = 141
Perhitungan cg dan ng, untuk g = 70 dan hg = 2
		cg	= cg + hg
			= 5 + 2 = 7
		ng 	= max(0, round[(255)*(7/9)] )
			= max(0,198) = 198
Perhitungan cg, untuk g = 80 dan hg = 2
		cg	= cg + hg
			= 7 + 2 = 9
		ng 	= max(0, round[(255)*(9/9)] )
			= max(0,255) = 255

<!-- Slide number: 46 -->

Histogram Citra Hasil:

![](Picture3.jpg)
| g | hg | cg | ng |
| --- | --- | --- | --- |
| 45 | 1 | 1 | 28 |
| 50 | 1 | 2 | 56 |
| 55 | 1 | 3 | 85 |
| 60 | 2 | 5 | 141 |
| 70 | 2 | 7 | 198 |
| 80 | 2 | 9 | 255 |

<!-- Slide number: 47 -->

Pada matriks grayscale:

Diperoleh:

![](Picture4.jpg)

![](Picture1.jpg)

![](Picture7.jpg)

<!-- Slide number: 48 -->

Dilakukan proses ekualisasi histogram:

Perhitungan cg dan ng, untuk g = 45 dan hg = 1
		cg	= cg + hg
			= 0 + 1 = 1
		ng 	= max(0, round[(255)* (1/9)] – 1)
			= max(0,27) = 27
Perhitungan cg dan ng, untuk g = 50 dan hg = 1
		cg	= cg + hg
			= 1 + 1 = 2
		ng 	= max(0, round[(255) *(2/9)] – 1)
			= max(0,55) = 55
Perhitungan cg, untuk g = 55 dan hg = 1
		cg	= cg + hg
			= 2 + 1 = 3
		ng 	= max(0, round[(255) *(3/9)] – 1)
			= max(0,84) = 84

<!-- Slide number: 49 -->

Perhitungan cg dan ng, untuk g = 60 dan hg = 2
		cg	= cg + hg
			= 3 + 2 = 5
		ng 	= max(0, round[(255) *(5/9)])
			= max(0,140) = 140
Perhitungan cg dan ng, untuk g = 70 dan hg = 2
		cg	= cg + hg
			= 5 + 2 = 7
		ng 	= max(0, round[(255) *(7/9)])
			= max(0,197) = 197
Perhitungan cg, untuk g = 80 dan hg = 2
		cg	= cg + hg
			= 7 + 2 = 9
		ng 	= max(0, round[(255) *(9/9)])
			= max(0,255) = 255

<!-- Slide number: 50 -->

Histogram Citra Hasil:

![](Picture3.jpg)
| g | hg | cg | ng |
| --- | --- | --- | --- |
| 45 | 1 | 1 | 28 |
| 50 | 1 | 2 | 56 |
| 55 | 1 | 3 | 85 |
| 60 | 2 | 5 | 141 |
| 70 | 2 | 7 | 198 |
| 80 | 2 | 9 | 255 |

<!-- Slide number: 51 -->
# IMAGE SUBSTRACTION
Perbedaan dua citra u1(x,y) dan u2(x,y) dapat dinyatakan:

Contoh Kasus:
	Diberikan dua buah matriks citra input A dan B.

![](Picture1.jpg)

![](Picture1.jpg)

![](Picture2.jpg)

<!-- Slide number: 52 -->
Dilakukan proses image substraction terhadap kedua citra
Posisi (0,0)	= 101 – 219 	= -118	 0
Posisi (0,1) 	= 73 – 253 	= -180	 0
Posisi (0,2)	= 146 – 35	= 111
Posisi (1,0)	= 45 – 182	= -137	 0
Posisi (1,1)	= 162 – 148	= 14
Posisi (1,2)	= 182 – 157	= 25
Posisi (2,0)	= 234 – 122	= 112
Posisi (2,1)	= 160 – 238	= -78	 0
Posisi (2,2)	= 79 – 66		= 13

Matriks Citra Hasil:

![](Picture4.jpg)

<!-- Slide number: 53 -->
# IMAGE AVERAGING
Rata-rata dari M buah citra dapat dinyatakan:

Contoh Kasus:
	Diberikan dua buah matriks citra input A dan B.

![](Picture1.jpg)

![](Picture1.jpg)

![](Picture2.jpg)

<!-- Slide number: 54 -->
Dilakukan proses image averaging terhadap kedua citra
Posisi (0,0)	= (101 + 219)/2 	= 160
Posisi (0,1) 	= (73 + 253)/2 	= 163
Posisi (0,2)	= (146 + 35)/2	= 91
Posisi (1,0)	= (45 + 182)/2	= 114
Posisi (1,1)	= (162 + 148)/2	= 155
Posisi (1,2)	= (182 + 157)/2	= 170
Posisi (2,0)	= (234 + 122)/2	= 178
Posisi (2,1)	= (160 + 238)/2	= 199
Posisi (2,2)	= (79 + 66)/2	= 73

Matriks Citra Hasil:

![](Picture2.jpg)
Terima Kasih