
import tkinter as tk
from tkinter import ttk


class BukuView(tk.Tk):
    def __init__(self, user_role="admin"):
        super().__init__()

        self.user_role = str(user_role).strip().lower()

        self.title(f"Sistem Manajemen Perpustakaan - Mode: {self.user_role.upper()}")
        self.geometry("850x420")
        self.resizable(True, True)
        self.config(bg="#d9d9d9")

        # FRAME KIRI
        self.left_frame = tk.LabelFrame(
            self,
            text=" Form Data Buku ",
            font=("Arial", 10, "bold"),
            bg="#d9d9d9",
            padx=10,
            pady=10
        )
        self.left_frame.place(x=15, y=15, width=300, height=390)

        # Input Judul Buku
        self.entry_judul = tk.Entry(
            self.left_frame,
            fg="grey",
            font=("Arial", 9)
        )
        self.entry_judul.insert(0, "Masukkan Judul Buku")
        self.entry_judul.bind(
            "<FocusIn>",
            lambda e: self.clear_placeholder(
                self.entry_judul, "Masukkan Judul Buku"
            )
        )
        self.entry_judul.pack(fill="x", pady=6)

        # Input Penulis
        self.entry_penulis = tk.Entry(
            self.left_frame,
            fg="grey",
            font=("Arial", 9)
        )
        self.entry_penulis.insert(0, "Masukkan Nama Penulis")
        self.entry_penulis.bind(
            "<FocusIn>",
            lambda e: self.clear_placeholder(
                self.entry_penulis, "Masukkan Nama Penulis"
            )
        )
        self.entry_penulis.pack(fill="x", pady=6)

        # Input Tahun
        self.entry_tahun = tk.Entry(
            self.left_frame,
            fg="grey",
            font=("Arial", 9)
        )
        self.entry_tahun.insert(0, "Tahun Terbit (Misal: 2024)")
        self.entry_tahun.bind(
            "<FocusIn>",
            lambda e: self.clear_placeholder(
                self.entry_tahun, "Tahun Terbit (Misal: 2024)"
            )
        )
        self.entry_tahun.pack(fill="x", pady=6)

        # Tombol Simpan
        self.btn_simpan = tk.Button(
            self.left_frame,
            text="Simpan Data",
            bg="green",
            fg="white",
            font=("Arial", 9, "bold")
        )
        self.btn_simpan.pack(fill="x", pady=5)

        # Tombol Perbarui
        self.btn_update = tk.Button(
            self.left_frame,
            text="Perbarui Data",
            bg="orange",
            fg="black",
            font=("Arial", 9, "bold")
        )

        # Tombol Hapus
        self.btn_delete = tk.Button(
            self.left_frame,
            text="Hapus Data",
            bg="red",
            fg="white",
            font=("Arial", 9, "bold")
        )

        # Pengaturan tampilan berdasarkan role
        if self.user_role in ("anggota", "mahasiswa"):
            self.btn_simpan.configure(
                state="disabled",
                text="Akses Terkunci (Khusus Admin)"
            )

            self.entry_judul.configure(state="disabled")
            self.entry_penulis.configure(state="disabled")
            self.entry_tahun.configure(state="disabled")

        else:
            self.btn_update.pack(fill="x", pady=5)
            self.btn_delete.pack(fill="x", pady=5)

        # Tombol Logout
        self.btn_logout = tk.Button(
            self.left_frame,
            text="Logout",
            bg="gray",
            fg="white",
            font=("Arial", 9, "bold")
        )
        self.btn_logout.pack(fill="x", pady=(12, 5))

        # FRAME KANAN
        self.right_frame = tk.LabelFrame(
            self,
            text=" Daftar Koleksi Buku ",
            font=("Arial", 10, "bold"),
            bg="#d9d9d9",
            padx=10,
            pady=10
        )
        self.right_frame.place(x=330, y=15, width=500, height=390)

        # Tabel Buku
        columns = ("id", "judul", "penulis", "tahun")

        self.tabel = ttk.Treeview(
            self.right_frame,
            columns=columns,
            show="headings",
            height=12
        )

        self.tabel.heading("id", text="ID")
        self.tabel.heading("judul", text="Judul Buku")
        self.tabel.heading("penulis", text="Penulis")
        self.tabel.heading("tahun", text="Tahun")

        self.tabel.column("id", width=40, anchor="center")
        self.tabel.column("judul", width=170, anchor="w")
        self.tabel.column("penulis", width=160, anchor="w")
        self.tabel.column("tahun", width=60, anchor="center")

        self.tabel.pack(fill="both", expand=True)

    def clear_placeholder(self, entry_widget, placeholder_text):
        if entry_widget.get() == placeholder_text:
            entry_widget.delete(0, tk.END)
            entry_widget.config(fg="black")

    def run(self):
        self.mainloop()
