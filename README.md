# 📚 Library Hub - Sistem Manajemen Perpustakaan

Library Hub adalah aplikasi manajemen perpustakaan berbasis desktop yang dibangun menggunakan **Python** dan **PyQt5**. Aplikasi ini menerapkan prinsip **Object-Oriented Programming (OOP)** dan menggunakan **MySQL** sebagai sistem manajemen basis data untuk mengelola data anggota, inventaris buku, serta transaksi peminjaman secara real-time.

## ✨ Fitur Utama

### 🔐 Multi-User Authentication

* **Petugas (Admin):** Memiliki akses penuh untuk mengelola data buku, memvalidasi permintaan peminjaman, dan mengelola data anggota.
* **Anggota:** Dapat melihat katalog buku yang tersedia, mengajukan peminjaman, dan melihat riwayat peminjaman pribadi.

### 📖 Manajemen Inventaris

* Operasi CRUD (Create, Read, Update, Delete) data buku.
* Pencarian buku berdasarkan judul atau pengarang.
* Indikator stok buku otomatis (berkurang saat dipinjam, bertambah saat dikembalikan).

### 📝 Sistem Peminjaman Terintegrasi

* **Validasi Stok:** Mencegah peminjaman jika stok buku habis.
* **Status Workflow:** Alur peminjaman yang rapi mulai dari *Pending* -> *Dipinjam* -> *Dikembalikan*.
* **Penyetujuan Admin:** Admin memiliki otoritas untuk menyetujui atau menolak permintaan pinjam.

---

## 🛠️ Teknologi yang Digunakan

* **Bahasa Pemrograman:** Python 3.13+
* **GUI Framework:** PyQt5 (Modern Dark Theme)
* **Database:** MySQL (MariaDB)
* **Database Connector:** `mysql-connector-python`

---

## 🚀 Cara Instalasi

1. **Clone Repositori**
```bash
git clone https://github.com/username/perpustakaan-python.git
cd perpustakaan-python

```


2. **Instal Dependensi**
Pastikan Anda memiliki Python terinstal, lalu jalankan:
```bash
pip install PyQt5 mysql-connector-python

```


3. **Konfigurasi Database**
* Buka XAMPP dan aktifkan MySQL.
* Buat database baru bernama `db_perpustakaan_pbo`.
* Impor file `.sql` (jika ada) atau pastikan tabel `user`, `anggota`, `buku`, dan `pinjam` sudah sesuai dengan skema di `modul/`.
* Sesuaikan konfigurasi di `modul/database.py` jika username/password database Anda berbeda.


4. **Jalankan Aplikasi**
```bash
python main.py

```



---

## 📂 Struktur Proyek

```text
Perpustakaan - Python/
├── main.py              # Entry point aplikasi
├── login.py             # Logic & UI Halaman Login
├── petugas.py           # Dashboard Admin/Petugas
├── anggota.py           # Dashboard Anggota
├── form_buku.py         # Form Tambah/Edit Buku
├── form_validasi.py     # Panel Persetujuan Admin
└── modul/               # Folder Logika & Database (Models)
    ├── database.py      # Koneksi Database
    ├── buku.py          # CRUD Buku
    ├── pinjam.py        # Logic Transaksi Pinjam
    └── user.py          # Logic Login & User Session

