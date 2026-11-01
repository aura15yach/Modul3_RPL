import customtkinter as ctk
from tkinter import ttk

class BukuView(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Sistem Manajemen Perpustakaan")
        self.geometry("900x500")
        
        # Konfigurasi Grid Utama
        self.grid_columnconfigure(0, weight=1) # Form (Kiri)
        self.grid_columnconfigure(1, weight=2) # Tabel (Kanan)
        self.grid_rowconfigure(0, weight=1)
        
        # ==========================================
        # FRAME KIRI: FORMULIR & TOMBOL AKSI
        # ==========================================
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")
        
        ctk.CTkLabel(self.frame_kiri, text="Form Data Buku", font=("Arial", 16, "bold")).pack(pady=15)
        
        # Input Form (Tanpa Penerbit)
        self.entry_judul = ctk.CTkEntry(self.frame_kiri, placeholder_text="Judul Buku")
        self.entry_judul.pack(pady=8, padx=15, fill="x")
        
        self.entry_penulis = ctk.CTkEntry(self.frame_kiri, placeholder_text="Penulis / Pengarang")
        self.entry_penulis.pack(pady=8, padx=15, fill="x")
        
        self.entry_tahun = ctk.CTkEntry(self.frame_kiri, placeholder_text="Tahun Terbit")
        self.entry_tahun.pack(pady=8, padx=15, fill="x")
        
        # Tombol Aksi (Simpan, Perbarui, Hapus)
        self.btn_simpan = ctk.CTkButton(self.frame_kiri, text="Simpan Data", fg_color="green")
        self.btn_simpan.pack(pady=8, padx=15, fill="x")
        
        self.btn_perbarui = ctk.CTkButton(self.frame_kiri, text="Perbarui Data", fg_color="orange")
        self.btn_perbarui.pack(pady=8, padx=15, fill="x")
        
        self.btn_hapus = ctk.CTkButton(self.frame_kiri, text="Hapus Data", fg_color="red")
        self.btn_hapus.pack(pady=8, padx=15, fill="x")
        
        # ==========================================
        # FRAME KANAN: TABEL DAFTAR BUKU
        # ==========================================
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(row=0, column=1, padx=10, pady=15, sticky="nsew")
        
        ctk.CTkLabel(self.frame_kanan, text="Daftar Koleksi Buku", font=("Arial", 16, "bold")).pack(pady=15)
        
        # Tabel Treeview (Tanpa Penerbit)
        kolom = ("id", "judul", "pengarang", "tahun")
        self.tabel = ttk.Treeview(self.frame_kanan, columns=kolom, show="headings", height=15)
        
        self.tabel.heading("id", text="ID")
        self.tabel.heading("judul", text="Judul Buku")
        self.tabel.heading("pengarang", text="Pengarang")
        self.tabel.heading("tahun", text="Tahun")
        
        self.tabel.column("id", width=30, anchor="center")
        self.tabel.column("judul", width=180)
        self.tabel.column("pengarang", width=150)
        self.tabel.column("tahun", width=80, anchor="center")
        
        self.tabel.pack(fill="both", expand=True, padx=15, pady=10)

if __name__ == "__main__":
    app = BukuView()
    app.mainloop()