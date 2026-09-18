# Bike Sharing Dashboard

Dashboard interaktif untuk menganalisis data penyewaan sepeda dari Bike Sharing Dataset. Proyek ini dibuat dengan Streamlit dan menampilkan ringkasan performa penyewaan sepeda berdasarkan rentang tanggal, cuaca, musim, temperatur, dan kelembapan.

## Ringkasan Proyek

Dashboard ini menggunakan data historis penyewaan sepeda tahun 2011-2012 dari Capital Bikeshare, Washington D.C. Data utama yang dipakai aplikasi adalah `all_df.csv`, yaitu data hasil pengolahan dari dataset harian dan per jam.

Fitur utama dashboard:

- Filter rentang tanggal melalui sidebar.
- Total penyewaan sepeda dalam periode terpilih.
- Estimasi pendapatan dengan asumsi Rp10.000 per penyewa.
- Tren penyewaan harian.
- Visualisasi hubungan temperatur dan kelembapan terhadap jumlah penyewaan.
- Perbandingan total penyewaan berdasarkan kondisi cuaca.
- Perbandingan total penyewaan berdasarkan musim.
- Informasi jumlah penyewaan harian tertinggi pada periode terpilih.

## Struktur File

```text
.
├── dashboard.py                  # Aplikasi dashboard Streamlit
├── Proyek_Analisis_Data.ipynb    # Notebook eksplorasi dan analisis data
├── all_df.csv                    # Dataset hasil pengolahan yang digunakan dashboard
├── day.csv                       # Dataset agregasi harian
├── hour.csv                      # Dataset agregasi per jam
├── penamaan_pada_data.txt        # Dokumentasi atribut dataset
├── requirements.txt              # Daftar dependency Python
└── link.txt                      # Link dashboard yang sudah dipublikasikan
```

## Menjalankan Dashboard Secara Lokal

Pastikan Python sudah terpasang. Proyek ini direkomendasikan berjalan dengan Python 3.9 atau versi yang kompatibel dengan dependency pada `requirements.txt`.

### 1. Masuk ke folder proyek

```sh
cd "/Users/haifanghani/Library/Mobile Documents/com~apple~CloudDocs/Tugas Dicoding/ProyekAkhir_1"
```

Jika menjalankan dari folder lain, sesuaikan path dengan lokasi proyek di komputer Anda.

### 2. Buat dan aktifkan virtual environment

Dengan `venv`:

```sh
python3 -m venv .venv
source .venv/bin/activate
```

Atau dengan Conda:

```sh
conda create --name bike-sharing-dashboard python=3.9
conda activate bike-sharing-dashboard
```

### 3. Install dependency

```sh
pip install -r requirements.txt
```

### 4. Jalankan aplikasi Streamlit

```sh
streamlit run dashboard.py
```

Setelah perintah dijalankan, Streamlit akan menampilkan URL lokal seperti:

```text
http://localhost:8501
```

Buka URL tersebut di browser untuk menggunakan dashboard.

## Catatan Penting

- Jalankan perintah `streamlit run dashboard.py` dari root folder proyek agar file `all_df.csv` dapat terbaca.
- Jika aplikasi gagal membaca dataset, pastikan `all_df.csv` berada di folder yang sama dengan `dashboard.py`.
- Dashboard yang sudah dipublikasikan dapat dilihat melalui link pada file `link.txt`.

## Dataset

Dataset berasal dari Bike Sharing Dataset oleh Hadi Fanaee-T dan Joao Gama. Dataset ini berisi catatan penyewaan sepeda yang dipengaruhi oleh faktor waktu, cuaca, musim, temperatur, kelembapan, hari kerja, dan hari libur.

Referensi:

Fanaee-T, Hadi, and Gama, Joao. "Event labeling combining ensemble detectors and background knowledge." Progress in Artificial Intelligence, 2013.
