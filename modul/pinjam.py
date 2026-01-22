from modul.database import get_connection
from datetime import date

class PinjamModel:
    @staticmethod
    def create_pinjam(username, id_buku, tgl_pinjam):
        """Tahap 1: User mengajukan pinjaman (Status: Pending). Stok BELUM berkurang."""
        db = get_connection()
        cursor = db.cursor()
        try:
            # 1. Cari NIM anggota berdasarkan username
            cursor.execute("SELECT nim FROM anggota WHERE username = %s", (username,))
            res = cursor.fetchone()
            if not res: return False
            nim = res[0]

            # 2. Input peminjaman dengan status 'pending'
            query = "INSERT INTO pinjam (nim, id_buku, tgl_pinjam, status) VALUES (%s, %s, %s, 'pending')"
            cursor.execute(query, (nim, id_buku, tgl_pinjam))
            
            db.commit()
            return True
        except Exception as e:
            print(f"Error create_pinjam: {e}")
            db.rollback()
            return False
        finally: db.close()

    @staticmethod
    def validasi_admin(id_peminjaman, aksi):
        """Tahap 2: Admin ACC/Tolak. Jika ACC, status jadi 'dipinjam' & STOK BERKURANG."""
        db = get_connection()
        cursor = db.cursor()
        try:
            if aksi == "Setujui":
                # 1. Ambil ID buku terkait peminjaman ini
                cursor.execute("SELECT id_buku FROM pinjam WHERE id_peminjaman = %s", (id_peminjaman,))
                res = cursor.fetchone()
                if not res: return False
                id_buku = res[0]

                # 2. Cek stok buku terlebih dahulu [Optimasi]
                cursor.execute("SELECT stok FROM buku WHERE id_buku = %s", (id_buku,))
                stok = cursor.fetchone()[0]

                if stok > 0:
                    # 3. Update status & kurangi stok hanya jika stok tersedia
                    cursor.execute("UPDATE pinjam SET status = 'dipinjam' WHERE id_peminjaman = %s", (id_peminjaman,))
                    cursor.execute("UPDATE buku SET stok = stok - 1 WHERE id_buku = %s", (id_buku,))
                else:
                    # Jika stok 0, Anda bisa mengganti status menjadi 'ditolak' atau mengembalikan pesan error
                    print("Gagal: Stok buku sudah habis.")
                    return False 
            else:
                # Jika aksi adalah 'Tolak'
                cursor.execute("UPDATE pinjam SET status = 'ditolak' WHERE id_peminjaman = %s", (id_peminjaman,))
            
            db.commit()
            return True
        except Exception as e:
            print(f"Error validasi: {e}")
            db.rollback()
            return False
        finally: 
            db.close()

    @staticmethod
    def return_book(id_peminjaman, tgl_kembali):
        """Tahap 3: Buku dikembalikan. Status jadi 'dikembalikan' & STOK BERTAMBAH."""
        db = get_connection()
        cursor = db.cursor()
        try:
            # Ambil ID buku untuk nambah stok
            cursor.execute("SELECT id_buku FROM pinjam WHERE id_peminjaman = %s", (id_peminjaman,))
            id_buku = cursor.fetchone()[0]

            query = "UPDATE pinjam SET tgl_kembali=%s, status='dikembalikan' WHERE id_peminjaman=%s"
            cursor.execute(query, (tgl_kembali, id_peminjaman))
            
            cursor.execute("UPDATE buku SET stok = stok + 1 WHERE id_buku = %s", (id_buku,))
            db.commit()
            return True
        except Exception as e:
            print(f"Error return_book: {e}")
            db.rollback()
            return False
        finally: db.close()

    @staticmethod
    def get_pending_requests():
        """Admin: Mengambil semua yang statusnya 'pending'"""
        db = get_connection()
        cursor = db.cursor(dictionary=True)
        query = """
            SELECT p.id_peminjaman, u.username, b.judul, p.tgl_pinjam 
            FROM pinjam p
            JOIN anggota a ON p.nim = a.nim
            JOIN user u ON a.username = u.username
            JOIN buku b ON p.id_buku = b.id_buku
            WHERE p.status = 'pending'
        """
        cursor.execute(query)
        res = cursor.fetchall()
        db.close()
        return res

    @staticmethod
    def get_pinjam_by_user(username):
        """User: Mengambil buku yang sedang dibawa (Status: dipinjam)"""
        db = get_connection()
        cursor = db.cursor()
        query = """
            SELECT p.id_peminjaman, b.judul, p.id_buku, p.tgl_pinjam 
            FROM pinjam p
            JOIN anggota a ON p.nim = a.nim
            JOIN buku b ON p.id_buku = b.id_buku
            WHERE a.username = %s AND p.status = 'dipinjam'
        """
        cursor.execute(query, (username,))
        res = cursor.fetchall()
        db.close()
        return res

    @staticmethod
    def search_and_filter(keyword=None, status_filter=None):
        """Riwayat Global untuk Admin"""
        db = get_connection()
        cursor = db.cursor(dictionary=True)
        query = """
            SELECT p.*, u.username, b.judul 
            FROM pinjam p
            JOIN anggota a ON p.nim = a.nim
            JOIN user u ON a.username = u.username
            JOIN buku b ON p.id_buku = b.id_buku
            WHERE 1=1
        """
        params = []
        if keyword:
            query += " AND (u.username LIKE %s OR b.judul LIKE %s)"
            params.extend([f"%{keyword}%", f"%{keyword}%"])
        if status_filter:
            query += " AND p.status = %s"
            params.append(status_filter)

        cursor.execute(query, tuple(params))
        res = cursor.fetchall()
        db.close()
        return res