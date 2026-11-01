from config.database import Database

class BukuModel:
    def __init__(self):
        self.db = Database()

    def get_all_buku(self):
        connection = self.db.get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM buku")
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result

    def create_buku(self, judul, penulis, tahun):
        try:
            connection = self.db.get_connection()
            cursor = connection.cursor()
            query = "INSERT INTO buku (judul, penulis, tahun) VALUES (%s, %s, %s)"
            cursor.execute(query, (judul, penulis, tahun))
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except Exception as e:
            print(f"Gagal menyimpan data buku: {e}")
            return False

    def delete_buku(self, id_buku):
        try:
            connection = self.db.get_connection()
            cursor = connection.cursor()
            
            # Hapus data relasi dulu agar tidak kena error foreign key
            query_relasi = "DELETE FROM peminjaman WHERE id_buku = %s"
            cursor.execute(query_relasi, (id_buku,))
            
            # Hapus data bukunya
            query_buku = "DELETE FROM buku WHERE id_buku = %s"
            cursor.execute(query_buku, (id_buku,))
            
            connection.commit()
            cursor.close()
            connection.close()
            return True
            
        except Exception as e:
            print(f"Gagal menghapus data buku: {e}")
            return False