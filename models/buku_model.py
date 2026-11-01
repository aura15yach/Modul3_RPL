from config.database import Database


class BukuModel:

    def __init__(self):
        self.db = Database()
        self.conn = None

    # Menambahkan data buku
    def create_buku(self, judul, penulis, tahun):
        if self.conn is not None:
            connection = self.conn
        else:
            connection = self.db.get_connection()

        cursor = connection.cursor()

        query = """
            INSERT INTO buku (judul, penulis, tahun_terbit)
            VALUES (%s, %s, %s)
        """

        cursor.execute(query, (judul, penulis, tahun))
        connection.commit()

        cursor.close()

        if self.conn is None:
            connection.close()

        return True

    # Menampilkan seluruh data buku
    def get_all_buku(self):
        if self.conn is not None:
            connection = self.conn
        else:
            connection = self.db.get_connection()

        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM buku")
        result = cursor.fetchall()

        cursor.close()

        if self.conn is None:
            connection.close()

        return result

    # Memperbarui data buku
    def update_buku(self, id_buku, judul, penulis, tahun):
        if self.conn is not None:
            connection = self.conn
        else:
            connection = self.db.get_connection()

        cursor = connection.cursor()

        query = """
            UPDATE buku
            SET judul = %s,
                penulis = %s,
                tahun_terbit = %s
            WHERE id_buku = %s
        """

        cursor.execute(query, (judul, penulis, tahun, id_buku))
        connection.commit()

        cursor.close()

        if self.conn is None:
            connection.close()

        return True

    # Menghapus data buku
    def delete_buku(self, id_buku):
        if self.conn is not None:
            connection = self.conn
        else:
            connection = self.db.get_connection()

        cursor = connection.cursor()

        query = "DELETE FROM buku WHERE id_buku = %s"

        cursor.execute(query, (id_buku,))
        connection.commit()

        cursor.close()

        if self.conn is None:
            connection.close()

        return True