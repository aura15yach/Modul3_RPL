import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaApp


class AnggotaController:
    def __init__(self):
        self.model = AnggotaModel()
        self.view = AnggotaApp()

        # Hubungkan tombol simpan dengan fungsi Controller
        self.view.btn_simpan.configure(
            command=self.simpan_data
        )

        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        data_anggota = self.model.get_all_anggota()

        for anggota in data_anggota:
            self.view.tabel.insert(
                "",
                "end",
                values=tuple(anggota.values())
            )

    def simpan_data(self):
        nama = self.view.entry_nama.get()
        # Ambil teks dari CTkTextbox dengan benar
        alamat = self.view.entry_alamat.get("1.0", "end-1c").strip()

        if not nama or not alamat:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom harus diisi!"
            )
            return

        berhasil = self.model.create_anggota(nama, alamat)

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data anggota berhasil disimpan!"
            )
            self.muat_data_tabel()
            
            # Bersihkan form setelah sukses disimpan
            self.view.entry_nama.delete(0, 'end')
            self.view.entry_alamat.delete("1.0", "end")
        else:
            messagebox.showerror(
                "Error",
                "Data anggota gagal disimpan."
            )

    def run(self):
        self.view.mainloop()