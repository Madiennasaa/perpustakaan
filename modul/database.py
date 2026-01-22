import os
import mysql.connector
from dotenv import load_dotenv

# Load file .env
load_dotenv()

class Database:
    def __init__(self):
        try:
            self.db = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                port=int(os.getenv("DB_PORT")),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASS"),
                database=os.getenv("DB_NAME")
            )
            self.cursor = self.db.cursor()
        except mysql.connector.Error as err:
            print(f"Error Koneksi: {err}")
            self.db = None

# --- INI KUNCI PERBAIKANNYA ---
def get_connection():
    """Fungsi ini agar file lain bisa memanggil modul.database.get_connection"""
    obj_db = Database()
    return obj_db.db