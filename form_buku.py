from PyQt5 import QtWidgets, QtCore, QtGui
from modul.buku import BukuModel

class FormBukuDialog(QtWidgets.QDialog):
    def __init__(self, mode="tambah", data=None):
        super().__init__()
        self.mode = mode
        self.data = data
        self.setWindowTitle("Form Detail Buku - Library Hub")
        self.setFixedSize(500, 800)  # Diperbesar dari 680 ke 800
        
        # Dark theme styling
        self.setStyleSheet("""
            QDialog {
                background: #0a0a0a;
            }
            #headerCard {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #1a1a1a, stop:1 #0f0f0f);
                border-radius: 15px;
                border: 1px solid #2a2a2a;
            }
            #titleLabel {
                color: white;
                font-size: 20px;
                font-weight: bold;
                letter-spacing: 1px;
            }
            #subtitleLabel {
                color: rgba(255, 255, 255, 0.5);
                font-size: 12px;
            }
            QLabel {
                color: rgba(255, 255, 255, 0.7);
                font-size: 13px;
                font-weight: bold;
            }
            QLineEdit, QSpinBox {
                background: #2a2a2a;
                border: 2px solid #3a3a3a;
                border-radius: 8px;
                padding: 12px;
                color: white;
                font-size: 14px;
                min-height: 20px;
            }
            QLineEdit::placeholder {
                color: #888888;
            }
            QLineEdit:focus, QSpinBox:focus {
                border: 2px solid #f97316;
                background: #333333;
            }
            QLineEdit:disabled {
                background: #1a1a1a;
                color: rgba(255, 255, 255, 0.3);
            }
            QSpinBox::up-button, QSpinBox::down-button {
                background: #2a2a2a;
                border: none;
                border-radius: 4px;
                width: 20px;
            }
            QSpinBox::up-button:hover, QSpinBox::down-button:hover {
                background: #3a3a3a;
            }
            QPushButton#btnSave {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #dc2626, stop:1 #f97316);
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 15px;
                font-weight: bold;
                padding: 14px;
                min-height: 20px;
            }
            QPushButton#btnSave:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #ef4444, stop:1 #fb923c);
            }
            QPushButton#btnSave:pressed {
                padding-top: 16px;
                padding-bottom: 12px;
            }
        """)

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(25, 25, 25, 25)
        layout.setSpacing(15)  # Dikurangi dari 18 ke 15

        # Header Card
        header_card = QtWidgets.QFrame()
        header_card.setObjectName("headerCard")
        header_layout = QtWidgets.QVBoxLayout(header_card)
        header_layout.setContentsMargins(20, 15, 20, 15)
        header_layout.setSpacing(5)

        title_container = QtWidgets.QHBoxLayout()
        title_icon = QtWidgets.QLabel("📚")
        title_icon.setStyleSheet("font-size: 24px;")
        
        mode_text = "TAMBAH BUKU" if mode == "tambah" else "EDIT BUKU"
        title_label = QtWidgets.QLabel(mode_text)
        title_label.setObjectName("titleLabel")
        
        title_container.addWidget(title_icon)
        title_container.addWidget(title_label)
        title_container.addStretch()

        subtitle_label = QtWidgets.QLabel("Lengkapi informasi buku dibawah ini")
        subtitle_label.setObjectName("subtitleLabel")

        header_layout.addLayout(title_container)
        header_layout.addWidget(subtitle_label)

        # Shadow for header
        header_shadow = QtWidgets.QGraphicsDropShadowEffect()
        header_shadow.setBlurRadius(20)
        header_shadow.setXOffset(0)
        header_shadow.setYOffset(8)
        header_shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        header_card.setGraphicsEffect(header_shadow)

        layout.addWidget(header_card)

        # Form Fields
        form_layout = QtWidgets.QVBoxLayout()
        form_layout.setSpacing(10)  # Dikurangi dari 12 ke 10

        # ID Buku
        id_label = QtWidgets.QLabel("📋 ID BUKU")
        self.txtId = QtWidgets.QLineEdit()
        self.txtId.setPlaceholderText("Masukkan ID Buku (contoh: BK001)")
        form_layout.addWidget(id_label)
        form_layout.addWidget(self.txtId)

        # Judul
        judul_label = QtWidgets.QLabel("📖 JUDUL BUKU")
        self.txtJudul = QtWidgets.QLineEdit()
        self.txtJudul.setPlaceholderText("Masukkan judul buku")
        form_layout.addWidget(judul_label)
        form_layout.addWidget(self.txtJudul)

        # Pengarang
        pengarang_label = QtWidgets.QLabel("✍️ PENGARANG")
        self.txtPengarang = QtWidgets.QLineEdit()
        self.txtPengarang.setPlaceholderText("Masukkan nama pengarang")
        form_layout.addWidget(pengarang_label)
        form_layout.addWidget(self.txtPengarang)

        # Penerbit
        penerbit_label = QtWidgets.QLabel("🏢 PENERBIT")
        self.txtPenerbit = QtWidgets.QLineEdit()
        self.txtPenerbit.setPlaceholderText("Masukkan nama penerbit")
        form_layout.addWidget(penerbit_label)
        form_layout.addWidget(self.txtPenerbit)

        # Tahun
        tahun_label = QtWidgets.QLabel("📅 TAHUN TERBIT")
        self.txtTahun = QtWidgets.QLineEdit()
        self.txtTahun.setPlaceholderText("Masukkan tahun terbit (contoh: 2024)")
        form_layout.addWidget(tahun_label)
        form_layout.addWidget(self.txtTahun)

        # Stok
        stok_label = QtWidgets.QLabel("📦 STOK BUKU")
        self.txtStok = QtWidgets.QSpinBox()
        self.txtStok.setRange(0, 999)
        self.txtStok.setPrefix("Stok: ")
        self.txtStok.setSuffix(" buku")
        form_layout.addWidget(stok_label)
        form_layout.addWidget(self.txtStok)

        layout.addLayout(form_layout)

        # Fill data if edit mode
        if mode == "edit" and data:
            self.txtId.setText(data['id_buku'])
            self.txtId.setEnabled(False)
            self.txtJudul.setText(data['judul'])
            self.txtPengarang.setText(data['pengarang'])
            self.txtPenerbit.setText(data['penerbit'])
            self.txtTahun.setText(data['tahun'])
            self.txtStok.setValue(int(data['stok']))

        # Save Button
        self.btnSimpan = QtWidgets.QPushButton("💾  SIMPAN DATA")
        self.btnSimpan.setObjectName("btnSave")
        self.btnSimpan.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSimpan.clicked.connect(self.simpan)
        
        layout.addSpacing(10)  # Dikurangi dari 5 ke 10 untuk spacing yang lebih konsisten
        layout.addWidget(self.btnSimpan)

    def simpan(self):
        id_b = self.txtId.text().strip()
        j = self.txtJudul.text().strip()
        p = self.txtPengarang.text().strip()
        pb = self.txtPenerbit.text().strip()
        th = self.txtTahun.text().strip()
        st = self.txtStok.value()

        # Validasi
        if not id_b or not j or not p:
            self.show_warning("Peringatan", "ID Buku, Judul, dan Pengarang tidak boleh kosong!")
            return

        try:
            if self.mode == "tambah":
                success = BukuModel.create(id_b, j, p, pb, th, st)
            else:
                success = BukuModel.update(id_b, j, p, pb, th, st)
            
            print(f"Debug - Mode: {self.mode}, Success: {success}")  # Debug line
            
            if success:
                self.show_success("Berhasil", "Data buku berhasil disimpan!")
                self.accept()
            else:
                self.show_warning("Gagal", "Gagal menyimpan data buku. Silakan coba lagi.")
        except Exception as e:
            print(f"Error saat menyimpan: {e}")  # Debug line
            self.show_warning("Error", f"Terjadi kesalahan: {str(e)}")

    def show_warning(self, title, message):
        msg = QtWidgets.QMessageBox(self)
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setWindowTitle(title)
        msg.setText(message)
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
                    stop:0 #dc2626, stop:1 #f97316);
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 25px;
                font-weight: bold;
                min-width: 80px;
            }
        """)
        msg.exec_()

    def show_success(self, title, message):
        msg = QtWidgets.QMessageBox(self)
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle(title)
        msg.setText(message)
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
                    stop:0 #10b981, stop:1 #059669);
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 25px;
                font-weight: bold;
                min-width: 80px;
            }
        """)
        msg.exec_()