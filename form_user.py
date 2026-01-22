from PyQt5 import QtWidgets, QtCore, QtGui
from modul.anggota import Anggota

class FormUserDialog(QtWidgets.QDialog):
    def __init__(self, mode="tambah", data=None):
        super().__init__()
        self.mode = mode
        self.data = data
        self.setWindowTitle("Form Detail User - Library Hub")
        self.setFixedSize(500, 750)
        
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
            QLineEdit {
                background: #2a2a2a;
                border: 2px solid #3a3a3a;
                border-radius: 8px;
                padding: 12px;
                color: white;
                font-size: 14px;
            }
            QLineEdit::placeholder {
                color: #888888;
            }
            QLineEdit:focus {
                border: 2px solid #f97316;
                background: #333333;
            }
            QLineEdit:disabled {
                background: #1a1a1a;
                color: rgba(255, 255, 255, 0.3);
            }
            QPushButton#btnShowPass {
                background: #2a2a2a;
                border: 2px solid #2a2a2a;
                border-radius: 8px;
                font-size: 16px;
                padding: 8px;
            }
            QPushButton#btnShowPass:hover {
                background: #3a3a3a;
                border: 2px solid #f97316;
            }
            QPushButton#btnShowPass:checked {
                background: #f97316;
                border: 2px solid #f97316;
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
        layout.setSpacing(18)

        # Header Card
        header_card = QtWidgets.QFrame()
        header_card.setObjectName("headerCard")
        header_layout = QtWidgets.QVBoxLayout(header_card)
        header_layout.setContentsMargins(20, 15, 20, 15)
        header_layout.setSpacing(5)

        title_container = QtWidgets.QHBoxLayout()
        title_icon = QtWidgets.QLabel("👤")
        title_icon.setStyleSheet("font-size: 24px;")
        
        mode_text = "TAMBAH USER" if mode == "tambah" else "EDIT USER"
        title_label = QtWidgets.QLabel(mode_text)
        title_label.setObjectName("titleLabel")
        
        title_container.addWidget(title_icon)
        title_container.addWidget(title_label)
        title_container.addStretch()

        subtitle_label = QtWidgets.QLabel("Lengkapi informasi user dibawah ini")
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
        form_layout.setSpacing(12)

        # Username
        user_label = QtWidgets.QLabel("🔑 USERNAME")
        self.txtUser = QtWidgets.QLineEdit()
        self.txtUser.setPlaceholderText("Masukkan username")
        form_layout.addWidget(user_label)
        form_layout.addWidget(self.txtUser)

        # Password dengan tombol intip
        pass_label = QtWidgets.QLabel("🔒 PASSWORD")
        self.passLayout = QtWidgets.QHBoxLayout()
        self.passLayout.setSpacing(10)
        
        self.txtPass = QtWidgets.QLineEdit()
        self.txtPass.setPlaceholderText("Masukkan password")
        self.txtPass.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.btnShowPass = QtWidgets.QPushButton("👁️")
        self.btnShowPass.setObjectName("btnShowPass")
        self.btnShowPass.setFixedSize(45, 45)
        self.btnShowPass.setCheckable(True)
        self.btnShowPass.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnShowPass.clicked.connect(self.toggle_password)
        
        self.passLayout.addWidget(self.txtPass)
        self.passLayout.addWidget(self.btnShowPass)
        
        form_layout.addWidget(pass_label)
        form_layout.addLayout(self.passLayout)

        # Nama Lengkap
        nama_label = QtWidgets.QLabel("👨 NAMA LENGKAP")
        self.txtNama = QtWidgets.QLineEdit()
        self.txtNama.setPlaceholderText("Masukkan nama lengkap")
        form_layout.addWidget(nama_label)
        form_layout.addWidget(self.txtNama)

        # NIM
        nim_label = QtWidgets.QLabel("🎓 NIM")
        self.txtNim = QtWidgets.QLineEdit()
        self.txtNim.setPlaceholderText("Masukkan NIM")
        form_layout.addWidget(nim_label)
        form_layout.addWidget(self.txtNim)

        # Alamat
        alamat_label = QtWidgets.QLabel("🏠 ALAMAT LENGKAP")
        self.txtAlamat = QtWidgets.QLineEdit()
        self.txtAlamat.setPlaceholderText("Masukkan alamat lengkap")
        form_layout.addWidget(alamat_label)
        form_layout.addWidget(self.txtAlamat)

        # Telepon
        telp_label = QtWidgets.QLabel("📱 NO. TELEPON")
        self.txtTelp = QtWidgets.QLineEdit()
        self.txtTelp.setPlaceholderText("Masukkan nomor telepon")
        form_layout.addWidget(telp_label)
        form_layout.addWidget(self.txtTelp)

        layout.addLayout(form_layout)

        # Fill data if edit mode
        if mode == "edit" and data:
            self.txtUser.setText(data.get('username', ''))
            self.txtUser.setEnabled(False)
            self.txtNama.setText(data.get('nama', ''))
            self.txtNim.setText(data.get('nim', ''))
            self.txtAlamat.setText(data.get('alamat', ''))
            self.txtTelp.setText(data.get('no_telp', ''))
            
            if 'password' in data:
                self.txtPass.setText(data['password'])

        # Save Button
        self.btnSimpan = QtWidgets.QPushButton("💾  SIMPAN DATA")
        self.btnSimpan.setObjectName("btnSave")
        self.btnSimpan.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSimpan.clicked.connect(self.simpan)
        
        layout.addSpacing(5)
        layout.addWidget(self.btnSimpan)

    def toggle_password(self):
        """Fungsi untuk mengintip password"""
        if self.btnShowPass.isChecked():
            self.txtPass.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.btnShowPass.setText("🙈")
        else:
            self.txtPass.setEchoMode(QtWidgets.QLineEdit.Password)
            self.btnShowPass.setText("👁️")

    def simpan(self):
        u = self.txtUser.text().strip()
        p = self.txtPass.text().strip()
        n = self.txtNama.text().strip()
        nim = self.txtNim.text().strip()
        alm = self.txtAlamat.text().strip()
        tlp = self.txtTelp.text().strip()

        if not u or not p or not n:
            self.show_warning("Peringatan", "Username, Password, dan Nama tidak boleh kosong!")
            return

        try:
            if self.mode == "tambah":
                res = Anggota.create(u, p, n, alm, tlp, nim, "2026-01-21")
            else:
                res = Anggota.update(u, p, n, alm, tlp, nim)
            
            print(f"Debug - Mode: {self.mode}, Result: {res}")  # Debug line
            
            if res:
                self.show_success("Berhasil", "Data User Tersimpan")
                self.accept()
            else:
                self.show_warning("Gagal", "Gagal menyimpan data user. Silakan coba lagi.")
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