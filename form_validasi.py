from PyQt5 import QtWidgets, QtCore, QtGui
from modul.pinjam import PinjamModel

class AdminValidasiWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Persetujuan Peminjaman")
        self.resize(900, 600)
        self.setStyleSheet("background-color: #0a0a0a; color: white;")
        
        layout = QtWidgets.QVBoxLayout(self)
        
        # Header
        header = QtWidgets.QLabel("DAFTAR PERMINTAAN PINJAM")
        header.setStyleSheet("font-size: 24px; font-weight: bold; color: #f97316; margin: 10px 0;")
        layout.addWidget(header)
        
        # Table
        self.table = QtWidgets.QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Username", "Buku", "Tgl Pinjam", "Aksi"])
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table.setStyleSheet("""
            QTableWidget { background-color: #1a1a1a; border: 1px solid #2a2a2a; gridline-color: #333; }
            QHeaderView::section { background-color: #222; color: white; padding: 5px; }
        """)
        layout.addWidget(self.table)
        
        self.load_data()
    
    def load_data(self):
        data = PinjamModel.get_pending_requests()
        self.table.setRowCount(len(data))
        for row, item in enumerate(data):
            self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(str(item['id_peminjaman'])))
            self.table.setItem(row, 1, QtWidgets.QTableWidgetItem(item['username']))
            self.table.setItem(row, 2, QtWidgets.QTableWidgetItem(item['judul']))
            self.table.setItem(row, 3, QtWidgets.QTableWidgetItem(str(item['tgl_pinjam'])))
            
            # Action Buttons
            btn_widget = QtWidgets.QWidget()
            btn_layout = QtWidgets.QHBoxLayout(btn_widget)
            btn_layout.setContentsMargins(5, 2, 5, 2)
            
            btn_acc = QtWidgets.QPushButton("Setujui")
            btn_acc.setStyleSheet("background-color: #10b981; font-weight: bold; border-radius: 4px; padding: 5px;")
            btn_acc.clicked.connect(lambda _, r=item['id_peminjaman']: self.proses(r, "Setujui"))
            
            btn_tolak = QtWidgets.QPushButton("Tolak")
            btn_tolak.setStyleSheet("background-color: #dc2626; font-weight: bold; border-radius: 4px; padding: 5px;")
            btn_tolak.clicked.connect(lambda _, r=item['id_peminjaman']: self.proses(r, "Tolak"))
            
            btn_layout.addWidget(btn_acc)
            btn_layout.addWidget(btn_tolak)
            self.table.setCellWidget(row, 4, btn_widget)

    def proses(self, id_pinjam, aksi):
        if PinjamModel.validasi_admin(id_pinjam, aksi):
            QtWidgets.QMessageBox.information(self, "Berhasil", f"Peminjaman telah di-{aksi}!")
            self.load_data()