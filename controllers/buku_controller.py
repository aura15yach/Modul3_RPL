
import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView


class BukuController:
    def __init__(self, user_role="anggota"):
        self.user_role = str(user_role).strip().lower()

        # Hak akses Admin dan Petugas
        self.izin_kelola = self.user_role in ("admin", "petugas")

        self.model = BukuModel()
        self.view = BukuView(user_role=self.user_role)

        # Menghubungkan tombol dengan fungsi
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_update.configure(command=self.perbarui_data)
        self.view.btn_delete.configure(command=self.hapus_data)
        self.view.btn_logout.configure(command=self.logout)

        # Menghubungkan tabel dengan fungsi pilih data
        self.view.tabel.bind(
            "<<TreeviewSelect>>",
            self.pilih_data
        )

        # Pengaturan hak akses anggota
        if not self.izin_kelola:
            self.view.btn_simpan.configure(
                state="disabled",
                text="Akses Terkunci (Khusus Admin)"
            )

            # Menyembunyikan tombol Perbarui dan Hapus
            self.view.btn_update.pack_forget()
            self.view.btn_delete.pack_forget()

            # Menonaktifkan form input
            self.view.entry_judul.configure(state="disabled")
            self.view.entry_penulis.configure(state="disabled")
            self.view.entry_tahun.configure(state="disabled")

        # Memuat data buku ke tabel
        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        data_buku = self.model.get_all_buku()

        for buku in data_buku:
            self.view.tabel.insert(
                "",
                "end",
                values=(
                    buku["id_buku"],
                    buku["judul"],
                    buku["penulis"],
                    buku["tahun_terbit"]
                )
            )

    def pilih_data(self, event=None):
        if not self.izin_kelola:
            return

        selected = self.view.tabel.selection()

        if selected:
            data = self.view.tabel.item(selected[0], "values")

            self.view.entry_judul.delete(0, "end")
            self.view.entry_penulis.delete(0, "end")
            self.view.entry_tahun.delete(0, "end")

            self.view.entry_judul.insert(0, data[1])
            self.view.entry_penulis.insert(0, data[2])
            self.view.entry_tahun.insert(0, data[3])

    def simpan_data(self):
        if not self.izin_kelola:
            messagebox.showerror(
                "Akses Ditolak",
                "Anda tidak memiliki izin untuk menambah data!"
            )
            return

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom form harus diisi!"
            )
            return

        if self.model.create_buku(judul, penulis, tahun):
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil disimpan!"
            )
            self.kosongkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Gagal menyimpan data ke database."
            )

    def perbarui_data(self):
        if not self.izin_kelola:
            messagebox.showerror(
                "Akses Ditolak",
                "Anda tidak memiliki izin untuk memperbarui data!"
            )
            return

        selected = self.view.tabel.selection()

        if not selected:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data buku yang ingin diperbarui!"
            )
            return

        data = self.view.tabel.item(selected[0], "values")
        id_buku = data[0]

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom form harus diisi!"
            )
            return

        if self.model.update_buku(id_buku, judul, penulis, tahun):
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil diperbarui!"
            )
            self.kosongkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Gagal memperbarui data buku."
            )

    def hapus_data(self):
        if not self.izin_kelola:
            messagebox.showerror(
                "Akses Ditolak",
                "Anda tidak memiliki izin untuk menghapus data!"
            )
            return

        selected = self.view.tabel.selection()

        if not selected:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data buku yang ingin dihapus!"
            )
            return

        data = self.view.tabel.item(selected[0], "values")
        id_buku = data[0]

        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            "Apakah Anda yakin ingin menghapus data buku ini?"
        )

        if konfirmasi:
            if self.model.delete_buku(id_buku):
                messagebox.showinfo(
                    "Sukses",
                    "Data buku berhasil dihapus!"
                )
                self.kosongkan_form()
                self.muat_data_tabel()
            else:
                messagebox.showerror(
                    "Error",
                    "Gagal menghapus data buku."
                )

    def kosongkan_form(self):
        if not self.izin_kelola:
            return

        self.view.entry_judul.delete(0, "end")
        self.view.entry_penulis.delete(0, "end")
        self.view.entry_tahun.delete(0, "end")

    def logout(self):
        self.view.destroy()

        from controllers.auth_controller import AuthController

        login = AuthController()
        login.run()

    def run(self):
        self.view.mainloop()
