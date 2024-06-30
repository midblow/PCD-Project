<a name="readme-top"></a>

# HASIL ANALISIS TUGAS BESAR PENGOLAHAN CITRA DIGITAL

## Kelompok 20

### Muhamad Erwin Hariadinata (F1D022065)

### Muhammad Nune Huria Sakti (F1D022075)

### Nadya Azzahra (F1D022083)

### Safira Dwi Rizqia (F1D022096)

### Muhammad akbar setiadi (F1D022140)

# DetectSea: Deteksi Objek Laut dengan Metode CNN

## Latar Belakang

Lautan menutupi lebih dari 70% permukaan bumi dan menjadi rumah bagi berbagai flora dan fauna yang penting untuk ekosistem global. Hewan laut seperti ikan, mamalia laut, dan invertebrata membentuk keseimbangan ekosistem laut dan membantu berbagai aspek kehidupan manusia, seperti perikanan, pariwisata, dan penelitian ilmiah. Namun, karena kondisi lingkungan yang dinamis dan sulit dijangkau, eksplorasi dan pemantauan hewan laut sering kali menghadapi tantangan besar.

Convolutional Neural Networks (CNN) adalah salah satu metode deep learning yang paling populer dan efektif untuk analisis data visual, seperti gambar dan video. CNN dirancang untuk mengenali pola dan fitur dalam data visual melalui proses yang meniru cara kerja otak manusia dalam memproses informasi visual. Metode ini terdiri dari beberapa lapisan, termasuk lapisan konvolusi, lapisan pooling, dan lapisan fully connected, yang bekerja secara bersama-sama untuk melakukan ekstraksi fitur dan klasifikasi.

Pemilihan topik ini didasarkan oleh kebutuhan untuk mengembangkan metode yang lebih efisien dan akurat dalam mendeteksi dan memantau hewan-hewan laut. Program `detectSea` bertujuan untuk mendeteksi dan mengklasifikasikan berbagai spesies hewan laut dari citra dengan menerapkan CNN. Dengan menggunakan CNN, program ini dapat memproses data visual dengan cepat dan akurat, memungkinkan para peneliti dan konservasionis untuk melakukan pemantauan yang lebih efektif.

## Identifikasi Masalah

Lautan merupakan habitat vital bagi berbagai spesies flora dan fauna yang mendukung keberlangsungan ekosistem global serta berbagai sektor penting manusia seperti perikanan, pariwisata, dan penelitian ilmiah. Namun, tantangan besar yang dihadapi adalah sulitnya eksplorasi dan pemantauan hewan laut akibat kondisi lingkungan yang kompleks dan sulit dijangkau. Hal ini mengakibatkan keterbatasan dalam memperoleh data yang akurat dan konsisten mengenai populasi dan perilaku hewan laut. Convolutional Neural Networks (CNN), yang terkenal efektif dalam menganalisis data visual seperti gambar dan video, menjanjikan solusi untuk meningkatkan efisiensi dan ketepatan dalam mendeteksi serta memantau hewan laut. Melalui implementasi CNN dalam program `detectSea`, diharapkan dapat ditingkatkan kemampuan untuk mengenali spesies hewan laut dari citra dengan tingkat keakuratan yang tinggi. Namun, untuk mencapai hal ini, diperlukan penyelesaian masalah terkait dengan ketersediaan data yang berkualitas, validasi model yang konsisten dalam berbagai kondisi lingkungan laut yang berubah-ubah, serta integrasi teknologi ini ke dalam strategi konservasi laut yang berkelanjutan. Dengan mengatasi tantangan-tantangan ini, program `detectSea` diharapkan dapat memberikan kontribusi penting dalam pemahaman dan perlindungan terhadap keanekaragaman hayati di laut.

## Tujuan

Adapun tujuan dari pembuatan detectSea adalah sebagai berikut:

1. **Meningkatkan Efisiensi Pemantauan**: Mengimplementasikan Convolutional Neural Networks (CNN) dalam program `detectSea` untuk meningkatkan efisiensi dalam mendeteksi dan memantau berbagai spesies hewan laut dari gambar atau video, sehingga memungkinkan pengumpulan data yang lebih cepat dan akurat tentang populasi dan perilaku hewan laut.

2. **Mengatasi Tantangan Lingkungan**: Menyediakan solusi teknologi yang dapat menangani tantangan lingkungan yang dinamis dan sulit dijangkau di lautan, sehingga meningkatkan konsistensi dan validitas data yang diperoleh dari pemantauan hewan laut.

3. **Mendukung Konservasi dan Perlindungan**: Memperkuat upaya konservasi laut dengan menyediakan alat yang lebih efektif untuk identifikasi dan pengawasan terhadap keberagaman hayati laut, sehingga mendukung keberlanjutan ekosistem laut dan manfaat ekonomi yang bergantung padanya seperti perikanan dan pariwisata.

## DetectSea Berdasarkan Jenis Objek yang Berbeda

### Data Understanding

Pada Project detectSea ini digunakan kumpulan data (dataset) berupa gambar dari beberapa spesies laut, diantaranya coral, kepiting, ikan, ubur-ubur, serta bintang laut yang diambil dari situs kaggle dengan link https://www.kaggle.com/datasets/vencerlanz09/sea-animals-image-dataste jumlah rincian dari label yang digunakan adalah sebagai berikut:

<img src="ImageSource/display_object.png">

*Gambar 2.1 Tampilan Objek*

- **Corals** dengan jumlah 200 gambar 
- **Crabs** dengan jumlah 250 gambar 
- **Fish** dengan jumlah 200 gambar 
- **Jellyfish** dengan jumlah 300 gambar 
- **Starfish** dengan jumlah 200 gambar

## Analisis Percobaan

### **Percobaan 0**:

Pada percobaan 0 ini tidak dilakukan proses preprocessing sama sekali dikarenakan tujuannya adalah untuk mengetahui tingkat akurasi yang akan didapatkan tanpa proses prerpocessing terlebih dahulu.

#### Data Preparation

Pada bagian ini dilakukan proses resize pada function `Preprocess_images` terhadap seluruh gambar dengan ukuran 300x300

<img src="ImageSource/Data Distribution.png">

*Gambar 2.2 Distribusi Data*

Setelah itu dilakukan proses augmentasi dengan masing-masing gambar di-augmentasi sebanyak dua proses yakni proses rotasi sejauh 90 derajat dan sejauh -90 derajat.

<img src="ImageSource/After Augmentation.png">

*Gambar 2.3 Distribusi Data Setelah Augmentasi*

#### Modeling & Evaluation

Didapatkan hasil evaluasi menggunakan berbagai model terhadap data pelatihan dan pengujian yang mana tiga model tersebut yaitu KNN, SVM, dan Random Forest.

**Tabel 2.1 Hasil Evaluasi Menggunakan GLCM Pada 3 Metode Berbeda**

| Model | Accuracy | Precision | Recall | F1 Score |
|-------|----------|-----------|--------|----------|
| KNN   | 0.671014 | 0.673427  | 0.671014 | 0.670043 |
| SVM   | 0.544928 | 0.538977  | 0.544928 | 0.539096 |
| RF    | 0.755072 | 0.756856  | 0.755072 | 0.753014 |

Setelah itu, hasil evaluasi tersebut juga ditampilkan pada confusion matrix. Confusion matrix ini menggambarkan seberapa baik model dapat mengklasifikasikan data dengan memperlihatkan persentase prediksi yang benar dari setiap kelas, serta kesalahan prediksi antara kelas-kelas yang berbeda.

<img src="ImageSource/Conf_Matrix_2.0.png">

*Gambar 2.4 Confusion Matrix Tanpa Preprocessing*

Selanjutnya dilakukan modeling dengan menggunakan model CNN dengan hasil evaluasi sebagai berikut:

**Tabel 2.2 Hasil Evaluasi Dengan Metode CNN**

| Class            | Precision | Recall | F1-Score               | Support |
| ---------------- | --------- | ------ | ---------------------- | ------- |
| 0                | 0.78      | 0.86   | 0.82                   | 145     |
| 1                | 0.87      | 0.83   | 0.85                   | 140     |
| 2                | 0.89      | 0.86   | 0.87                   | 120     |
| 3                | 0.92      | 0.91   | 0.92                   | 172     |
| 4                | 0.72      | 0.72   | 0.72                   | 113     |
| **Accuracy**     |           |        | **0.8420289754867554** | 690     |
| **Macro Avg**    | 0.84      | 0.83   | 0.84                   | 690     |
| **Weighted Avg** | 0.84      | 0.84   | 0.84                   | 690     |

Kemudian, ditampilkan juga confusion matrix khusus untuk model CNN ini yang menampilkan jumlah absolut prediksi yang tepat dan kesalahan prediksi untuk setiap kelas target.

<img src="ImageSource/Conf_Matrix_2.0.2.png">

*Gambar 2.5 Confusion Matrix Tanpa Preprocessing dengan CNN*

Setalh itu, ditampilkan juga hasil kurva accuracy dan kurva loss yang didapatkan berdasarkan data dari proses CNN tersebut:

<img src="ImageSource/Model Fit_2.0.png">

*Gambar 2.6 Model Fitting Percobaan 0*

### **Percobaan 1**:

Pada percobaan 1 ini dilakukan berbagai proses preprocessing dengan tujuan untuk mengetahui tingkat akurasi yang akan didapatkan. Tahapan dari proses preprocessing tersebut adalah sebagai berikut:
Grayscale > Threshold > Edge Detection > Find Countur

#### Data Preparation

Untuk persiapan data sebelum dilakukan proses preprocessing, dilakukan persiapan data sama seperti `Percobaan 0` sebelumnya.

#### Modeling & Evaluation

Didapatkan hasil evaluasi menggunakan berbagai model terhadap data pelatihan dan pengujian yang mana tiga model tersebut yaitu KNN, SVM, dan Random Forest.

**Tabel 2.3 Hasil Evaluasi Menggunakan GLCM Pada 3 Metode Berbeda dengan Preprocessing**

| Model | Accuracy | Precision | Recall | F1 Score |
|-------|----------|-----------|--------|----------|
| KNN   | 0.544928 | 0.538967  | 0.544928 | 0.53929  |
| SVM   | 0.527536 | 0.516103  | 0.527536 | 0.510629 |
| RF    | 0.691304 | 0.687119  | 0.691304 | 0.686287 |

Selanjutnya dilakukan modeling dengan menggunakan model CNN dengan hasil evaluasi sebagai berikut:

**Tabel 2.4 Hasil Evaluasi Dengan Metode CNN**

| Class            | Precision | Recall | F1-Score               | Support |
| ---------------- | --------- | ------ | ---------------------- | ------- |
| 0                | 0.46      | 0.39   | 0.42                   | 145     |
| 1                | 0.55      | 0.65   | 0.59                   | 140     |
| 2                | 0.65      | 0.41   | 0.50                   | 120     |
| 3                | 0.65      | 0.76   | 0.70                   | 172     |
| 4                | 0.44      | 0.50   | 0.47                   | 113     |
| **Accuracy**     |           |        | **0.5536231994628906** | 690     |
| **Macro Avg**    | 0.55      | 0.54   | 0.54                   | 690     |
| **Weighted Avg** | 0.56      | 0.55   | 0.55                   | 690     |

Kemudian, ditampilkan juga confusion matrix khusus untuk model CNN ini yang menampilkan jumlah absolut prediksi yang tepat dan kesalahan prediksi untuk setiap kelas target.

<img src="ImageSource/Conf_Matrix_2.1.2.png">

*Gambar 2.7 Confusion Matrix dengan Preprocessing Pada CNN*

Setalh itu, ditampilkan juga hasil kurva accuracy dan kurva loss yang didapatkan berdasarkan data dari proses CNN tersebut:

<img src="ImageSource/Model Fit_2.1.png">

*Gambar 2.8 Model Fitting Percobaan 1*


- Percobaan 0 menghasilkan akurasi lebih rendah dibandingkan dengan percobaan lain karena penggunaan metode GLCM dalam preprocessing tidak memberikan keuntungan signifikan bagi model CNN.

- Percobaan 1 menunjukkan bahwa terlalu banyak tahapan preprocessing dapat menurunkan performa model dan menghasilkan akurasi terendah untuk semua model yang diuji, terutama pada CNN.

- Percobaan 2 dan percobaan 4 menunjukkan bahwa preprocessing sederhana seperti resize dan konversi ke grayscale bisa memberikan akurasi yang tinggi dan stabil. Ini berarti tahapan dasar ini sudah cukup efektif untuk mempersiapkan data bagi CNN.

- Percobaan 5 dan percobaan 7 menunjukkan bahwa tambahan histogram equalization atau median blur tidak memberikan peningkatan yang signifikan dibandingkan dengan Percobaan 4, dengan akurasi yang tetap stabil.

- Percobaan 6 menunjukkan bahwa penggunaan gaussian blur memberikan akurasi tertinggi, sedikit lebih tinggi dibandingkan dengan Percobaan 4 dan 5. Ini berarti gaussian blur bisa membantu meningkatkan fokus pada fitur yang relevan dan memberikan hasil yang lebih baik.


