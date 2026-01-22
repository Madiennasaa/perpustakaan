import sys
from PyQt5 import QtWidgets
from login import LoginPage

def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion") 
    login_win = LoginPage()
    login_win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()