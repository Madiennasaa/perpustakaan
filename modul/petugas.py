from modul.user import User

class Petugas(User):
    def __init__(self, username, nama, alamat, no_telp, id_petugas):
        super().__init__(username, None, nama, alamat, no_telp, 'petugas')
        self.id_petugas = id_petugas