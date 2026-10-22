import customtkinter as ctk
from tkinter import ttk


class AnggotaApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistem Perpustakaan - Manajemen Data Anggota")
        self.geometry("1000x650")

        # ==========================================
        # DATA ANGGOTA
        # ==========================================

        self.data_anggota = [
            (
                1,
                "Aura Qadriandhara",
                "Jl. Anoa 1"
            )
        ]

        # ==========================================
        # KONFIGURASI GRID
        # ==========================================

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # ==========================================
        # FRAME KIRI
        # ==========================================

        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(
            row=0,
            column=0,
            padx=20,
            pady=20,
            sticky="nsew"
        )

        ctk.CTkLabel(
            self.frame_kiri,
            text="Form Data Anggota",
            font=("Arial", 20, "bold")
        ).pack(pady=25)

        # ==========================================
        # INPUT NAMA ANGGOTA
        # ==========================================

        ctk.CTkLabel(
            self.frame_kiri,
            text="Nama Anggota:",
            font=("Arial", 14)
        ).pack(
            anchor="w",
            padx=20,
            pady=(10, 5)
        )

        self.entry_nama = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan Nama Lengkap",
            height=35
        )

        self.entry_nama.pack(
            padx=20,
            fill="x"
        )

        # ==========================================
        # INPUT ALAMAT
        # ==========================================

        ctk.CTkLabel(
            self.frame_kiri,
            text="Alamat:",
            font=("Arial", 14)
        ).pack(
            anchor="w",
            padx=20,
            pady=(25, 5)
        )

        self.entry_alamat = ctk.CTkTextbox(
            self.frame_kiri,
            height=100
        )

        self.entry_alamat.pack(
            padx=20,
            fill="x"
        )

        # ==========================================
        # TOMBOL SIMPAN
        # ==========================================

        self.btn_simpan = ctk.CTkButton(
            self.frame_kiri,
            text="Simpan Data",
            fg_color="#20b15a",
            height=35,
            command=self.simpan_data
        )

        self.btn_simpan.pack(
            padx=20,
            pady=20,
            fill="x"
        )

        # ==========================================
        # FRAME KANAN
        # ==========================================

        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(
            row=0,
            column=1,
            padx=(0, 20),
            pady=20,
            sticky="nsew"
        )

        ctk.CTkLabel(
            self.frame_kanan,
            text="Daftar Anggota Perpustakaan",
            font=("Arial", 20, "bold")
        ).pack(pady=25)

        # ==========================================
        # TABEL ANGGOTA
        # ==========================================

        kolom = (
            "id",
            "nama",
            "alamat"
        )

        self.tabel = ttk.Treeview(
            self.frame_kanan,
            columns=kolom,
            show="headings"
        )

        self.tabel.heading(
            "id",
            text="ID Anggota"
        )

        self.tabel.heading(
            "nama",
            text="Nama Anggota"
        )

        self.tabel.heading(
            "alamat",
            text="Alamat"
        )

        self.tabel.column(
            "id",
            width=100,
            anchor="center"
        )

        self.tabel.column(
            "nama",
            width=220,
            anchor="center"
        )

        self.tabel.column(
            "alamat",
            width=350,
            anchor="center"
        )

        self.tabel.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        # ==========================================
        # TAMPILKAN DATA AWAL
        # ==========================================

        self.tampilkan_data()

    # ==========================================
    # MENAMPILKAN DATA
    # ==========================================

    def tampilkan_data(self):

        for item in self.tabel.get_children():
            self.tabel.delete(item)

        for data in self.data_anggota:
            self.tabel.insert(
                "",
                "end",
                values=data
            )

    # ==========================================
    # SIMPAN DATA
    # ==========================================

    def simpan_data(self):

        nama = self.entry_nama.get()

        alamat = self.entry_alamat.get(
            "1.0",
            "end-1c"
        )

        if nama == "" or alamat == "":
            return

        id_baru = len(self.data_anggota) + 1

        data_baru = (
            id_baru,
            nama,
            alamat
        )

        self.data_anggota.append(
            data_baru
        )

        self.tampilkan_data()

        # Bersihkan form
        self.entry_nama.delete(
            0,
            "end"
        )

        self.entry_alamat.delete(
            "1.0",
            "end"
        )


# ==========================================
# BLOK EKSEKUSI
# ==========================================

if __name__ == "__main__":
    app = AnggotaApp()
    app.mainloop()