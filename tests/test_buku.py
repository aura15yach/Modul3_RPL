from unittest.mock import MagicMock
from models.buku_model import BukuModel


def test_get_all_buku():
    model = BukuModel()

    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    data_buku = [
        {
            "id_buku": 1,
            "judul": "Buku Testing",
            "penulis": "Penulis QA",
            "tahun_terbit": 2026
        }
    ]

    mock_cursor.fetchall.return_value = data_buku

    hasil = model.get_all_buku()

    assert hasil == data_buku
    mock_cursor.execute.assert_called_once()