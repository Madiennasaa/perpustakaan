import os
import mysql.connector
from dotenv import load_dotenv

class Database:
    def __init__(self):
        load_dotenv()  # load file .env

        try:
            self.db = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                port=int(os.getenv("DB_PORT")),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASS"),
                database=os.getenv("DB_NAME")
            )
            self.cursor = self.db.cursor()
            print("Koneksi Cloud Berhasil!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
