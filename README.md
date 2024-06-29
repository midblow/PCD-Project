<a name="readme-top"></a> 

# HASIL ANALISIS TUGAS BESAR PENGOLAHAN CITRA DIGITAL  

 

## Kelompok 20 

### Muhamad Erwin Hariadinata (F1D022065) 

### Muhammad Nune Huria Sakti (F1D022075) 

### Nadya Azzahra (F1D022083) 

### Safira Dwi Rizqia (F1D022096) 

### Muhammad akbar setiadi (F1D022140) 

 

# Judul _Project_  

## "DetectSea: Deteksi Objek Laut dengan Metode CNN" 

 

 

## Latar Belakang 

Lautan menutupi lebih dari 70% permukaan bumi dan menjadi rumah bagi berbagai flora dan fauna yang penting untuk ekosistem global. Hewan laut seperti ikan, mamalia laut, dan invertebrata membentuk keseimbangan ekosistem laut dan membantu berbagai aspek kehidupan manusia, seperti perikanan, pariwisata, dan penelitian ilmiah. Namun, karena kondisi lingkungan yang dinamis dan sulit dijangkau, eksplorasi dan pemantauan hewan laut sering kali menghadapi tantangan besar. 

 

Convolutional Neural Networks (CNN) adalah salah satu metode deep learning yang paling populer dan efektif untuk analisis data visual, seperti gambar dan video. CNN dirancang untuk mengenali pola dan fitur dalam data visual melalui proses yang meniru cara kerja otak manusia dalam memproses informasi visual. Metode ini terdiri dari beberapa lapisan, termasuk lapisan konvolusi, lapisan pooling, dan lapisan fully connected, yang bekerja secara bersama-sama untuk melakukan ekstraksi fitur dan klasifikasi. 

 

Pemilihan topik ini didasarkan oleh kebutuhan untuk mengembangkan metode yang lebih efisien dan akurat dalam mendeteksi dan memantau hewan-hewan laut. Program "detectSea" bertujuan untuk mendeteksi dan mengklasifikasikan berbagai spesies hewan laut dari citra dengan menerapkan CNN. Dengan menggunakan CNN, program ini dapat memproses data visual dengan cepat dan akurat, memungkinkan para peneliti dan konservasionis untuk melakukan pemantauan yang lebih efektif. 

 

## Identifikasi Masalah 

Lautan merupakan habitat vital bagi berbagai spesies flora dan fauna yang mendukung keberlangsungan ekosistem global serta berbagai sektor penting manusia seperti perikanan, pariwisata, dan penelitian ilmiah. Namun, tantangan besar yang dihadapi adalah sulitnya eksplorasi dan pemantauan hewan laut akibat kondisi lingkungan yang kompleks dan sulit dijangkau. Hal ini mengakibatkan keterbatasan dalam memperoleh data yang akurat dan konsisten mengenai populasi dan perilaku hewan laut. Convolutional Neural Networks (CNN), yang terkenal efektif dalam menganalisis data visual seperti gambar dan video, menjanjikan solusi untuk meningkatkan efisiensi dan ketepatan dalam mendeteksi serta memantau hewan laut. Melalui implementasi CNN dalam program "detectSea", diharapkan dapat ditingkatkan kemampuan untuk mengenali spesies hewan laut dari citra dengan tingkat keakuratan yang tinggi. Namun, untuk mencapai hal ini, diperlukan penyelesaian masalah terkait dengan ketersediaan data yang berkualitas, validasi model yang konsisten dalam berbagai kondisi lingkungan laut yang berubah-ubah, serta integrasi teknologi ini ke dalam strategi konservasi laut yang berkelanjutan. Dengan mengatasi tantangan-tantangan ini, program "detectSea" diharapkan dapat memberikan kontribusi penting dalam pemahaman dan perlindungan terhadap keanekaragaman hayati di laut. 

 

## Tujuan 

Adapun tujuan dari pembuatan detectSea adalah sebagai berikut: 

 

1. Meningkatkan Efisiensi Pemantauan: Mengimplementasikan Convolutional Neural Networks (CNN) dalam program "detectSea" untuk    meningkatkan efisiensi dalam mendeteksi dan memantau berbagai spesies hewan laut dari gambar atau video, sehingga memungkinkan pengumpulan data yang lebih cepat dan akurat tentang populasi dan perilaku hewan laut. 

 

2. Mengatasi Tantangan Lingkungan: Menyediakan solusi teknologi yang dapat menangani tantangan lingkungan yang dinamis dan sulit dijangkau di lautan, sehingga meningkatkan konsistensi dan validitas data yang diperoleh dari pemantauan hewan laut. 

 

3. Mendukung Konservasi dan Perlindungan: Memperkuat upaya konservasi laut dengan menyediakan alat yang lebih efektif untuk identifikasi dan pengawasan terhadap keberagaman hayati laut, sehingga mendukung keberlanjutan ekosistem laut dan manfaat ekonomi yang bergantung padanya seperti perikanan dan pariwisata. 

 

## DetectSea Berdasarkan Jenis Objek yang Berbeda 

### Data Understanding 
Pada Project detectSea ini digunakan kumpulan data (dataset) berupa gambar dari beberapa spesies laut, diantaranya coral, kepiting, ikan, ubur-ubur, serta bintang laut yang diambil dari situs kaggle dengan link https://www.kaggle.com/datasets/vencerlanz09/sea-animals-image-dataste jumlah rincian dari label yang digunakan adalah sebagai berikut: 
<li>Corals dengan jumlah 200 gambar 
<li>Crabs dengan jumlah 250 gambar 
<li>Fish dengan jumlah 200 gambar 
<li>Jellyfish dengan jumlah 300 gambar 
<li>Starfish dengan jumlah 200 gambar 

 
## Analisis Percobaan 

Percobaan 0: 

Preprocessing yang dilakukan adalah resize dengan menggunakan metode GLCM dan CNN.  

Accuracy KNN = 0.67 

Accuracy SVM = 0.54 

Accuracy RF = 0.75 

Accuracy CNN = 0.84 

Percobaan 1: 

Preprocessing yang dilakukan adalah resize, convert to gray, threshold, edge detection, dan contour detection dengan menggunakan metode GLCM dan CNN.  

Accuracy KNN = 0.54 

Accuracy SVM = 0.52 

Accuracy RF = 0.69 

Accuracy CNN = 0.55 

Percobaan 2: 

Preprocessing yang dilakukan adalah resize, convert to gray, dan threshold dengan menggunakan metode CNN.  

Accuracy CNN = 0.84 

Percobaan 3: 

Preprocessing yang dilakukan adalah resize, convert to gray, dan histogram equalization dengan menggunakan metode CNN.  

Accuracy CNN = 0.74 

Percobaan 4: 

Preprocessing yang dilakukan adalah resize dan convert to gray dengan menggunakan metode CNN.  

Accuracy CNN = 0.89 

Percobaan 5: 

Preprocessing yang dilakukan adalah resize, histogram equalization, dan convert to gray dengan menggunakan metode CNN.  

Accuracy CNN = 0.89 

Percobaan 6: 

Preprocessing yang dilakukan adalah resize, gaussian blur, dan convert to gray dengan menggunakan metode CNN.  

Accuracy CNN = 0.90 

Percobaan 7: 

Preprocessing yang dilakukan adalah resize, median blur, dan convert to gray dengan menggunakan metode CNN.  

Accuracy CNN = 0.89 

 

- Percobaan 0 menghasilkan akurasi lebih rendah dibandingkan dengan percobaan lain karena penggunaan metode GLCM dalam preprocessing tidak memberikan keuntungan signifikan bagi model CNN. 

- Percobaan 1 menunjukkan bahwa terlalu banyak tahapan preprocessing dapat menurunkan performa model dan menghasilkan akurasi terendah untuk semua model yang diuji, terutama pada CNN. 

- Percobaan 2 dan percobaan 4 m menunjukkan bahwa preprocessing sederhana seperti resize dan konversi ke grayscale bisa memberikan akurasi yang tinggi dan stabil. Ini berarti tahapan dasar ini sudah cukup efektif untuk mempersiapkan data bagi CNN. 

- Percobaan 5 dan percobaan 7 menunjukkan bahwa tambahan histogram equalization atau median blur tidak memberikan peningkatan yang signifikan dibandingkan dengan Percobaan 4, dengan akurasi yang tetap stabil.  

- Percobaan 6 menunjukkan bahwa penggunaan gaussian blur memberikan akurasi tertinggi, sedikit lebih tinggi dibandingkan dengan Percobaan 4 dan 5. Ini berarti gaussian blur bisa membantu meningkatkan fokus pada fitur yang relevan dan memberikan hasil yang lebih baik. 

 

## Modeling 

Dalam proses membuat model, langkah pertama adalah menyesuaikan learning rate dan menggunakan optimizer Adam untuk membangun model CNN menggunakan Keras Sequential API. Model ini terdiri dari beberapa lapisan konvolusi yang bertujuan untuk mengekstraksi fitur dari gambar, diikuti dengan lapisan pooling untuk mereduksi ukuran data. Setelah itu, data diproses dengan meratakan dan melewati lapisan Dense yang menggunakan aktivasi ReLU untuk menangkap pola-pola yang kompleks. Lapisan Dropout digunakan untuk mencegah model terlalu mengingat detail yang spesifik dari data latih, sehingga dapat menghasilkan hasil yang lebih baik pada data baru. Lapisan output menggunakan aktivasi softmax untuk melakukan klasifikasi. 

  

Sebelum data dimasukkan ke dalam model, proses preprocessing dimulai dengan ekstraksi fitur tekstur menggunakan metode GLCM. Setelah itu, data diproses lebih lanjut oleh CNN. Model ini dikompilasi dengan optimizer Adam, menggunakan fungsi loss sparse categorical crossentropy, dan metrik akurasi sebagai penilaian kinerja model. Callback EarlyStopping digunakan untuk menghentikan pelatihan jika tidak ada peningkatan kinerja pada data validasi, dan memastikan bahwa bobot terbaik digunakan dalam model akhir. 

  

Data yang digunakan untuk melatih model dibagi menjadi dua bagian, yaitu data latih untuk mengajari model dan data validasi untuk menguji seberapa baik model tersebut melakukan klasifikasi. Dengan menggunakan metode ini, model dapat menggunakan kombinasi preprocessing GLCM dan arsitektur CNN untuk memastikan hasil yang optimal dalam mengenali dan mengklasifikasi gambar. 

 

## Evaluation 

Hasil evaluasi menggunakan berbagai model pada dataset pengujian ditampilkan melalui confusion matrix untuk masing-masing model, yaitu KNN, SVM, dan Random Forest. Confusion matrix ini menggambarkan seberapa baik model dapat mengklasifikasikan data dengan memperlihatkan persentase prediksi yang benar dari setiap kelas, serta kesalahan prediksi antara kelas-kelas yang berbeda. 

  

Selain itu, akan disajikan juga confusion matrix khusus untuk model CNN, yang menyajikan jumlah absolut prediksi yang tepat dan kesalahan prediksi untuk setiap kelas target. 

  

Selanjutnya, akan ditampilkan kurva pembelajaran dari model CNN selama proses pelatihan. Kurva ini mencakup akurasi dan loss dari setiap epoch untuk melihat bagaimana performa model CNN berkembang seiring waktu, serta untuk mengidentifikasi apakah terjadi overfitting atau underfitting. 

  

Analisis ini memberikan gambaran tentang performa relatif dari setiap model dalam mengklasifikasikan data uji, serta memberikan wawasan tentang kekuatan dan kelemahan dari masing-masing model yang dievaluasi. Informasi ini dapat digunakan untuk memilih model yang paling sesuai untuk aplikasi spesifik atau untuk mengarahkan langkah-langkah perbaikan dan peningkatan performa model di masa depan. 

 

## GLCM 

Gray-Level Co-occurrence Matrix (GLCM) atau Matriks Ko-terjadi Tingkat Abu-abu adalah sebuah teknik dalam analisis citra yang digunakan untuk mengukur hubungan spasial antara pasangan nilai piksel dalam gambar grayscale. GLCM menghitung seberapa sering sepasang nilai piksel tertentu muncul bersama-sama dalam jarak dan arah tertentu dalam gambar. Dengan kata lain, GLCM menggambarkan pola atau tekstur dalam gambar berdasarkan frekuensi kemunculan pasangan nilai piksel yang berdekatan. Teknik ini sering digunakan untuk mengekstrak fitur-fitur tekstur dari gambar, seperti kasar atau halusnya permukaan, yang dapat digunakan untuk pengenalan pola, klasifikasi gambar, atau analisis citra medis. GLCM memberikan representasi statistik dari distribusi intensitas piksel dalam gambar, yang bermanfaat untuk berbagai aplikasi di bidang pengolahan gambar dan analisis citra. 

 

## Convolutional Neural Networks (CNN) 

Convolutional Neural Networks (CNN) adalah jenis model deep learning yang sangat efektif dalam menganalisis data visual seperti gambar dan video. CNN dirancang untuk meniru cara kerja otak manusia dalam memproses informasi visual. Arsitektur CNN terdiri dari beberapa lapisan yang berbeda, termasuk lapisan konvolusi untuk mengekstraksi fitur dari gambar, lapisan pooling untuk mengurangi dimensi data dan mempertahankan informasi yang relevan, serta lapisan fully connected yang digunakan untuk klasifikasi akhir. Proses konvolusi memungkinkan CNN untuk secara efisien mengidentifikasi pola kompleks dalam data visual, seperti tepi, tekstur, atau bentuk objek, yang kemudian digunakan untuk tugas-tugas seperti klasifikasi gambar, deteksi objek, atau pengenalan wajah. Keunggulan utama CNN adalah kemampuannya untuk belajar secara mandiri dari data pelatihan tanpa memerlukan fitur manual yang harus diekstrak terlebih dahulu, sehingga membuatnya sangat cocok untuk aplikasi dalam pengolahan gambar dan visi komputer secara umum. 

 
