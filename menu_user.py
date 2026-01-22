from PyQt5 import QtWidgets, QtCore, QtGui
from modul.anggota import Anggota
from form_user import FormUserDialog
from modul.database import get_connection

class KelolaUserWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User Management - Library Hub")
        self.resize(1100, 650)
        
        # Dark theme matching dashboard
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
                font-size: 24px;
                font-weight: bold;
                letter-spacing: 1px;
            }
            #subtitleLabel {
                color: rgba(255, 255, 255, 0.5);
                font-size: 13px;
            }
            QPushButton#btnAction {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #1a1a1a, stop:1 #0f0f0f);
                color: white;
                border: 2px solid #2a2a2a;
                border-radius: 10px;
                font-size: 14px;
                font-weight: bold;
                padding: 12px 24px;
            }
            QPushButton#btnAction:hover {
                border: 2px solid #dc2626;
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #252525, stop:1 #1a1a1a);
            }
            QPushButton#btnDelete {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #dc2626, stop:1 #f97316);
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 14px;
                font-weight: bold;
                padding: 12px 24px;
            }
            QPushButton#btnDelete:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #ef4444, stop:1 #fb923c);
            }
            QPushButton#btnRefresh {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #1a1a1a, stop:1 #0f0f0f);
                color: white;
                border: 2px solid #2a2a2a;
                border-radius: 10px;
                font-size: 14px;
                font-weight: bold;
                padding: 12px 24px;
            }
            QPushButton#btnRefresh:hover {
                border: 2px solid #8b5cf6;
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #252525, stop:1 #1a1a1a);
            }
            QTableWidget {
                background: #1a1a1a;
                border: 1px solid #2a2a2a;
                border-radius: 12px;
                color: white;
                gridline-color: #2a2a2a;
                selection-background-color: rgba(220, 38, 38, 0.3);
                selection-color: white;
            }
            QTableWidget::item {
                padding: 8px;
                border-bottom: 1px solid #2a2a2a;
            }
            QTableWidget::item:selected {
                background: rgba(220, 38, 38, 0.3);
            }
            QHeaderView::section {
                background: #0f0f0f;
                color: rgba(255, 255, 255, 0.7);
                padding: 12px;
                border: none;
                border-bottom: 2px solid #dc2626;
                font-weight: bold;
                font-size: 13px;
                letter-spacing: 1px;
            }
            QScrollBar:vertical {
                background: #1a1a1a;
                width: 12px;
                border-radius: 6px;
            }
            QScrollBar::handle:vertical {
                background: #2a2a2a;
                border-radius: 6px;
            }
            QScrollBar::handle:vertical:hover {
                background: #3a3a3a;
            }
        """)

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)

        # Header Card
        header_card = QtWidgets.QFrame()
        header_card.setObjectName("headerCard")
        header_layout = QtWidgets.QVBoxLayout(header_card)
        header_layout.setContentsMargins(25, 20, 25, 20)
        header_layout.setSpacing(8)

        title_container = QtWidgets.QHBoxLayout()
        title_icon = QtWidgets.QLabel("👥")
        title_icon.setStyleSheet("font-size: 28px;")
        
        title_label = QtWidgets.QLabel("USER MANAGEMENT")
        title_label.setObjectName("titleLabel")
        
        title_container.addWidget(title_icon)
        title_container.addWidget(title_label)
        title_container.addStretch()

        subtitle_label = QtWidgets.QLabel("Kelola data anggota perpustakaan")
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

        # Action Buttons
        btns = QtWidgets.QHBoxLayout()
        btns.setSpacing(15)
        
        self.btnTambah = QtWidgets.QPushButton("+  ADD USER")
        self.btnTambah.setObjectName("btnAction")
        
        self.btnEdit = QtWidgets.QPushButton("✎  EDIT USER")
        self.btnEdit.setObjectName("btnAction")
        
        self.btnHapus = QtWidgets.QPushButton("🗑  DELETE USER")
        self.btnHapus.setObjectName("btnDelete")

        self.btnRefresh = QtWidgets.QPushButton("🔄  REFRESH")
        self.btnRefresh.setObjectName("btnRefresh")
        
        self.btnTambah.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnEdit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnHapus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnRefresh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        self.btnTambah.clicked.connect(self.tambah)
        self.btnEdit.clicked.connect(self.edit)
        self.btnHapus.clicked.connect(self.hapus)
        self.btnRefresh.clicked.connect(self.load_data)
        
        btns.addWidget(self.btnTambah)
        btns.addWidget(self.btnEdit)
        btns.addWidget(self.btnHapus)
        btns.addWidget(self.btnRefresh)
        btns.addStretch()
        
        layout.addLayout(btns)

        # Table
        self.table = QtWidgets.QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["USERNAME", "NAMA LENGKAP", "NIM", "ALAMAT", "NO. TELP"])
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table.verticalHeader().setVisible(False)
        self.table.setAlternatingRowColors(False)
        self.table.setShowGrid(True)
        
        layout.addWidget(self.table)
        
        # Info Label
        info_label = QtWidgets.QLabel("💡 Tip: Klik baris untuk memilih user, lalu gunakan tombol Edit atau Delete")
        info_label.setStyleSheet("""
            color: rgba(255, 255, 255, 0.4);
            font-size: 12px;
            padding: 10px;
        """)
        layout.addWidget(info_label)
        
        self.load_data()

    def create_icon(self, text, color):
        """Create colored icon from text"""
        pixmap = QtGui.QPixmap(20, 20)
        pixmap.fill(QtCore.Qt.transparent)
        painter = QtGui.QPainter(pixmap)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setPen(QtGui.QColor(color))
        painter.setFont(QtGui.QFont("Segoe UI", 14, QtGui.QFont.Bold))
        painter.drawText(pixmap.rect(), QtCore.Qt.AlignCenter, text)
        painter.end()
        return QtGui.QIcon(pixmap)

    def load_data(self):
        data = Anggota.read_all()
        self.table.setRowCount(0)
        for r, row in enumerate(data):
            self.table.insertRow(r)
            
            # Add items with custom styling
            for col, key in enumerate(['username', 'nama', 'nim', 'alamat', 'no_telp']):
                item = QtWidgets.QTableWidgetItem(str(row[key]))
                item.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                
                # Highlight username column
                if col == 0:
                    item.setForeground(QtGui.QColor("#f97316"))
                    font = item.font()
                    font.setBold(True)
                    item.setFont(font)
                
                self.table.setItem(r, col, item)
        
        # Update row height for better readability
        for row in range(self.table.rowCount()):
            self.table.setRowHeight(row, 50)

    def get_password_from_db(self, username):
        db = get_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT password FROM user WHERE username = %s", (username,))
        result = cursor.fetchone()
        db.close()
        return result['password'] if result else ""

    def edit(self):
        row = self.table.currentRow()
        if row < 0:
            self.show_warning("Warning", "Please select a user to edit!")
            return
            
        username = self.table.item(row, 0).text()
        pw_lama = self.get_password_from_db(username)
        
        data_pilih = {
            "username": username,
            "nama": self.table.item(row, 1).text(),
            "nim": self.table.item(row, 2).text(),
            "alamat": self.table.item(row, 3).text(),
            "no_telp": self.table.item(row, 4).text(),
            "password": pw_lama
        }
        
        dial = FormUserDialog(mode="edit", data=data_pilih)
        if dial.exec_(): 
            self.load_data()

    def tambah(self):
        if FormUserDialog(mode="tambah").exec_(): 
            self.load_data()

    def hapus(self):
        row = self.table.currentRow()
        if row < 0:
            self.show_warning("Warning", "Please select a user to delete!")
            return
            
        u = self.table.item(row, 0).text()
        
        msg = QtWidgets.QMessageBox(self)
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setWindowTitle("Confirm Delete")
        msg.setText(f"Are you sure you want to delete user '{u}'?")
        msg.setInformativeText("This action cannot be undone.")
        msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        msg.setDefaultButton(QtWidgets.QMessageBox.No)
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
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #ef4444, stop:1 #fb923c);
            }
            QPushButton[text="No"] {
                background: #2a2a2a;
            }
            QPushButton[text="No"]:hover {
                background: #3a3a3a;
            }
        """)
        
        if msg.exec_() == QtWidgets.QMessageBox.Yes:
            if Anggota.delete(u):
                self.load_data()

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