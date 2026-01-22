from PyQt5 import QtWidgets, QtCore, QtGui
from modul.pinjam import PinjamModel
from datetime import datetime

class KembaliBukuWindow(QtWidgets.QWidget):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.setWindowTitle("Pengembalian Buku")
        self.resize(1000, 600)
        
        # Modern dark theme
        self.setStyleSheet("""
            QWidget {
                background-color: #0a0a0a;
                color: white;
            }
            #headerLabel {
                color: white;
                font-size: 28px;
                font-weight: bold;
                letter-spacing: 2px;
            }
            #subtitleLabel {
                color: rgba(255, 255, 255, 0.5);
                font-size: 13px;
                letter-spacing: 1px;
            }
            QTableWidget {
                background-color: #1a1a1a;
                color: white;
                border: 2px solid #2a2a2a;
                border-radius: 15px;
                gridline-color: #2a2a2a;
            }
            QTableWidget::item {
                padding: 10px;
                border-bottom: 1px solid #2a2a2a;
            }
            QTableWidget::item:selected {
                background-color: #f97316;
                color: white;
            }
            QHeaderView::section {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #2a2a2a, stop:1 #1a1a1a);
                color: white;
                padding: 12px;
                border: none;
                border-bottom: 2px solid #f97316;
                font-weight: bold;
                font-size: 13px;
                letter-spacing: 1px;
            }
            QPushButton#btnReturn {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #f97316, stop:1 #ea580c);
                color: white;
                border: none;
                border-radius: 8px;
                padding: 10px 25px;
                font-size: 13px;
                font-weight: bold;
                letter-spacing: 1px;
            }
            QPushButton#btnReturn:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #fb923c, stop:1 #f97316);
            }
            QPushButton#btnClose {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #dc2626, stop:1 #b91c1c);
                color: white;
                border: none;
                border-radius: 10px;
                padding: 12px 30px;
                font-size: 14px;
                font-weight: bold;
                letter-spacing: 1px;
            }
            QPushButton#btnClose:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #ef4444, stop:1 #dc2626);
            }
            QPushButton#btnRefresh {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #3b82f6, stop:1 #2563eb);
                color: white;
                border: none;
                border-radius: 10px;
                padding: 12px 30px;
                font-size: 14px;
                font-weight: bold;
                letter-spacing: 1px;
            }
            QPushButton#btnRefresh:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #60a5fa, stop:1 #3b82f6);
            }
            #infoCard {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(249, 115, 22, 0.2), stop:1 rgba(249, 115, 22, 0.05));
                border: 1px solid rgba(249, 115, 22, 0.3);
                border-radius: 12px;
                padding: 15px;
            }
            #infoLabel {
                color: #fb923c;
                font-size: 13px;
            }
        """)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(20)

        # Header
        header_layout = QtWidgets.QVBoxLayout()
        header_layout.setSpacing(8)
        
        title_label = QtWidgets.QLabel("📤 PENGEMBALIAN BUKU")
        title_label.setObjectName("headerLabel")
        
        subtitle_label = QtWidgets.QLabel(f"MEMBER: {username.upper()}")
        subtitle_label.setObjectName("subtitleLabel")
        
        header_layout.addWidget(title_label)
        header_layout.addWidget(subtitle_label)
        
        main_layout.addLayout(header_layout)

        # Info card
        info_card = QtWidgets.QFrame()
        info_card.setObjectName("infoCard")
        info_layout = QtWidgets.QHBoxLayout(info_card)
        
        info_icon = QtWidgets.QLabel("ℹ️")
        info_icon.setStyleSheet("font-size: 24px;")
        
        info_text = QtWidgets.QLabel(
            "Daftar buku yang sedang Anda pinjam. Klik tombol 'Kembalikan' untuk mengembalikan buku."
        )
        info_text.setObjectName("infoLabel")
        info_text.setWordWrap(True)
        
        info_layout.addWidget(info_icon)
        info_layout.addWidget(info_text, 1)
        
        main_layout.addWidget(info_card)

        # Table
        self.table = QtWidgets.QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels([
            "ID PINJAM", 
            "ID BUKU", 
            "JUDUL BUKU", 
            "TGL PINJAM", 
            "AKSI"
        ])
        
        # Set column widths
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Fixed)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Fixed)
        
        self.table.setColumnWidth(0, 120)
        self.table.setColumnWidth(1, 100)
        self.table.setColumnWidth(3, 150)
        self.table.setColumnWidth(4, 150)
        
        # Table settings
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.verticalHeader().setVisible(False)
        self.table.setShowGrid(True)
        
        main_layout.addWidget(self.table)

        # Empty state label (shown when no books borrowed)
        self.empty_label = QtWidgets.QLabel("📚 Anda tidak memiliki buku yang sedang dipinjam")
        self.empty_label.setAlignment(QtCore.Qt.AlignCenter)
        self.empty_label.setStyleSheet("""
            color: rgba(255, 255, 255, 0.5);
            font-size: 16px;
            padding: 40px;
        """)
        self.empty_label.hide()
        main_layout.addWidget(self.empty_label)

        # Button section
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.setSpacing(15)
        
        btn_refresh = QtWidgets.QPushButton("🔄 REFRESH")
        btn_refresh.setObjectName("btnRefresh")
        btn_refresh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btn_refresh.clicked.connect(self.load_data)
        
        btn_close = QtWidgets.QPushButton("TUTUP")
        btn_close.setObjectName("btnClose")
        btn_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btn_close.clicked.connect(self.close)
        
        button_layout.addStretch()
        button_layout.addWidget(btn_refresh)
        button_layout.addWidget(btn_close)
        
        main_layout.addLayout(button_layout)

        # Load data
        self.load_data()

    def load_data(self):
        """Load borrowed books by user (Only with status 'dipinjam')"""
        try:
            # Mengambil data dari model yang filternya sudah status='dipinjam'
            # Data yang dikembalikan model: (id_peminjaman, judul, id_buku, tgl_pinjam)
            data = PinjamModel.get_pinjam_by_user(self.username)
            
            if not data:
                self.table.hide()
                self.empty_label.show()
                # Set row count ke 0 agar data lama tidak nyangkut
                self.table.setRowCount(0)
                return
            
            self.table.show()
            self.empty_label.hide()
            self.table.setRowCount(len(data))
            
            for i, row_data in enumerate(data):
                # Unpack sesuai struktur return tuple dari PinjamModel.get_pinjam_by_user
                # row_data[0] = id_peminjaman
                # row_data[1] = judul
                # row_data[2] = id_buku
                # row_data[3] = tgl_pinjam
                id_pinjam, judul, id_buku, tgl_pinjam = row_data
                
                # Kolom 0: ID Peminjaman
                id_item = QtWidgets.QTableWidgetItem(str(id_pinjam))
                id_item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.table.setItem(i, 0, id_item)
                
                # Kolom 1: ID Buku
                id_buku_item = QtWidgets.QTableWidgetItem(str(id_buku))
                id_buku_item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.table.setItem(i, 1, id_buku_item)
                
                # Kolom 2: Judul Buku
                judul_item = QtWidgets.QTableWidgetItem(str(judul))
                self.table.setItem(i, 2, judul_item)
                
                # Kolom 3: Tanggal Pinjam (Hasil ACC Admin)
                tgl_item = QtWidgets.QTableWidgetItem(str(tgl_pinjam))
                tgl_item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.table.setItem(i, 3, tgl_item)
                
                # Kolom 4: Button Kembalikan
                btn_container = QtWidgets.QWidget()
                btn_layout = QtWidgets.QHBoxLayout(btn_container)
                btn_layout.setContentsMargins(5, 5, 5, 5)
                btn_layout.setAlignment(QtCore.Qt.AlignCenter)
                
                btn = QtWidgets.QPushButton("📤 Kembalikan")
                btn.setObjectName("btnReturn")
                btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                
                # Hubungkan ke fungsi proses_kembali
                btn.clicked.connect(lambda checked, idp=id_pinjam, title=judul: self.proses_kembali(idp, title))
                
                btn_layout.addWidget(btn)
                self.table.setCellWidget(i, 4, btn_container)
                
                # Set row height agar rapi
                self.table.setRowHeight(i, 60)
                
        except Exception as e:
            print(f"Error load_data: {e}") # Debugging di terminal
            QtWidgets.QMessageBox.critical(self, "Error", f"Gagal memuat data: {str(e)}")

    def proses_kembali(self, id_pinjam, judul):
        """Process book return"""
        # Confirmation dialog
        msg = QtWidgets.QMessageBox(self)
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setWindowTitle("Konfirmasi Pengembalian")
        msg.setText(f"Apakah Anda yakin ingin mengembalikan buku:\n\n'{judul}'?")
        msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        msg.setDefaultButton(QtWidgets.QMessageBox.Yes)
        msg.setStyleSheet("""
            QMessageBox {
                background-color: #1a1a1a;
            }
            QMessageBox QLabel {
                color: white;
                font-size: 14px;
            }
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #f97316, stop:1 #ea580c);
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 25px;
                font-weight: bold;
                min-width: 80px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #fb923c, stop:1 #f97316);
            }
            QPushButton[text="No"] {
                background: #2a2a2a;
            }
            QPushButton[text="No"]:hover {
                background: #3a3a3a;
            }
        """)
        
        if msg.exec_() != QtWidgets.QMessageBox.Yes:
            return
        
        # Process return
        tgl_skrg = datetime.now().strftime('%Y-%m-%d')
        
        try:
            if PinjamModel.return_book(id_pinjam, tgl_skrg):
                QtWidgets.QMessageBox.information(
                    self, 
                    "Berhasil", 
                    f"Buku '{judul}' telah berhasil dikembalikan!\n\nTanggal kembali: {tgl_skrg}\n\nTerima kasih telah mengembalikan tepat waktu."
                )
                self.load_data()
            else:
                QtWidgets.QMessageBox.warning(
                    self, 
                    "Gagal", 
                    "Pengembalian gagal! Silakan coba lagi atau hubungi petugas perpustakaan."
                )
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Terjadi kesalahan: {str(e)}")