from modul.database import get_connection

class BukuModel:
    @staticmethod
    def create(id_buku, judul, pengarang, penerbit, tahun, stok):
        db = get_connection()
        cursor = db.cursor()
        try:
            query = "INSERT INTO buku VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (id_buku, judul, pengarang, penerbit, tahun, stok))
            db.commit()
            return True  # Tambahkan ini agar form_buku tahu proses berhasil
        except Exception as e:
            print(f"Error: {e}")
            db.rollback()
            return False # Tambahkan ini jika terjadi error (misal ID duplikat)
        finally: 
            db.close()

    @staticmethod
    def read_all():
        db = get_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM buku")
        res = cursor.fetchall()
        db.close()
        return res

    @staticmethod
    def update(id_buku, judul, pengarang, penerbit, tahun, stok):
        db = get_connection()
        cursor = db.cursor()
        try:
            query = """
                UPDATE buku 
                SET judul=%s, pengarang=%s, penerbit=%s, tahun_terbit=%s, stok=%s 
                WHERE id_buku=%s
            """
            cursor.execute(query, (judul, pengarang, penerbit, tahun, stok, id_buku))
            db.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            db.rollback()
            return False
        finally: db.close()

    @staticmethod
    def delete(id_buku):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("DELETE FROM buku WHERE id_buku=%s", (id_buku,))
        db.commit()
        db.close()

    @staticmethod
    def search(keyword):
        db = get_connection()
        cursor = db.cursor(dictionary=True)
        query = "SELECT * FROM buku WHERE judul LIKE %s OR pengarang LIKE %s"
        val = (f"%{keyword}%", f"%{keyword}%")
        cursor.execute(query, val)
        res = cursor.fetchall()
        db.close()
        return res