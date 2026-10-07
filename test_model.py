from models.buku_model import BukuModel
from models.anggota_model import AnggotaModel

# ==========================================
# PENGUJIAN BUKU MODEL
# ==========================================
print("=== PENGUJIAN BUKU MODEL ===")
buku_model = BukuModel()

# Menambahkan data buku baru
print("\n[+] Menambahkan data buku...")
buku_model.create_buku("Pemrograman Python MVC", "Guido van Rossum", 2023)

# Mengubah data buku
print("\n[*] Mengubah data buku ID 1...")
buku_model.update_buku(1, "Laut Bercerita (Edisi Revisi)", "Leila S. Chudori", 2018)

# Menghapus data buku (menggunakan ID 5 agar tidak terbentrok Foreign Key)
print("\n[-] Menghapus data buku ID 5...")
buku_model.delete_buku(5)

# Menampilkan Daftar Buku Terkini
print("\n=== Daftar Buku Terkini ===")
daftar_buku = buku_model.get_all_buku()
for buku in daftar_buku:
    print(f"[{buku['id_buku']}] {buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")


# ==========================================
# PENGUJIAN ANGGOTA MODEL
# ==========================================
print("\n\n=== PENGUJIAN ANGGOTA MODEL ===")
anggota_model = AnggotaModel()

# Menambahkan data anggota
print("\n[+] Menambahkan data anggota...")
anggota_model.create_anggota("Budi Santoso", "Jl. Mawar No. 12, Jakarta")

# Menampilkan Daftar Anggota Terkini
print("\n=== Daftar Anggota Terkini ===")
daftar_anggota = anggota_model.get_all_anggota()
for anggota in daftar_anggota:
    print(f"[{anggota['id_anggota']}] {anggota['nama']} - {anggota['alamat']}")