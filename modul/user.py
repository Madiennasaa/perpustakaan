from modul.database import get_connection

class User:
    def __init__(self, username, password, nama, alamat, no_telp, role):
        self.username = username
        self.password = password
        self.nama = nama
        self.alamat = alamat
        self.no_telp = no_telp
        self.role = role

    @staticmethod
    def login(username, password):
        db = get_connection()
        cursor = db.cursor(dictionary=True)
        query = "SELECT * FROM user WHERE username=%s AND password=%s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        db.close()
        return result