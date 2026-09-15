<!-- Slide number: 1 -->
# Operasi aritmatika citra

<!-- Slide number: 2 -->
# Operasi aritmatika #1
Citra digital merupakan suatu matriks dimana indeks baris dan kolomnya menyatakan suatu titik pada citra tersebut dan elemen matriksnya menyatakan tingkat keabuan pada titik tersebut.

Sebuah citra digital dapat direpresentasikan dalam bentuk matriks yang terdiri dari M kolom dan N baris, di mana perpotongan antara kolom dan baris disebut piksel.

Piksel merupakan elemen terkecil dari suatu citra, yakni berupa titik-titik warna yang membentuk citra.
ditulis dalam bentuk matriks berikut:

![](Picture3.jpg)

<!-- Slide number: 3 -->
# Operasi aritmatika #2
Operasi arimatika citra (Image arithmatic) merupakan proses pengolahan citra dengan memanfaatkan operator aritmatika atau operator logika terhadap dua atau lebih citra input

Operasi aritmatika berlaku untuk multivalued  piksel.
Operasi aritmatika mencakup
penambahan & pengurangan -> kecerahan
perkalian & pembagian -> kontras nilai pixel dengan suatu nilai tetapan

operasi logika hanya berlaku untuk gambar biner.

Operasi logika digunakan untuk tugas-tugas seperti masking, deteksi fitur, dan analisa bentuk.

<!-- Slide number: 4 -->
# Operasi aritmatika #3
2 buah citra
		C(x, y) = A(x, y) op B(x, y)

		A, B = citra input
		C = citra output
		 op = operator yang akan diterapkan

N buah citra
		C(x, y) = A1(x, y) op A2(x, y) op A3(x, y) … op AN(x, y)

		A1,…, AN = citra input
		C = citra output
		 op = operator yang akan diterapkan

<!-- Slide number: 5 -->
# Operasi aritmatika #4
Penjumlahan
Pengurangan
Perkalian
Pembagian
Pencampuran
Logika AND/NAND
Logika OR/NOR
Logika XOR/XNOR
Invert/logika NOT
Bitshift Operators

<!-- Slide number: 6 -->
# 1. penjumlahan
Pixel citra hasil merupakan hasil penjumlahan nilai pixel pada citra pertama dengan nilai pixel citra kedua.

Image blending adalah operasi penggabungan 2  citra. Operasi ini menggunakan operasi aritmatika penambahan

Penjumlahan membuat citra lebih cerah

Proses penjumlahan dilakukan dengan cara:
		 o(x,y) = u1(x,y) + u2(x,y)

Penjumlahan dengan konstanta yaitu:
		o(x,y) = u(x,y) + K

<!-- Slide number: 7 -->
# Penjumlahan #2

 Penjumlahan 2 buah matrik atau lebih dapat dilakukan bila masing-masing matrik berordo  sama.tugas4.xlsx

 Penjumlahan matrik dengan konstanta dengan menjumlahkan setia unsur matrik dengan konstanta tersebut. tugas4.xlsx

![](Picture3.jpg)

<!-- Slide number: 8 -->
# Penjumlahan #3

![](Picture4.jpg)

![](Picture5.jpg)

![](Picture6.jpg)

<!-- Slide number: 9 -->
# 2. Pengurangan #1
Operasi pengurangan hampir sama dengan penjumlahan, hanya saja untuk mendapatkan citra hasil nilai pixel input pertama dikurangi dengan nilai pixel input lainnya.

Deteksi gerak adalah operasi pengurangan 2  citra untuk mendeteksi adanya perubahan citra 1 ke citra 2.

Dengan mengevaluasi nilai selisih tersebut, dapat diketahui apakah pada citra terdapat objek yang bergerak

Mencari beda antara 2 buah citra yang berurutan pada hasil pencitraan menggunakan kamera video digital
	• operator pengurangan
	• bagian tidak bergerak : nilai nol
	• bagian yang bergerak : nilai tidak nol

<!-- Slide number: 10 -->
# Pengurangan #2
Sama halnya dengan penjumlahan di atas, maka pengurangan 2 buah matrik hanya dapat dilakukan pada matrik yang berordo sama

Pengurangan matrik dengan konstanta yaitu dengan mengurangi seiap unsur matrik dengan niai konstanta tersebut

Operasi aritmatika pengurangan:
		o(x,y) = u1(x,y) - u2(x,y)

 Proses pengurangan dengan konstanta :
		o(x,y) = u(x,y) - K

<!-- Slide number: 11 -->
# Pengurangan #3

Contoh pengurangan matriktugas4.xlsx

![](Picture2.jpg)

<!-- Slide number: 12 -->
# Pengurangan #4

![](Picture3.jpg)

![](Picture4.jpg)

![](Picture2.jpg)
Citra hasil pengurangan citra dengan konstanta 100

<!-- Slide number: 13 -->
# Contoh Deteksi Gerakan

![](Picture3.jpg)

![](Picture4.jpg)

![](Picture2.jpg)
A
B
citra hasil mendeteksi gerakan :
objek paku hitam menunjukkan posisi objek      mengalami perpindahan
objek paku putih menunjukkan posisi akhir dari objek tersebut

<!-- Slide number: 14 -->
# 3. perkalian
Operasi perkalian dengan sebuah citra menghilangkan bagian tertentu dari citra dan menampakkan hanya objek yang diinginkan.

Proses perkalian citra mengakibatkan adanya peningkatan nilai citra

Hasil dari perkalian citra dipengaruhi oleh besarnya nilai konstanta

Apabila nilai konstanta lebih besar dari 1 maka akan terjadi peningkatan nilai citra.

Apabila nilai konstanta negatif maka akan terjadi penurunan nilai intensitas.

<!-- Slide number: 15 -->
# Perkalian #2
Perkalian matrik dengan konstanta yaitu dengan mengalikan setiap unsur matrik dengan nilai konstanta.

Perkalian antara 2 buah citra dapat dilakukan dengan persamaan:
		o(x,y) = u1(x,y) * u2(x,y)

Perkalian citra dengan konstanta :
		o(x,y) = u(x,y) * K

<!-- Slide number: 16 -->
# Perkalian #3

![](Picture2.jpg)

<!-- Slide number: 17 -->
# Perkalian #4

![](Picture2.jpg)

<!-- Slide number: 18 -->
# Perkalian #4

![](Picture2.jpg)
Perkalian citra dengan konstanta

<!-- Slide number: 19 -->
# 4. pembagian
Operasi pembagian menghasilkan citra rasio perbedaan antara kedua input citra.

Hasil pembagian antara 2 citra memperlihatkan perbedaan letak antar kedua citra tersebut.

Hasil pembagian antara 2 citra dapat digambarkan dengan persamaan sebagai berikut:
		o(x,y) = u1(x,y) / u2(x,y)

Hasil pembagian citra dengan konstanta:
		o(x,y) = u(x,y) / Ktugas4.xlsx

<!-- Slide number: 20 -->
# Pembagian #2

![](Picture2.jpg)

menunjukkan hasil pembagian 2 citra yang hampir mirip tetapi memiliki perbedaan letak.

![](Picture3.jpg)
(a) dan (b) Citra input, (c) Citra hasil pembagian

<!-- Slide number: 21 -->
# 5. pencampuran
Proses pencampuran citra sama dengan proses penjumlahan 2 citra, tetapi menggunakan parameter.

Parameter penjumlahan menentukan citra mana yang lebih dominan.

Setiap pixel dari citra hasil dihitung dengan persamaan sebagai berikut:

		o(x,y) =(p* u1(x,y)) + ((1-p)*u2(x,y))

		   p        = parameter  (0 – 1)tugas4.xlsx

<!-- Slide number: 22 -->
# Pencampuran #2

![](Picture2.jpg)

![](Picture4.jpg)
(a) dan (b) Citra input, (c) Citra output dengan rasio perbandingan citra (a) : (b) = 4 : 1

<!-- Slide number: 23 -->
# 6. Logika and/nand
Perubahan warna yang dihasilkan dari operasi logika AND dan NAND mengikuti tabel kebenaran yang bersangkutan.

Tabel kebenaran operator NAND menghasilkan nilai yang berkebalikan dengan nilai operator AND.

Tabel kebenaran operator AND menghasilkan nilai true, jika kedua nilai input adalah true, selain itu nilai keluarannya adalah false.tugas4.xlsx

Tabel kebenaran operator NAND menghasilkan nilai false, jika kedua nilai input adalah true, selain itu nilai keluarannya adalah true.

<!-- Slide number: 24 -->
# Logika and/nand #2
Tabel 1. Tabel kebenaran operator AND

Tabel 2. Tabel kebenaran operator NAND

![](Picture3.jpg)

![](Picture4.jpg)

<!-- Slide number: 25 -->
# Logika and/nand #3
Masking (AND) operation dapat digunakan untuk memisahkan antara bagian obyek dan bagian latar belakang pada citra biomedik.

<!-- Slide number: 26 -->
# Contoh  logika AND

![](Picture2.jpg)

![](Picture3.jpg)

jaringan paru

Mask dengan operasi AND

<!-- Slide number: 27 -->
# 7. Logika or/nor
Operator OR menghasilkan nilai false  jika kedua inputnya false, selain itu hasilnya adalah true.tugas4.xlsx
Operator NOR menghasilkan nilai true  jika kedua inputnya false, selain itu hasilnya adalah false.
Tabel 3. Tabel kebenaran operator OR

Tabel 4. Tabel kebenaran operator NOR

![](Picture3.jpg)

![](Picture4.jpg)

<!-- Slide number: 28 -->
# 8. Logika xor/xnor
Operator XOR menghasilkan nilai true  jika salah satu dari input bernilai true.
Operator XOR menghasilhan nilai false  jika kedua input bernilai true.
Operator NXOR adalah kebalikan dari operator XOR.tugas4.xlsx
Tabel 5. Tabel kebenaran operator XOR

Tabel 6. Tabel kebenaran operator XNOR

![](Picture3.jpg)

![](Picture4.jpg)

<!-- Slide number: 29 -->
# 9. Logika not/invert
Invert atau logika NOT pada citra memberikan hasil keluaran berupa kebalikan dari citra input.

Pada citra biner, apabila citra input bernilai 1 maka keluarannya akan bernilai 0, demikian sebaliknya.tugas4.xlsx

<!-- Slide number: 30 -->
# Citra hasil operasi logika #1

![](Picture4.jpg)

![](Picture2.jpg)

![](Picture3.jpg)

![](Picture5.jpg)
A AND B
A OR B
Citra A
Citra B

![](Picture7.jpg)

![](Picture6.jpg)
A XOR B
NOT A

<!-- Slide number: 31 -->
# Citra hasil operasi logika #2

![](Picture2.jpg)

![](Picture4.jpg)

<!-- Slide number: 32 -->
# 10. Bitshift operators
Proses bitshift melakukan pergeseran deret bit pada pixel ke arah kanan atau kiri sebesar 1 bit.

Secara matematika dapat dimodelkan seperti berikut:
		bitshift – right (n)  o(x,y) ÷ 2n
	bitshift – left (n)   o(x,y) x 2n

Contoh:
Citra input  =  00000111 = 7
	00000111 digeser ke kiri sebanyak 2 bit    => 7 x 22   =  28 => 00011100
00011100 digeser ke kanan sebanyak 1 bit => 28 / 21 =  14 => 00001110

<!-- Slide number: 33 -->
# Bitshift operators #2

![](ContentPlaceholder3.jpg)
(a) Citra input, (b) Citra output bitshift ke kanan sebesar 1 bit, (c) Citra output bitshift ke kiri sebesar 2 bit

<!-- Slide number: 34 -->
# Terima kasih