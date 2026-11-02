from config.database import Database

class BukuModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "buku"

    def get_all_buku(self):
        """Mengambil seluruh data buku dari database"""
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)
            query = f"SELECT id_buku, judul, penulis, tahun_terbit FROM {self.table_name}"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        return []

    def create_buku(self, judul, penulis, tahun):
        """Menambahkan data buku baru"""
        if self.conn:
            cursor = self.conn.cursor()
            query = f"INSERT INTO {self.table_name} (judul, penulis, tahun_terbit) VALUES (%s, %s, %s)"
            try:
                cursor.execute(query, (judul, penulis, tahun))
                self.conn.commit()
                cursor.close()
                return True
            except Exception as e:
                print(f"Gagal insert buku: {e}")
                cursor.close()
                return False
        return False

    def update_buku(self, id_buku, judul, penulis, tahun):
        """Memperbarui data buku berdasarkan ID"""
        if self.conn:
            cursor = self.conn.cursor()
            query = f"UPDATE {self.table_name} SET judul = %s, penulis = %s, tahun_terbit = %s WHERE id_buku = %s"
            try:
                cursor.execute(query, (judul, penulis, tahun, id_buku))
                self.conn.commit()
                cursor.close()
                return True
            except Exception as e:
                print(f"Gagal update buku: {e}")
                cursor.close()
                return False
        return False

    def delete_buku(self, id_buku):
        """Menghapus data buku berdasarkan ID"""
        if self.conn:
            cursor = self.conn.cursor()
            query = f"DELETE FROM {self.table_name} WHERE id_buku = %s"
            try:
                cursor.execute(query, (id_buku,))
                self.conn.commit()
                cursor.close()
                return True
            except Exception as e:
                print(f"Gagal hapus buku: {e}")
                cursor.close()
                return False
        return False