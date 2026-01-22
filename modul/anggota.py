from modul.user import User
from modul.database import get_connection

class Anggota(User):
    def __init__(self, username, nama, alamat, no_telp, nim, tgl_daftar):
        super().__init__(username, None, nama, alamat, no_telp, 'anggota')
        self.nim = nim
        self.tgl_daftar = tgl_daftar

    @staticmethod
    def create(username, password, nama, alamat, no_telp, nim, tgl_daftar):
        db = get_connection()
        cursor = db.cursor()
        try:
            cursor.execute("INSERT INTO user VALUES (%s, %s, %s, %s, %s, 'anggota')", 
                           (username, password, nama, alamat, no_telp))
            cursor.execute("INSERT INTO anggota VALUES (%s, %s, %s)", 
                           (nim, username, tgl_daftar))
            db.commit()
            return True
        except:
            db.rollback()
            return False
        finally: db.close()

    @staticmethod
    def read_all():
        db = get_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT u.*, a.nim, a.tanggal_daftar FROM user u JOIN anggota a ON u.username = a.username")
        res = cursor.fetchall()
        db.close()
        return res

    @staticmethod
    def update(username, password, nama, alamat, no_telp, nim):
        db = get_connection()
        cursor = db.cursor()
        try:
            # Jika password diisi, update password. Jika kosong, biarkan yang lama.
            if password and password.strip() != "":
                query_user = "UPDATE user SET password=%s, nama=%s, alamat=%s, no_telp=%s WHERE username=%s"
                val_user = (password, nama, alamat, no_telp, username)
            else:
                query_user = "UPDATE user SET nama=%s, alamat=%s, no_telp=%s WHERE username=%s"
                val_user = (nama, alamat, no_telp, username)
            
            cursor.execute(query_user, val_user)
            
            # Update data di tabel anggota (NIM)
            query_agt = "UPDATE anggota SET nim=%s WHERE username=%s"
            cursor.execute(query_agt, (nim, username))
            
            db.commit()
            return True
        except Exception as e:
            print(f"Error update user: {e}")
            db.rollback()
            return False
        finally: 
            db.close()

    @staticmethod
    def delete(username):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("DELETE FROM user WHERE username=%s", (username,))
        db.commit()
        db.close()

    @staticmethod
    def search(keyword):
        db = get_connection()
        cursor = db.cursor(dictionary=True)
        query = """
            SELECT u.*, a.nim, a.tanggal_daftar 
            FROM user u 
            JOIN anggota a ON u.username = a.username
            WHERE u.nama LIKE %s OR a.nim LIKE %s
        """
        val = (f"%{keyword}%", f"%{keyword}%")
        cursor.execute(query, val)
        res = cursor.fetchall()
        db.close()
        return res