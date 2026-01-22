from PyQt5 import QtWidgets, QtCore, QtGui
from modul.buku import BukuModel

class LihatBukuWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Katalog Buku Perpustakaan")
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
            #searchBox {
                background-color: #1a1a1a;
                color: white;
                border: 2px solid #2a2a2a;
                border-radius: 12px;
                padding: 12px 20px;
                font-size: 14px;
            }
            #searchBox:focus {
                border: 2px solid #3b82f6;
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
                background-color: #3b82f6;
                color: white;
            }
            QHeaderView::section {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #2a2a2a, stop:1 #1a1a1a);
                color: white;
                padding: 12px;
                border: none;
                border-bottom: 2px solid #3b82f6;
                font-weight: bold;
                font-size: 13px;
                letter-spacing: 1px;
            }
            QPushButton#btnClose {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #dc2626, stop:1 #f97316);
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
                    stop:0 #ef4444, stop:1 #fb923c);
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
            #statsCard {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #1a1a1a, stop:1 #0f0f0f);
                border: 2px solid #2a2a2a;
                border-radius: 12px;
                padding: 15px;
            }
            #statsLabel {
                color: rgba(255, 255, 255, 0.7);
                font-size: 13px;
            }
            #statsValue {
                color: #3b82f6;
                font-size: 24px;
                font-weight: bold;
            }
        """)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(20)

        # Header section
        header_layout = QtWidgets.QVBoxLayout()
        header_layout.setSpacing(8)
        
        title_label = QtWidgets.QLabel("📚 KATALOG BUKU")
        title_label.setObjectName("headerLabel")
        
        subtitle_label = QtWidgets.QLabel("JELAJAHI KOLEKSI PERPUSTAKAAN")
        subtitle_label.setObjectName("subtitleLabel")
        
        header_layout.addWidget(title_label)
        header_layout.addWidget(subtitle_label)
        
        main_layout.addLayout(header_layout)

        # Search and stats section
        search_stats_layout = QtWidgets.QHBoxLayout()
        search_stats_layout.setSpacing(20)

        # Search box
        search_container = QtWidgets.QVBoxLayout()
        search_label = QtWidgets.QLabel("🔍 Cari Buku")
        search_label.setStyleSheet("color: rgba(255, 255, 255, 0.7); font-size: 13px; margin-bottom: 5px;")
        
        self.search_input = QtWidgets.QLineEdit()
        self.search_input.setObjectName("searchBox")
        self.search_input.setPlaceholderText("Cari berdasarkan judul atau pengarang...")
        self.search_input.textChanged.connect(self.filter_table)
        
        search_container.addWidget(search_label)
        search_container.addWidget(self.search_input)

        # Stats card
        stats_card = QtWidgets.QFrame()
        stats_card.setObjectName("statsCard")
        stats_layout = QtWidgets.QVBoxLayout(stats_card)
        stats_layout.setContentsMargins(20, 15, 20, 15)
        
        stats_label = QtWidgets.QLabel("Total Buku")
        stats_label.setObjectName("statsLabel")
        
        self.stats_value = QtWidgets.QLabel("0")
        self.stats_value.setObjectName("statsValue")
        
        stats_layout.addWidget(stats_label)
        stats_layout.addWidget(self.stats_value)
        
        search_stats_layout.addLayout(search_container, 3)
        search_stats_layout.addWidget(stats_card, 1)
        
        main_layout.addLayout(search_stats_layout)

        # Table
        self.table = QtWidgets.QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID BUKU", "JUDUL", "PENGARANG", "STOK"])
        
        # Set column widths
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Fixed)
        
        self.table.setColumnWidth(0, 120)
        self.table.setColumnWidth(3, 100)
        
        # Table settings
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setAlternatingRowColors(False)
        self.table.verticalHeader().setVisible(False)
        self.table.setShowGrid(True)
        
        main_layout.addWidget(self.table)

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

        # Load initial data
        self.all_books = []
        self.load_data()

    def load_data(self):
        """Load all books from database"""
        try:
            self.all_books = BukuModel.read_all()
            self.display_books(self.all_books)
            self.stats_value.setText(str(len(self.all_books)))
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Gagal memuat data: {str(e)}")

    def display_books(self, books):
        """Display books in table"""
        self.table.setRowCount(len(books))
        
        for row, book in enumerate(books):
            # ID Buku
            id_item = QtWidgets.QTableWidgetItem(str(book['id_buku']))
            id_item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table.setItem(row, 0, id_item)
            
            # Judul
            judul_item = QtWidgets.QTableWidgetItem(str(book['judul']))
            self.table.setItem(row, 1, judul_item)
            
            # Pengarang
            pengarang_item = QtWidgets.QTableWidgetItem(str(book['pengarang']))
            self.table.setItem(row, 2, pengarang_item)
            
            # Stok with color coding
            stok = int(book['stok'])
            stok_item = QtWidgets.QTableWidgetItem(str(stok))
            stok_item.setTextAlignment(QtCore.Qt.AlignCenter)
            
            # Color code based on stock
            if stok == 0:
                stok_item.setForeground(QtGui.QColor("#ef4444"))  # Red
                stok_item.setFont(QtGui.QFont("", -1, QtGui.QFont.Bold))
            elif stok < 5:
                stok_item.setForeground(QtGui.QColor("#f97316"))  # Orange
            else:
                stok_item.setForeground(QtGui.QColor("#10b981"))  # Green
            
            self.table.setItem(row, 3, stok_item)
            
            # Set row height
            self.table.setRowHeight(row, 50)

    def filter_table(self):
        """Filter table based on search input"""
        search_text = self.search_input.text().lower()
        
        if not search_text:
            # Show all books if search is empty
            self.display_books(self.all_books)
            return
        
        # Filter books
        filtered_books = [
            book for book in self.all_books
            if search_text in str(book['judul']).lower() or 
               search_text in str(book['pengarang']).lower() or
               search_text in str(book['id_buku']).lower()
        ]
        
        self.display_books(filtered_books)