
# Sistem Manajemen Perpustakaan

## 1. Deskripsi Aplikasi

Sistem Manajemen Perpustakaan merupakan aplikasi berbasis desktop yang dikembangkan menggunakan bahasa pemrograman Python dengan menerapkan konsep Model-View-Controller (MVC). Aplikasi ini digunakan untuk mengelola data buku serta menerapkan sistem autentikasi dan otorisasi pengguna berdasarkan hak akses masing-masing pengguna.

Aplikasi menyediakan fitur login, pengelolaan data buku, serta pembatasan akses berdasarkan role pengguna, yaitu admin, petugas, dan anggota.

## 2. Struktur Direktori MVC

Proyek ini menggunakan konsep Model-View-Controller (MVC) untuk memisahkan pengelolaan data, tampilan aplikasi, dan proses pengendalian aplikasi.

```text
MODUL 3 RPL/
│
├── config/
│   └── database.py
│
├── controllers/
│   ├── anggota_controller.py
│   ├── auth_controller.py
│   └── buku_controller.py
│
├── dist/
│   └── AplikasiPerpustakaan.exe
│
├── models/
│   ├── anggota_model.py
│   ├── buku_model.py
│   └── user_model.py
│
├── tests/
│   ├── test_auth.py
│   └── test_buku.py
│
├── views/
│   ├── anggota_view.py
│   ├── buku_view.py
│   └── login_view.py
│
├── .github/
│   └── workflows/
│       └── ci_pipeline.yml
│
├── AplikasiPerpustakaan.spec
├── main.py
├── requirements.txt
├── README.md
└── test_model.py
```

### Penjelasan Direktori

- **config:** Menyimpan konfigurasi koneksi database MySQL.
- **controllers:** Mengatur proses aplikasi dan menghubungkan model dengan tampilan.
- **models:** Mengelola data serta operasi yang berhubungan dengan database.
- **views:** Menampilkan antarmuka aplikasi kepada pengguna.
- **tests:** Menyimpan file pengujian aplikasi menggunakan Pytest.
- **dist:** Menyimpan hasil aplikasi yang telah dikemas menjadi file executable.
- **.github/workflows:** Menyimpan konfigurasi CI Pipeline untuk menjalankan pemeriksaan kode dan pengujian otomatis.

## 3. Panduan Instalasi dan Konfigurasi Database MySQL

### A. Persiapan

Sebelum menjalankan aplikasi, pastikan perangkat telah memiliki:
- Python.
- Laragon.
- MySQL.
- Git.

### B. Mengunduh Proyek

Unduh proyek melalui GitHub menggunakan perintah:

```bash
git clone https://github.com/aura15yach/Modul3_RPL.git
```

Masuk ke direktori proyek:

```bash
cd Modul3_RPL
```

### C. Membuat Virtual Environment

Buat lingkungan virtual Python menggunakan perintah:

```bash
python -m venv env
```

Aktifkan virtual environment pada Windows:

```bash
env\Scripts\activate
```

### D. Menginstal Library

Instal seluruh library yang dibutuhkan melalui file requirements.txt:

```bash
pip install -r requirements.txt
```

### E. Konfigurasi Database MySQL

1. Buka aplikasi Laragon.
2. Jalankan layanan MySQL.
3. Buka HeidiSQL atau aplikasi pengelola database lainnya.
4. Buat database dengan nama `perpustakaan`.

Gunakan perintah SQL berikut:

```sql
CREATE DATABASE perpustakaan;
```

Sesuaikan pengaturan koneksi pada file `config/database.py` dengan konfigurasi MySQL yang digunakan:

- Host: localhost
- Port: 3306
- Username: root
- Password: sesuaikan dengan konfigurasi MySQL.
- Database: perpustakaan.

Pastikan tabel yang dibutuhkan aplikasi sudah tersedia di dalam database sebelum menjalankan aplikasi.

## 4. Cara Menjalankan Aplikasi

Setelah proses instalasi dan konfigurasi database selesai, ikuti langkah berikut:

1. Pastikan layanan MySQL pada Laragon sudah berjalan.
2. Buka terminal pada direktori proyek.
3. Aktifkan virtual environment.
4. Jalankan aplikasi menggunakan perintah:

```bash
python main.py
```

5. Aplikasi akan menampilkan halaman login.
6. Masukkan username dan password sesuai akun yang telah terdaftar di database.
7. Setelah berhasil login, pengguna akan diarahkan ke halaman aplikasi sesuai hak akses masing-masing role.

## 5. Pengujian Aplikasi

Pengujian aplikasi dilakukan menggunakan Pytest dengan perintah:

```bash
python -m pytest -v tests/
```

Pemeriksaan kualitas kode dilakukan menggunakan Flake8 dengan perintah:

```bash
flake8 models/ controllers/ --count --select=E9,F63,F7,F82 --show-source --statistics
```

Kedua proses tersebut juga dijalankan secara otomatis melalui GitHub Actions pada CI Pipeline.
