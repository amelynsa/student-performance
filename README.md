# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut (berdiri 2000) menghadapi tingkat dropout yang tinggi yang sangat memengaruhi reputasi dan efisiensi biaya. Proyek ini bertujuan untuk mendeteksi dini siswa berisiko agar tim akademik dapat melakukan intervensi tepat waktu (bimbingan akademik, dukungan finansial, dsb.).

### Permasalahan Bisnis
1. Bagaimana mengidentifikasi siswa berisiko dropout sejak awal?
2. Faktor akademik, demografis, finansial apa saja yang memengaruhi keputusan dropout?
3. Bagaimana memonitor metrik kunci (dropout rate, admission grade) secara real time?

### Cakupan Proyek
1. Melakukan analisis data untuk menemukan faktor-faktor utama penyebab dropout.
2. Membangun dashboard interaktif menggunakan Metabase untuk monitoring performa mahasiswa.
3. Membuat prototype sistem machine learning untuk memprediksi kemungkinan dropout mahasiswa.

### Persiapan

Sumber data: **Predict Students' Dropout and Academic Success** (https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success)

Setup environment:
```bash
# Instalasi dependencies
pip install pipenv
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Business Dashboard
Dashboard dibuat menggunakan Metabase dan berisi beberapa visualisasi utama:
1. perbandingan jumlah status siswa
2. rata-rata nilai tes masuk per status
3. jumlah siswa debtor per status
4. rata-rata nilai semester 1 dan semester 2 per status
5. jumlah siswa pemegang beasiswa per status
6. rata-rata usia masuk siswa per status

```bash

docker run -d ^
  --name <nama_kontainer> ^
  -p 3000:3000 ^
  -v "<path_local_proyek>:/<direktori di kontainer>" ^
  -e "MB_DB_FILE=/<direktori di kontainer>/metabase.db" ^
  metabase/metabase

**Menambahkan Data Source SQLite**
** Setelah Metabase jalan: **
**1. Masuk ke Admin settings → Databases → Add database**
**2. Pilih SQLite**
**3. Masukkan Database file path:**
  /<direktori_di_kontainer>/data_mahasiswa.db
**4. Klik Save**

# Backup Dashboard Metabase
  docker cp metabase:/metabase.db ./metabase.db   
```

Akses Dashboard:
```bash

Email: ameliayunisaaa@gmail.com
Password: 25amelultah
URL: http://localhost:3000

```


## Menjalankan Sistem Machine Learning
Sistem machine learning dibangun menggunakan Random Forest Classifier dan telah di-deploy sebagai prototype menggunakan Streamlit.

Untuk mengakses prototype streamlit:

```
https://student-performance-amelynsa.streamlit.app/
```
File model telah disimpan sebagai model.pkl.


## Conclusion

Proyek ini bertujuan membantu Jaya Jaya Institut mengidentifikasi mahasiswa yang berisiko tinggi untuk dropout menggunakan pendekatan Machine Learning. Berdasarkan model Random Forest yang dilatih menggunakan data akademik dan sosial-ekonomi mahasiswa, fitur-fitur seperti:

- **Admission Grade**
- **Status Pembayaran (Tuition Fees Up to Date)**
- **Status Debtor**
- **Nilai Akademik Semester 1 & 2**
- **Jumlah SKS yang Disetujui dan Diambil**
- **Faktor Eksternal seperti Tingkat Pengangguran dan GDP**

merupakan indikator kuat dalam menentukan risiko dropout mahasiswa.  
Model mencapai **[tulis skor akurasi/recall kamu di sini]**, dengan kemampuan mendeteksi mayoritas mahasiswa berisiko tinggi.

Platform end-to-end telah dibangun:
- Dashboard **Metabase** untuk analisis cohort dan monitoring institusional.
- Aplikasi **Streamlit** untuk prediksi risiko individual mahasiswa secara real-time.

---

## Rekomendasi Action Items

Berdasarkan hasil analisis dan model, berikut langkah-langkah strategis yang dapat dilakukan oleh institusi:

1. **Peringatan Dini Otomatis**
   - Kirim notifikasi (email/SMS) kepada mahasiswa dengan **Admission Grade < 130** atau **Debtor = 1**.
   - Integrasikan prediksi model ke sistem informasi akademik.

2. **Program Remedial & Mentoring**
   - Wajibkan mahasiswa berisiko tinggi mengikuti kelas tambahan atau mentoring intensif.
   - Fokus pada mahasiswa dengan nilai semester 1 & 2 di bawah rata-rata.

3. **Skema Dukungan Finansial**
   - Tawarkan beasiswa mikro, cicilan biaya kuliah, atau penghapusan denda keterlambatan untuk mahasiswa dengan status *Debtor* atau *Tuition_fees_up_to_date = 0*.

4. **Evaluasi Berkala**
   - Lakukan rapat bulanan tim akademik berdasarkan insight dashboard Metabase.
   - Gunakan data prediksi untuk menentukan strategi intervensi berikutnya.

5. **Kolaborasi Lintas Unit**
   - Libatkan unit akademik, keuangan, dan kemahasiswaan untuk membuat *Early Warning System* terintegrasi.

---

## Dampak yang Diharapkan

Dengan mengimplementasikan rekomendasi di atas, institusi diharapkan mampu:
- Menurunkan angka dropout secara signifikan.
- Meningkatkan retensi dan keberhasilan studi mahasiswa.
- Mengoptimalkan intervensi berbasis data untuk pengambilan keputusan.


