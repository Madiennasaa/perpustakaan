from PyQt5 import QtWidgets, QtCore, QtGui
from modul.buku import BukuModel
from form_buku import FormBukuDialog

class KelolaBukuWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Book Management - Library Hub")
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
                border: 2px solid #f97316;
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
                selection-background-color: rgba(249, 115, 22, 0.3);
                selection-color: white;
            }
            QTableWidget::item {
                padding: 8px;
                border-bottom: 1px solid #2a2a2a;
            }
            QTableWidget::item:selected {
                background: rgba(249, 115, 22, 0.3);
            }
            QHeaderView::section {
                background: #0f0f0f;
                color: rgba(255, 255, 255, 0.7);
                padding: 12px;
                border: none;
                border-bottom: 2px solid #f97316;
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
        title_icon = QtWidgets.QLabel("📚")
        title_icon.setStyleSheet("font-size: 28px;")
        
        title_label = QtWidgets.QLabel("BOOK MANAGEMENT")
        title_label.setObjectName("titleLabel")
        
        title_container.addWidget(title_icon)
        title_container.addWidget(title_label)
        title_container.addStretch()

        subtitle_label = QtWidgets.QLabel("Kelola koleksi buku perpustakaan")
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
        hbox = QtWidgets.QHBoxLayout()
        hbox.setSpacing(15)
        
        self.btnTambah = QtWidgets.QPushButton("+  ADD BOOK")
        self.btnTambah.setObjectName("btnAction")
        
        self.btnEdit = QtWidgets.QPushButton("✎  EDIT BOOK")
        self.btnEdit.setObjectName("btnAction")
        
        self.btnHapus = QtWidgets.QPushButton("🗑  DELETE BOOK")
        self.btnHapus.setObjectName("btnDelete")

        self.btnRefresh = QtWidgets.QPushButton("🔄  REFRESH")
        self.btnRefresh.setObjectName("btnRefresh")
        
        self.btnTambah.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnEdit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnHapus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnRefresh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        hbox.addWidget(self.btnTambah)
        hbox.addWidget(self.btnEdit)
        hbox.addWidget(self.btnHapus)
        hbox.addWidget(self.btnRefresh)
        hbox.addStretch()
        
        layout.addLayout(hbox)

        # Table
        self.table = QtWidgets.QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID BUKU", "JUDUL", "PENGARANG", "PENERBIT", "TAHUN", "STOK"])
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table.verticalHeader().setVisible(False)
        self.table.setAlternatingRowColors(False)
        self.table.setShowGrid(True)
        
        layout.addWidget(self.table)
        
        # Info Label
        info_label = QtWidgets.QLabel("💡 Tip: Double-click pada baris untuk quick edit")
        info_label.setStyleSheet("""
            color: rgba(255, 255, 255, 0.4);
            font-size: 12px;
            padding: 10px;
        """)
        layout.addWidget(info_label)
        
        # Koneksi Tombol
        self.btnTambah.clicked.connect(self.buka_tambah)
        self.btnEdit.clicked.connect(self.buka_edit)
        self.btnHapus.clicked.connect(self.hapus_buku)
        self.btnRefresh.clicked.connect(self.load_data)
        
        # Double click to edit
        self.table.doubleClicked.connect(self.buka_edit)
        
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
        data = BukuModel.read_all()
        self.table.setRowCount(0)
        for r, row in enumerate(data):
            self.table.insertRow(r)
            
            items_data = [
                ('id_buku', 0, "#f97316", True),
                ('judul', 1, None, False),
                ('pengarang', 2, None, False),
                ('penerbit', 3, None, False),
                ('tahun_terbit', 4, None, False),
                ('stok', 5, "#10b981", True)
            ]
            
            for key, col, color, bold in items_data:
                value = str(row.get(key, '-'))
                item = QtWidgets.QTableWidgetItem(value)
                item.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                
                if color:
                    item.setForeground(QtGui.QColor(color))
                if bold:
                    font = item.font()
                    font.setBold(True)
                    item.setFont(font)
                
                self.table.setItem(r, col, item)
        
        # Update row height for better readability
        for row in range(self.table.rowCount()):
            self.table.setRowHeight(row, 50)

    def buka_edit(self):
        row = self.table.currentRow()
        if row < 0:
            self.show_warning("Warning", "Please select a book to edit!")
            return
        
        data_pilih = {
            "id_buku": self.table.item(row, 0).text(),
            "judul": self.table.item(row, 1).text(),
            "pengarang": self.table.item(row, 2).text(),
            "penerbit": self.table.item(row, 3).text(),
            "tahun": self.table.item(row, 4).text(),
            "stok": self.table.item(row, 5).text()
        }
        
        dialog = FormBukuDialog(mode="edit", data=data_pilih)
        if dialog.exec_(): 
            self.load_data()

    def buka_tambah(self):
        if FormBukuDialog(mode="tambah").exec_(): 
            self.load_data()

    def hapus_buku(self):
        row = self.table.currentRow()
        if row < 0:
            self.show_warning("Warning", "Please select a book to delete!")
            return
            
        id_b = self.table.item(row, 0).text()
        judul = self.table.item(row, 1).text()
        
        msg = QtWidgets.QMessageBox(self)
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setWindowTitle("Confirm Delete")
        msg.setText(f"Are you sure you want to delete this book?")
        msg.setInformativeText(f"ID: {id_b}\nTitle: {judul}\n\nThis action cannot be undone.")
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
            if BukuModel.delete(id_b): 
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