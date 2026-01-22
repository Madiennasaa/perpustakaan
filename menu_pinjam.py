from PyQt5 import QtWidgets, QtCore, QtGui
from modul.pinjam import PinjamModel

class KelolaPinjamWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Loan Management - Library Hub")
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
            QComboBox {
                background: #1a1a1a;
                color: white;
                border: 2px solid #2a2a2a;
                border-radius: 10px;
                padding: 8px 15px;
                font-weight: bold;
                min-width: 160px;
            }
            QComboBox::drop-down { border: none; }
            QComboBox QAbstractItemView {
                background-color: #1a1a1a;
                color: white;
                selection-background-color: #3b82f6;
                outline: none;
            }
            QPushButton#btnValidate {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #10b981, stop:1 #059669);
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 14px;
                font-weight: bold;
                padding: 12px 24px;
            }
            QPushButton#btnValidate:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #34d399, stop:1 #10b981);
            }
            QPushButton#btnReturn {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #3b82f6, stop:1 #2563eb);
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 14px;
                font-weight: bold;
                padding: 12px 24px;
            }
            QPushButton#btnReturn:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #60a5fa, stop:1 #3b82f6);
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
                selection-background-color: rgba(59, 130, 246, 0.3);
                selection-color: white;
            }
            QTableWidget::item {
                padding: 8px;
                border-bottom: 1px solid #2a2a2a;
            }
            QTableWidget::item:selected {
                background: rgba(59, 130, 246, 0.3);
            }
            QHeaderView::section {
                background: #0f0f0f;
                color: rgba(255, 255, 255, 0.7);
                padding: 12px;
                border: none;
                border-bottom: 2px solid #3b82f6;
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
            #statusBadge {
                border-radius: 8px;
                padding: 4px 12px;
                font-size: 11px;
                font-weight: bold;
                letter-spacing: 1px;
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
        title_icon = QtWidgets.QLabel("📋")
        title_icon.setStyleSheet("font-size: 28px;")
        
        title_label = QtWidgets.QLabel("LOAN MANAGEMENT")
        title_label.setObjectName("titleLabel")
        
        title_container.addWidget(title_icon)
        title_container.addWidget(title_label)
        title_container.addStretch()

        subtitle_label = QtWidgets.QLabel("Validasi permintaan & kelola pengembalian buku")
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
        
        # Filter Dropdown
        self.comboFilter = QtWidgets.QComboBox()
        self.comboFilter.addItems(["SEMUA STATUS", "PENDING", "DIPINJAM", "DIKEMBALIKAN"])
        self.comboFilter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboFilter.currentTextChanged.connect(self.load_data) # Otomatis refresh saat diganti

        self.btnValidasi = QtWidgets.QPushButton("✓  APPROVE LOAN")
        self.btnValidasi.setObjectName("btnValidate")
        self.btnValidasi.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnValidasi.clicked.connect(self.validasi_pinjam)

        self.btnKembali = QtWidgets.QPushButton("↩  PROCESS RETURN")
        self.btnKembali.setObjectName("btnReturn")
        self.btnKembali.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnKembali.clicked.connect(self.proses_kembali)

        self.btnRefresh = QtWidgets.QPushButton("🔄  REFRESH")
        self.btnRefresh.setObjectName("btnRefresh")
        self.btnRefresh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnRefresh.clicked.connect(self.load_data)

        hbox.addWidget(self.comboFilter) # Menambahkan filter ke layout
        hbox.addWidget(self.btnValidasi)
        hbox.addWidget(self.btnKembali)
        hbox.addWidget(self.btnRefresh)
        hbox.addStretch()
        
        layout.addLayout(hbox)

        # Table
        self.table = QtWidgets.QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "BORROWER", "BOOK TITLE", "LOAN DATE", "STATUS", "BOOK_ID"])
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table.verticalHeader().setVisible(False)
        self.table.setAlternatingRowColors(False)
        self.table.setShowGrid(True)
        
        # Hide BOOK_ID column
        self.table.setColumnHidden(5, True)
        
        layout.addWidget(self.table)
        
        # Legend & Info
        legend_layout = QtWidgets.QHBoxLayout()
        
        legend_waiting = QtWidgets.QLabel("● MENUNGGU")
        legend_waiting.setStyleSheet("color: #f59e0b; font-size: 12px; font-weight: bold;")
        
        legend_borrowed = QtWidgets.QLabel("● DIPINJAM")
        legend_borrowed.setStyleSheet("color: #3b82f6; font-size: 12px; font-weight: bold;")
        
        legend_returned = QtWidgets.QLabel("● DIKEMBALIKAN")
        legend_returned.setStyleSheet("color: #10b981; font-size: 12px; font-weight: bold;")
        
        info_text = QtWidgets.QLabel("💡 Tip: Pilih baris lalu klik tombol aksi yang sesuai")
        info_text.setStyleSheet("color: rgba(255, 255, 255, 0.4); font-size: 12px;")
        
        legend_layout.addWidget(legend_waiting)
        legend_layout.addSpacing(15)
        legend_layout.addWidget(legend_borrowed)
        legend_layout.addSpacing(15)
        legend_layout.addWidget(legend_returned)
        legend_layout.addStretch()
        legend_layout.addWidget(info_text)
        
        layout.addLayout(legend_layout)
        
        self.load_data()

    def load_data(self):
        # Ambil nilai filter dari dropdown
        filter_text = self.comboFilter.currentText().lower()
        status_filter = None if filter_text == "semua status" else filter_text
        
        # Memanggil search_and_filter dari model asli Anda tanpa merubah base
        data = PinjamModel.search_and_filter(status_filter=status_filter) 
        self.table.setRowCount(0)
        
        for r, row in enumerate(data):
            self.table.insertRow(r)
            
            # ID
            id_item = QtWidgets.QTableWidgetItem(str(row.get('id_peminjaman')))
            id_item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            id_item.setForeground(QtGui.QColor("#f97316"))
            font = id_item.font()
            font.setBold(True)
            id_item.setFont(font)
            self.table.setItem(r, 0, id_item)
            
            # Borrower
            borrower_item = QtWidgets.QTableWidgetItem(str(row.get('username')))
            borrower_item.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            self.table.setItem(r, 1, borrower_item)
            
            # Book Title
            title_item = QtWidgets.QTableWidgetItem(str(row.get('judul')))
            title_item.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            self.table.setItem(r, 2, title_item)
            
            # Date
            date_item = QtWidgets.QTableWidgetItem(str(row.get('tgl_pinjam')))
            date_item.setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
            self.table.setItem(r, 3, date_item)
            
            # Status with custom widget
            status = str(row.get('status')).upper()
            status_widget = self.create_status_badge(status)
            self.table.setCellWidget(r, 4, status_widget)
            
            # Hidden Book ID
            book_id_item = QtWidgets.QTableWidgetItem(str(row.get('id_buku')))
            self.table.setItem(r, 5, book_id_item)
        
        # Update row height
        for row in range(self.table.rowCount()):
            self.table.setRowHeight(row, 55)

    def create_status_badge(self, status):
        """Create colored status badge"""
        container = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(QtCore.Qt.AlignCenter)
        
        # Mapping database status ke display text
        status_map = {
            'pending': 'MENUNGGU',
            'dipinjam': 'DIPINJAM',
            'dikembalikan': 'DIKEMBALIKAN'
        }
        
        display_text = status_map.get(status.lower(), status.upper())
        
        badge = QtWidgets.QLabel(display_text)
        badge.setObjectName("statusBadge")
        badge.setAlignment(QtCore.Qt.AlignCenter)
        
        if display_text == "MENUNGGU":
            badge.setStyleSheet("""
                background: rgba(245, 158, 11, 0.2);
                color: #f59e0b;
                border: 1px solid #f59e0b;
                border-radius: 8px;
                padding: 4px 12px;
                font-size: 11px;
                font-weight: bold;
            """)
        elif status == "DIPINJAM":
            badge.setStyleSheet("""
                background: rgba(59, 130, 246, 0.2);
                color: #3b82f6;
                border: 1px solid #3b82f6;
                border-radius: 8px;
                padding: 4px 12px;
                font-size: 11px;
                font-weight: bold;
            """)
        elif status == "DIKEMBALIKAN":
            badge.setStyleSheet("""
                background: rgba(16, 185, 129, 0.2);
                color: #10b981;
                border: 1px solid #10b981;
                border-radius: 8px;
                padding: 4px 12px;
                font-size: 11px;
                font-weight: bold;
            """)
        
        layout.addWidget(badge)
        return container

    def validasi_pinjam(self):
        row = self.table.currentRow()
        if row < 0:
            self.show_warning("Warning", "Please select a loan request to approve!")
            return
        
        # Get status from badge widget
        status_widget = self.table.cellWidget(row, 4)
        badge = status_widget.findChild(QtWidgets.QLabel)
        status = badge.text().upper()
        
        if status != "MENUNGGU":
            self.show_warning("Invalid Action", "Only 'MENUNGGU' status can be validated!")
            return

        id_p = self.table.item(row, 0).text()
        borrower = self.table.item(row, 1).text()
        
        msg = QtWidgets.QMessageBox(self)
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setWindowTitle("Approve Loan")
        msg.setText(f"Approve loan request for '{borrower}'?")
        msg.setInformativeText(f"Loan ID: {id_p}")
        msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        msg.setDefaultButton(QtWidgets.QMessageBox.Yes)
        msg.setStyleSheet("""
            QMessageBox { background-color: #1a1a1a; }
            QMessageBox QLabel { color: white; font-size: 14px; }
            QPushButton { background: #10b981; color: white; border-radius: 6px; padding: 10px 25px; font-weight: bold; }
            QPushButton[text="No"] { background: #2a2a2a; }
        """)
        
        if msg.exec_() == QtWidgets.QMessageBox.Yes:
            if PinjamModel.validasi_admin(id_p, "Setujui"):
                self.show_success("Success", f"Loan {id_p} has been approved!")
                self.load_data()
            else:
                self.show_warning("Error", "Failed to approve loan request!")

    def proses_kembali(self):
        row = self.table.currentRow()
        if row < 0:
            self.show_warning("Warning", "Please select a loan to process return!")
            return
            
        status_widget = self.table.cellWidget(row, 4)
        badge = status_widget.findChild(QtWidgets.QLabel)
        if badge.text().upper() != "DIPINJAM":
            self.show_warning("Invalid Action", "Only 'DIPINJAM' status can be returned!")
            return
        
        id_p = self.table.item(row, 0).text()
        id_b = self.table.item(row, 5).text()
        book_title = self.table.item(row, 2).text()
        
        msg = QtWidgets.QMessageBox(self)
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setWindowTitle("Process Return")
        msg.setText(f"Process return for this book?")
        msg.setInformativeText(f"Book: {book_title}\nLoan ID: {id_p}")
        msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        msg.setDefaultButton(QtWidgets.QMessageBox.Yes)
        msg.setStyleSheet("""
            QMessageBox { background-color: #1a1a1a; }
            QMessageBox QLabel { color: white; font-size: 14px; }
            QPushButton { background: #3b82f6; color: white; border-radius: 6px; padding: 10px 25px; font-weight: bold; }
            QPushButton[text="No"] { background: #2a2a2a; }
        """)
        
        from datetime import date
        if msg.exec_() == QtWidgets.QMessageBox.Yes:
            if PinjamModel.return_book(id_p, date.today()):
                self.show_success("Success", "Book has been returned to stock!")
                self.load_data()

    def show_warning(self, title, message):
        msg = QtWidgets.QMessageBox(self)
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStyleSheet("QMessageBox { background-color: #1a1a1a; } QMessageBox QLabel { color: white; }")
        msg.exec_()

    def show_success(self, title, message):
        msg = QtWidgets.QMessageBox(self)
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStyleSheet("QMessageBox { background-color: #1a1a1a; } QMessageBox QLabel { color: white; }")
        msg.exec_()