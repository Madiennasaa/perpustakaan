import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from modul.user import User
from petugas import PetugasPage
from anggota import AnggotaPage

class LoginPage(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Library Hub")
        self.resize(1000, 650)
        
        # Dark theme dengan accent merah-oranye
        self.setStyleSheet("""
            QMainWindow { 
                background: #0a0a0a;
            }
            #mainCard {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #1a1a1a, stop:1 #0f0f0f);
                border-radius: 25px;
                border: 1px solid #2a2a2a;
            }
            #glowPanel {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 rgba(220, 38, 38, 0.15), 
                    stop:0.5 rgba(249, 115, 22, 0.15),
                    stop:1 rgba(234, 88, 12, 0.15));
                border-radius: 25px;
            }
            #titleMain {
                color: #ffffff;
                font-size: 42px;
                font-weight: bold;
                letter-spacing: 2px;
            }
            #subtitle {
                color: rgba(255, 255, 255, 0.6);
                font-size: 16px;
                letter-spacing: 1px;
            }
            QLabel#fieldLabel {
                color: rgba(255, 255, 255, 0.7);
                font-size: 13px;
                font-weight: 600;
            }
            QLineEdit {
                background: rgba(30, 30, 30, 0.8);
                border: 2px solid #2a2a2a;
                border-radius: 12px;
                padding: 16px 20px;
                color: white;
                font-size: 15px;
                selection-background-color: #dc2626;
            }
            QLineEdit:focus {
                border: 2px solid #dc2626;
                background: rgba(40, 40, 40, 0.9);
            }
            QLineEdit::placeholder {
                color: rgba(255, 255, 255, 0.3);
            }
            #btnLogin {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #dc2626, stop:0.5 #f97316, stop:1 #ea580c);
                color: white;
                border: none;
                border-radius: 12px;
                font-size: 16px;
                font-weight: bold;
                letter-spacing: 1px;
                padding: 18px;
            }
            #btnLogin:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #ef4444, stop:0.5 #fb923c, stop:1 #f97316);
            }
            #btnLogin:pressed {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #b91c1c, stop:0.5 #ea580c, stop:1 #c2410c);
            }
            #decorCircle {
                background: qradialgradient(cx:0.5, cy:0.5, radius:0.8,
                    fx:0.5, fy:0.5,
                    stop:0 rgba(220, 38, 38, 0.4),
                    stop:0.5 rgba(249, 115, 22, 0.2),
                    stop:1 transparent);
                border-radius: 200px;
            }
        """)

        self.central = QtWidgets.QWidget()
        self.setCentralWidget(self.central)
        self.main_layout = QtWidgets.QVBoxLayout(self.central)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        # Background decorative circles
        self.decor1 = QtWidgets.QFrame(self.central)
        self.decor1.setObjectName("decorCircle")
        self.decor1.setFixedSize(400, 400)
        self.decor1.move(-200, -100)

        self.decor2 = QtWidgets.QFrame(self.central)
        self.decor2.setObjectName("decorCircle")
        self.decor2.setFixedSize(350, 350)
        self.decor2.move(850, 400)

        # Main container
        self.container = QtWidgets.QWidget()
        self.container_layout = QtWidgets.QHBoxLayout(self.container)
        self.container_layout.setContentsMargins(80, 80, 80, 80)
        self.container_layout.setSpacing(60)

        # --- Bagian Kiri (Branding) ---
        self.left_side = QtWidgets.QWidget()
        self.left_layout = QtWidgets.QVBoxLayout(self.left_side)

        # Tambahkan stretch di awal agar konten terdorong ke tengah secara vertikal
        self.left_layout.addStretch() 
        self.left_layout.setAlignment(QtCore.Qt.AlignCenter)
        self.left_layout.setSpacing(15) # Mengurangi spasi agar lebih rapat dan rapi

        # Logo (Pastikan alignment label-nya Center)
        self.logo_widget = QtWidgets.QLabel()
        self.logo_widget.setFixedSize(180, 180)
        self.logo_widget.setPixmap(self.create_modern_logo())
        self.logo_widget.setAlignment(QtCore.Qt.AlignCenter) # <--- Sangat Penting

        self.brand_title = QtWidgets.QLabel("LIBRARY")
        self.brand_title.setObjectName("titleMain")
        self.brand_title.setAlignment(QtCore.Qt.AlignCenter)

        self.brand_subtitle = QtWidgets.QLabel("MANAGEMENT SYSTEM")
        self.brand_subtitle.setObjectName("subtitle")
        self.brand_subtitle.setAlignment(QtCore.Qt.AlignCenter)

        # Feature badges
        self.features = QtWidgets.QWidget()
        self.features_layout = QtWidgets.QVBoxLayout(self.features)
        self.features_layout.setSpacing(12)
        
        features_text = [
            "📚  Manajemen Koleksi Digital",
            "👥  Multi-User Support",
            "🔒  Keamanan Terjamin"
        ]
        
        for feat in features_text:
            lbl = QtWidgets.QLabel(feat)
            lbl.setStyleSheet("""
                color: rgba(255, 255, 255, 0.7);
                font-size: 14px;
                padding: 8px 0;
            """)
            self.features_layout.addWidget(lbl)

        self.left_layout.addWidget(self.logo_widget, 0, QtCore.Qt.AlignCenter)
        self.left_layout.addWidget(self.brand_title)
        self.left_layout.addWidget(self.brand_subtitle)
        self.left_layout.addSpacing(30)
        self.left_layout.addWidget(self.features)

        # Right side - Login form
        self.right_side = QtWidgets.QFrame()
        self.right_side.setObjectName("mainCard")
        self.right_side.setFixedWidth(420)
        self.right_layout = QtWidgets.QVBoxLayout(self.right_side)
        self.right_layout.setContentsMargins(45, 50, 45, 50)
        self.right_layout.setSpacing(0)

        # Glow effect panel
        self.glow_panel = QtWidgets.QFrame()
        self.glow_panel.setObjectName("glowPanel")
        self.glow_panel.setFixedHeight(6)
        
        self.form_title = QtWidgets.QLabel("Welcome Back")
        self.form_title.setStyleSheet("""
            color: white;
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 8px;
        """)
        
        self.form_subtitle = QtWidgets.QLabel("Sign in to continue")
        self.form_subtitle.setStyleSheet("""
            color: rgba(255, 255, 255, 0.5);
            font-size: 14px;
            margin-bottom: 35px;
        """)

        # Username field
        self.username_label = QtWidgets.QLabel("USERNAME")
        self.username_label.setObjectName("fieldLabel")
        
        self.txtUsername = QtWidgets.QLineEdit()
        self.txtUsername.setPlaceholderText("Enter your username")
        self.txtUsername.setMinimumHeight(55)

        # Password field
        self.password_label = QtWidgets.QLabel("PASSWORD")
        self.password_label.setObjectName("fieldLabel")
        
        self.txtPassword = QtWidgets.QLineEdit()
        self.txtPassword.setPlaceholderText("Enter your password")
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setMinimumHeight(55)

        # Login button
        self.btnLogin = QtWidgets.QPushButton("SIGN IN")
        self.btnLogin.setObjectName("btnLogin")
        self.btnLogin.setMinimumHeight(55)
        self.btnLogin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLogin.clicked.connect(self.handle_login)

        # Enter key support
        self.txtPassword.returnPressed.connect(self.handle_login)
        self.txtUsername.returnPressed.connect(self.txtPassword.setFocus)

        # Footer text
        self.footer_text = QtWidgets.QLabel("Powered by Library Hub System")
        self.footer_text.setAlignment(QtCore.Qt.AlignCenter)
        self.footer_text.setStyleSheet("""
            color: rgba(255, 255, 255, 0.3);
            font-size: 11px;
            margin-top: 20px;
        """)

        # Add widgets to right layout
        self.right_layout.addWidget(self.glow_panel)
        self.right_layout.addSpacing(35)
        self.right_layout.addWidget(self.form_title)
        self.right_layout.addWidget(self.form_subtitle)
        self.right_layout.addSpacing(30)
        self.right_layout.addWidget(self.username_label)
        self.right_layout.addSpacing(8)
        self.right_layout.addWidget(self.txtUsername)
        self.right_layout.addSpacing(22)
        self.right_layout.addWidget(self.password_label)
        self.right_layout.addSpacing(8)
        self.right_layout.addWidget(self.txtPassword)
        self.right_layout.addSpacing(35)
        self.right_layout.addWidget(self.btnLogin)
        self.right_layout.addWidget(self.footer_text)
        self.right_layout.addStretch()

        # Add to container
        self.container_layout.addWidget(self.left_side, 1)
        self.container_layout.addWidget(self.right_side, 0)

        self.main_layout.addWidget(self.container)

        # Shadow effects
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(50)
        shadow.setXOffset(0)
        shadow.setYOffset(20)
        shadow.setColor(QtGui.QColor(0, 0, 0, 150))
        self.right_side.setGraphicsEffect(shadow)

    def create_modern_logo(self):
        """Create a modern geometric logo"""
        pixmap = QtGui.QPixmap(180, 180)
        pixmap.fill(QtCore.Qt.transparent)
        
        painter = QtGui.QPainter(pixmap)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        
        # Outer glow circle
        gradient = QtGui.QRadialGradient(90, 90, 80)
        gradient.setColorAt(0, QtGui.QColor(220, 38, 38, 100))
        gradient.setColorAt(0.5, QtGui.QColor(249, 115, 22, 60))
        gradient.setColorAt(1, QtGui.QColor(234, 88, 12, 0))
        painter.setBrush(gradient)
        painter.setPen(QtCore.Qt.NoPen)
        painter.drawEllipse(10, 10, 160, 160)
        
        # Main circle
        gradient2 = QtGui.QLinearGradient(0, 0, 180, 180)
        gradient2.setColorAt(0, QtGui.QColor(220, 38, 38))
        gradient2.setColorAt(0.5, QtGui.QColor(249, 115, 22))
        gradient2.setColorAt(1, QtGui.QColor(234, 88, 12))
        painter.setBrush(gradient2)
        painter.setPen(QtGui.QPen(QtGui.QColor(255, 255, 255, 30), 2))
        painter.drawEllipse(30, 30, 120, 120)
        
        # Book symbol
        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(QtGui.QColor(255, 255, 255, 230))
        
        # Left page
        path1 = QtGui.QPainterPath()
        path1.moveTo(70, 65)
        path1.lineTo(70, 115)
        path1.lineTo(85, 115)
        path1.lineTo(90, 110)
        path1.lineTo(90, 70)
        path1.lineTo(85, 65)
        path1.closeSubpath()
        painter.drawPath(path1)
        
        # Right page
        path2 = QtGui.QPainterPath()
        path2.moveTo(90, 70)
        path2.lineTo(90, 110)
        path2.lineTo(95, 115)
        path2.lineTo(110, 115)
        path2.lineTo(110, 65)
        path2.lineTo(95, 65)
        path2.closeSubpath()
        painter.drawPath(path2)
        
        # Page lines
        painter.setPen(QtGui.QPen(QtGui.QColor(220, 38, 38, 150), 1.5))
        for i in range(3):
            y = 80 + (i * 10)
            painter.drawLine(75, y, 85, y)
            painter.drawLine(95, y, 105, y)
        
        painter.end()
        return pixmap

    def handle_login(self):
        u, p = self.txtUsername.text().strip(), self.txtPassword.text()
        
        if not u or not p:
            self.show_error_message("Error", "Please fill in all fields!")
            return
            
        user_data = User.login(u, p)
        if user_data:
            if user_data['role'] == 'petugas':
                self.win = PetugasPage()
            else:
                self.win = AnggotaPage(user_data['username'])
            self.win.show()
            self.close()
        else:
            self.show_error_message("Login Failed", "Invalid username or password!")

    def show_error_message(self, title, message):
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
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #ef4444, stop:1 #fb923c);
            }
        """)
        msg.exec_()