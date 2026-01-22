from PyQt5 import QtWidgets, QtCore, QtGui
from menu_anggota_buku import LihatBukuWindow
from menu_anggota_pinjam import PinjamBukuWindow
from menu_anggota_kembali import KembaliBukuWindow

class AnggotaPage(QtWidgets.QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.setWindowTitle(f"Member Dashboard - {username}")
        self.resize(1100, 700)
        
        # Enhanced dark theme with blue accents
        self.setStyleSheet("""
            QMainWindow { 
                background: #0a0a0a;
            }
            #headerCard {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #1a1a1a, stop:1 #0f0f0f);
                border-radius: 20px;
                border: 1px solid #2a2a2a;
            }
            #titleLabel {
                color: white;
                font-size: 32px;
                font-weight: bold;
                letter-spacing: 2px;
            }
            #subtitleLabel {
                color: rgba(255, 255, 255, 0.5);
                font-size: 14px;
                letter-spacing: 1px;
            }
            #menuCard {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #1a1a1a, stop:1 #0f0f0f);
                border: 2px solid #2a2a2a;
                border-radius: 20px;
            }
            #menuCard:hover {
                border: 2px solid #3b82f6;
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #1e3a5f, stop:1 #0f1e3a);
            }
            #menuIcon {
                color: transparent;
                font-size: 52px;
                margin-bottom: 15px;
            }
            #menuTitle {
                color: white;
                font-size: 18px;
                font-weight: bold;
                letter-spacing: 1px;
            }
            #menuDesc {
                color: rgba(255, 255, 255, 0.5);
                font-size: 13px;
            }
            #btnLogout {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #dc2626, stop:0.5 #f97316, stop:1 #ea580c);
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 14px;
                font-weight: bold;
                letter-spacing: 1px;
                padding: 12px 30px;
            }
            #btnLogout:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #ef4444, stop:0.5 #fb923c, stop:1 #f97316);
            }
            #btnLogout:pressed {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #b91c1c, stop:0.5 #ea580c, stop:1 #c2410c);
            }
            #footerText {
                color: rgba(255, 255, 255, 0.3);
                font-size: 12px;
            }
            #statusDot {
                background: #10b981;
                border-radius: 6px;
            }
            #userIcon {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #3b82f6, stop:1 #2563eb);
                border-radius: 30px;
                color: white;
                font-size: 24px;
                font-weight: bold;
            }
        """)

        self.central = QtWidgets.QWidget()
        self.setCentralWidget(self.central)
        layout = QtWidgets.QVBoxLayout(self.central)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(30)

        # Background decorative circles (blue theme)
        self.decor1 = QtWidgets.QFrame(self.central)
        self.decor1.setStyleSheet("""
            background: qradialgradient(cx:0.5, cy:0.5, radius:0.8,
                fx:0.5, fy:0.5,
                stop:0 rgba(59, 130, 246, 0.3),
                stop:0.5 rgba(37, 99, 235, 0.15),
                stop:1 transparent);
            border-radius: 250px;
        """)
        self.decor1.setFixedSize(500, 500)
        self.decor1.move(-200, -150)

        self.decor2 = QtWidgets.QFrame(self.central)
        self.decor2.setStyleSheet("""
            background: qradialgradient(cx:0.5, cy:0.5, radius:0.8,
                fx:0.5, fy:0.5,
                stop:0 rgba(37, 99, 235, 0.3),
                stop:0.5 rgba(59, 130, 246, 0.15),
                stop:1 transparent);
            border-radius: 200px;
        """)
        self.decor2.setFixedSize(400, 400)
        self.decor2.move(900, 450)

        # --- HEADER SECTION ---
        header_card = QtWidgets.QFrame()
        header_card.setObjectName("headerCard")
        header_layout = QtWidgets.QHBoxLayout(header_card)
        header_layout.setContentsMargins(30, 25, 30, 25)

        # Left side - User info with avatar
        left_header = QtWidgets.QHBoxLayout()
        left_header.setSpacing(20)
        
        # User avatar
        avatar = QtWidgets.QLabel(username[0].upper())
        avatar.setObjectName("userIcon")
        avatar.setFixedSize(60, 60)
        avatar.setAlignment(QtCore.Qt.AlignCenter)
        
        # Title and subtitle
        user_info = QtWidgets.QVBoxLayout()
        user_info.setSpacing(5)
        
        lbl_title = QtWidgets.QLabel(f"WELCOME, {username.upper()}!")
        lbl_title.setObjectName("titleLabel")
        
        lbl_subtitle = QtWidgets.QLabel("MEMBER LIBRARY PORTAL")
        lbl_subtitle.setObjectName("subtitleLabel")
        
        user_info.addWidget(lbl_title)
        user_info.addWidget(lbl_subtitle)
        
        left_header.addWidget(avatar)
        left_header.addLayout(user_info)

        # Right side - Status & Logout
        right_header = QtWidgets.QVBoxLayout()
        right_header.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        right_header.setSpacing(15)
        
        # Status indicator
        status_container = QtWidgets.QHBoxLayout()
        status_container.setAlignment(QtCore.Qt.AlignRight)
        
        status_dot = QtWidgets.QFrame()
        status_dot.setObjectName("statusDot")
        status_dot.setFixedSize(12, 12)
        
        status_label = QtWidgets.QLabel("Active Member")
        status_label.setStyleSheet("color: rgba(255, 255, 255, 0.7); font-size: 13px;")
        
        status_container.addWidget(status_dot)
        status_container.addSpacing(8)
        status_container.addWidget(status_label)
        
        self.btnLogout = QtWidgets.QPushButton("SIGN OUT")
        self.btnLogout.setObjectName("btnLogout")
        self.btnLogout.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLogout.clicked.connect(self.handle_logout)
        
        right_header.addLayout(status_container)
        right_header.addWidget(self.btnLogout)

        header_layout.addLayout(left_header, 1)
        header_layout.addLayout(right_header, 0)

        # Add shadow to header
        header_shadow = QtWidgets.QGraphicsDropShadowEffect()
        header_shadow.setBlurRadius(30)
        header_shadow.setXOffset(0)
        header_shadow.setYOffset(10)
        header_shadow.setColor(QtGui.QColor(0, 0, 0, 100))
        header_card.setGraphicsEffect(header_shadow)

        layout.addWidget(header_card)
        layout.addSpacing(20)

        # --- MENU GRID SECTION ---
        grid_container = QtWidgets.QWidget()
        grid = QtWidgets.QGridLayout(grid_container)
        grid.setSpacing(25)
        grid.setContentsMargins(0, 0, 0, 0)

        # Menu items data
        menus = [
            {
                'icon': '📚',
                'title': 'BOOK CATALOG',
                'desc': 'Jelajahi koleksi buku perpustakaan',
                'gradient': 'stop:0 rgba(59, 130, 246, 0.2), stop:1 rgba(59, 130, 246, 0.05)',
                'callback': self.buka_lihat_buku
            },
            {
                'icon': '📥',
                'title': 'BORROW BOOK',
                'desc': 'Pinjam buku dari koleksi tersedia',
                'gradient': 'stop:0 rgba(16, 185, 129, 0.2), stop:1 rgba(16, 185, 129, 0.05)',
                'callback': self.buka_pinjam_buku
            },
            {
                'icon': '📤',
                'title': 'RETURN BOOK',
                'desc': 'Kembalikan buku yang dipinjam',
                'gradient': 'stop:0 rgba(249, 115, 22, 0.2), stop:1 rgba(249, 115, 22, 0.05)',
                'callback': self.buka_kembalikan_buku
            }
        ]

        # Create menu cards
        for idx, menu in enumerate(menus):
            card = self.create_menu_card(
                menu['icon'],
                menu['title'],
                menu['desc'],
                menu['gradient'],
                menu['callback']
            )
            row = idx // 3
            col = idx % 3
            grid.addWidget(card, row, col)

        layout.addWidget(grid_container, 1)

        # Footer
        footer_layout = QtWidgets.QHBoxLayout()
        footer_left = QtWidgets.QLabel("Member Portal - Library Hub System v2.0")
        footer_left.setObjectName("footerText")
        
        footer_right = QtWidgets.QLabel("© 2026 All Rights Reserved")
        footer_right.setObjectName("footerText")
        footer_right.setAlignment(QtCore.Qt.AlignRight)
        
        footer_layout.addWidget(footer_left)
        footer_layout.addStretch()
        footer_layout.addWidget(footer_right)
        
        layout.addLayout(footer_layout)

    def create_menu_card(self, icon, title, desc, gradient, callback):
        """Create an interactive menu card"""
        card = QtWidgets.QFrame()
        card.setObjectName("menuCard")
        card.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        card.setMinimumSize(320, 200)
        
        # Make card clickable
        card.mousePressEvent = lambda event: callback()
        
        card_layout = QtWidgets.QVBoxLayout(card)
        card_layout.setContentsMargins(30, 30, 30, 30)
        card_layout.setSpacing(12)
        
        # Gradient background accent
        accent_bar = QtWidgets.QFrame()
        accent_bar.setFixedHeight(4)
        accent_bar.setStyleSheet(f"""
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                {gradient});
            border-radius: 2px;
        """)
        
        # Icon
        icon_label = QtWidgets.QLabel(icon)
        icon_label.setStyleSheet("font-size: 52px;")
        icon_label.setAlignment(QtCore.Qt.AlignCenter)
        
        # Title
        title_label = QtWidgets.QLabel(title)
        title_label.setObjectName("menuTitle")
        title_label.setAlignment(QtCore.Qt.AlignCenter)
        
        # Description
        desc_label = QtWidgets.QLabel(desc)
        desc_label.setObjectName("menuDesc")
        desc_label.setAlignment(QtCore.Qt.AlignCenter)
        desc_label.setWordWrap(True)
        
        # Arrow icon
        arrow_container = QtWidgets.QHBoxLayout()
        arrow_label = QtWidgets.QLabel("→")
        arrow_label.setStyleSheet("""
            color: rgba(255, 255, 255, 0.4);
            font-size: 24px;
            font-weight: bold;
        """)
        arrow_container.addStretch()
        arrow_container.addWidget(arrow_label)
        
        card_layout.addWidget(accent_bar)
        card_layout.addSpacing(10)
        card_layout.addWidget(icon_label)
        card_layout.addWidget(title_label)
        card_layout.addWidget(desc_label)
        card_layout.addStretch()
        card_layout.addLayout(arrow_container)
        
        # Shadow effect
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)
        shadow.setXOffset(0)
        shadow.setYOffset(10)
        shadow.setColor(QtGui.QColor(0, 0, 0, 120))
        card.setGraphicsEffect(shadow)
        
        return card

    # --- NAVIGATION FUNCTIONS ---

    def buka_lihat_buku(self):
        self.win = LihatBukuWindow()
        self.win.show()

    def buka_pinjam_buku(self):
        self.win = PinjamBukuWindow(self.username)
        self.win.show()

    def buka_kembalikan_buku(self):
        self.win = KembaliBukuWindow(self.username)
        self.win.show()

    def handle_logout(self):
        msg = QtWidgets.QMessageBox(self)
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setWindowTitle("Sign Out")
        msg.setText("Are you sure you want to sign out?")
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
            from login import LoginPage
            self.login_win = LoginPage()
            self.login_win.show()
            self.close()