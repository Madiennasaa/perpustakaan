from PyQt5 import QtWidgets, QtCore, QtGui
from modul.pinjam import PinjamModel
from modul.buku import BukuModel
from datetime import datetime

class PinjamBukuWindow(QtWidgets.QWidget):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.setWindowTitle("Pinjam Buku")
        self.resize(1000, 650)
        
        # Modern dark theme - Optimized heights
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
            #searchBox {
                background-color: #1a1a1a;
                color: white;
                border: 2px solid #2a2a2a;
                border-radius: 12px;
                padding: 10px 20px;
                font-size: 14px;
            }
            #searchBox:focus {
                border: 2px solid #10b981;
                background-color: #1e1e1e;
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
                background-color: #10b981;
                color: white;
            }
            QHeaderView::section {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #2a2a2a, stop:1 #1a1a1a);
                color: white;
                padding: 10px;
                border: none;
                border-bottom: 2px solid #10b981;
                font-weight: bold;
                font-size: 13px;
                letter-spacing: 1px;
            }
            #inputCard {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #1a1a1a, stop:1 #0f0f0f);
                border: 2px solid #2a2a2a;
                border-radius: 15px;
                padding: 12px;
            }
            #idInput {
                background-color: #1a1a1a;
                color: white;
                border: 2px solid #2a2a2a;
                border-radius: 10px;
                padding: 10px 15px;
                font-size: 14px;
                font-weight: bold;
            }
            #idInput:focus {
                border: 2px solid #10b981;
                background-color: #1e1e1e;
            }
            #selectedInfo {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(16, 185, 129, 0.2), stop:1 rgba(16, 185, 129, 0.05));
                border: 1px solid rgba(16, 185, 129, 0.3);
                border-radius: 8px;
                padding: 10px;
                color: #10b981;
            }
            QPushButton#btnBorrow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #10b981, stop:1 #059669);
                color: white;
                border: none;
                border-radius: 12px;
                padding: 12px 40px;
                font-size: 15px;
                font-weight: bold;
                letter-spacing: 1px;
            }
            QPushButton#btnBorrow:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #34d399, stop:1 #10b981);
            }
            QPushButton#btnBorrow:disabled {
                background: #2a2a2a;
                color: #666666;
            }
            QPushButton#btnCancel {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #dc2626, stop:1 #f97316);
                color: white;
                border: none;
                border-radius: 12px;
                padding: 12px 40px;
                font-size: 15px;
                font-weight: bold;
                letter-spacing: 1px;
            }
        """)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(25, 25, 25, 25)
        main_layout.setSpacing(15)

        # Header
        header_layout = QtWidgets.QVBoxLayout()
        header_layout.setSpacing(5)
        
        title_label = QtWidgets.QLabel("📥 PINJAM BUKU")
        title_label.setObjectName("headerLabel")
        
        subtitle_label = QtWidgets.QLabel(f"MEMBER: {username.upper()}")
        subtitle_label.setObjectName("subtitleLabel")
        
        header_layout.addWidget(title_label)
        header_layout.addWidget(subtitle_label)
        main_layout.addLayout(header_layout)

        # Search box
        search_label = QtWidgets.QLabel("🔍 Cari Buku yang Tersedia")
        search_label.setStyleSheet("color: rgba(255, 255, 255, 0.7); font-size: 12px; margin-bottom: 2px;")
        
        self.search_input = QtWidgets.QLineEdit()
        self.search_input.setObjectName("searchBox")
        self.search_input.setPlaceholderText("Cari berdasarkan judul, pengarang, atau ID buku...")
        self.search_input.textChanged.connect(self.filter_table)
        
        main_layout.addWidget(search_label)
        main_layout.addWidget(self.search_input)

        # Table with available books (Given more stretch factor)
        self.table = QtWidgets.QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID BUKU", "JUDUL", "PENGARANG", "STOK"])
        
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Fixed)
        
        self.table.setColumnWidth(0, 100)
        self.table.setColumnWidth(3, 80)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.verticalHeader().setVisible(False)
        self.table.itemSelectionChanged.connect(self.on_book_selected)
        
        # Add table with stretch factor 1 to maximize space
        main_layout.addWidget(self.table, stretch=1)

        # Input card for manual ID entry (Slimmer version)
        input_card = QtWidgets.QFrame()
        input_card.setObjectName("inputCard")
        input_layout = QtWidgets.QVBoxLayout(input_card)
        input_layout.setSpacing(10)
        input_layout.setContentsMargins(15, 10, 15, 10)
        
        input_label = QtWidgets.QLabel("Masukkan ID Buku secara manual:")
        input_label.setStyleSheet("color: rgba(255, 255, 255, 0.7); font-size: 12px;")
        
        self.id_input = QtWidgets.QLineEdit()
        self.id_input.setObjectName("idInput")
        self.id_input.setPlaceholderText("ID Buku...")
        self.id_input.textChanged.connect(self.on_manual_input)
        
        self.selected_info = QtWidgets.QLabel("📚 Pilih buku dari tabel atau masukkan ID buku")
        self.selected_info.setObjectName("selectedInfo")
        self.selected_info.setAlignment(QtCore.Qt.AlignCenter)
        self.selected_info.setWordWrap(True)
        
        input_layout.addWidget(input_label)
        input_layout.addWidget(self.id_input)
        input_layout.addWidget(self.selected_info)
        
        main_layout.addWidget(input_card)

        # Buttons
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.setSpacing(15)
        
        self.btn_borrow = QtWidgets.QPushButton("📥 PINJAM BUKU INI")
        self.btn_borrow.setObjectName("btnBorrow")
        self.btn_borrow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_borrow.clicked.connect(self.proses_pinjam)
        self.btn_borrow.setEnabled(False)
        
        btn_cancel = QtWidgets.QPushButton("BATAL")
        btn_cancel.setObjectName("btnCancel")
        btn_cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btn_cancel.clicked.connect(self.close)
        
        button_layout.addStretch()
        button_layout.addWidget(self.btn_borrow)
        button_layout.addWidget(btn_cancel)
        
        main_layout.addLayout(button_layout)

        # Load data
        self.all_books = []
        self.selected_book = None
        self.load_data()

    def load_data(self):
        """Load available books (stok > 0)"""
        try:
            all_books = BukuModel.read_all()
            self.all_books = [book for book in all_books if int(book['stok']) > 0]
            self.display_books(self.all_books)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Gagal memuat data: {str(e)}")

    def display_books(self, books):
        """Display books in table"""
        self.table.setRowCount(len(books))
        for row, book in enumerate(books):
            id_item = QtWidgets.QTableWidgetItem(str(book['id_buku']))
            id_item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table.setItem(row, 0, id_item)
            
            judul_item = QtWidgets.QTableWidgetItem(str(book['judul']))
            self.table.setItem(row, 1, judul_item)
            
            pengarang_item = QtWidgets.QTableWidgetItem(str(book['pengarang']))
            self.table.setItem(row, 2, pengarang_item)
            
            stok = int(book['stok'])
            stok_item = QtWidgets.QTableWidgetItem(str(stok))
            stok_item.setTextAlignment(QtCore.Qt.AlignCenter)
            
            if stok < 5:
                stok_item.setForeground(QtGui.QColor("#f97316"))
            else:
                stok_item.setForeground(QtGui.QColor("#10b981"))
            
            self.table.setItem(row, 3, stok_item)
            self.table.setRowHeight(row, 45)

    def filter_table(self):
        """Filter table based on search input"""
        search_text = self.search_input.text().lower()
        if not search_text:
            self.display_books(self.all_books)
            return
        
        filtered_books = [
            book for book in self.all_books
            if search_text in str(book['judul']).lower() or 
               search_text in str(book['pengarang']).lower() or
               search_text in str(book['id_buku']).lower()
        ]
        self.display_books(filtered_books)

    def on_book_selected(self):
        """Handle book selection from table"""
        selected_rows = self.table.selectedItems()
        if not selected_rows:
            self.selected_book = None
            self.id_input.clear()
            self.selected_info.setText("📚 Pilih buku dari tabel atau masukkan ID buku")
            self.btn_borrow.setEnabled(False)
            return
        
        row = self.table.currentRow()
        book_id = self.table.item(row, 0).text()
        judul = self.table.item(row, 1).text()
        pengarang = self.table.item(row, 2).text()
        stok = self.table.item(row, 3).text()
        
        # Block signals temporarily to avoid loop with manual input
        self.id_input.blockSignals(True)
        self.id_input.setText(book_id)
        self.id_input.blockSignals(False)
        
        self.selected_book = book_id
        self.selected_info.setText(f"✅ Dipilih: [{book_id}] {judul} (Stok: {stok})")
        self.btn_borrow.setEnabled(True)

    def on_manual_input(self):
        """Handle manual ID input"""
        book_id = self.id_input.text().strip()
        if not book_id:
            self.selected_book = None
            self.selected_info.setText("📚 Pilih buku dari tabel atau masukkan ID buku")
            self.btn_borrow.setEnabled(False)
            return
        
        book_found = next((b for b in self.all_books if str(b['id_buku']) == book_id), None)
        
        if book_found:
            self.selected_book = book_id
            self.selected_info.setText(f"✅ Dipilih: [{book_id}] {book_found['judul']} (Stok: {book_found['stok']})")
            self.btn_borrow.setEnabled(True)
            
            # Select in table if visible
            for row in range(self.table.rowCount()):
                if self.table.item(row, 0).text() == book_id:
                    self.table.selectRow(row)
                    break
        else:
            self.selected_book = None
            self.selected_info.setText("❌ ID Buku tidak ditemukan atau stok habis")
            self.btn_borrow.setEnabled(False)

    def proses_pinjam(self):
        """Process book borrowing"""
        if not self.selected_book:
            return
        
        msg = QtWidgets.QMessageBox(self)
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setWindowTitle("Konfirmasi")
        msg.setText(f"Pinjam buku ID: {self.selected_book}?")
        msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        msg.setStyleSheet("QMessageBox { background-color: #1a1a1a; } QLabel { color: white; }")
        
        if msg.exec_() != QtWidgets.QMessageBox.Yes:
            return
        
        tgl_skrg = datetime.now().strftime('%Y-%m-%d')
        if PinjamModel.create_pinjam(self.username, self.selected_book, tgl_skrg):
            QtWidgets.QMessageBox.information(self, "Berhasil", "Permintaan terkirim! Menunggu validasi admin.")
            self.close()
        else:
            QtWidgets.QMessageBox.critical(self, "Gagal", "Gagal mengirim permintaan.")