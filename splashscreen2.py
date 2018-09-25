import sys

from PyQt4 import QtGui, QtCore
from loginD import *
from mainwindow import Ui_MainWindow


class Login(QtGui.QDialog):


# A dialog with username and password lineedit
def __init__(self, parent=None):
    QtGui.QDialog.__init__(self, parent)
    self.ui = Ui_LoginD()
    self.ui.setupUi(self)
    self.ui.PasswordLE.setEchoMode(QtGui.QLineEdit.Password)
    QtCore.QObject.connect(self.ui.LoginPB, QtCore.SIGNAL('clicked()'),
                           self.HandleLogin)


def HandleLogin(self):
    if self.ui.PasswordLE.text() == "pass":
        self.accept()

    else:
        QtGui.QMessageBox.warning(
            self, 'Error;', 'bad')


class Main_Window(QtGui.QMainWindow, ):
    # main window ui
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)

    splash_pix = QtGui.QPixmap('logo and typeface blue.jpg')
    splash = QtGui.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    splash.show()


    def login():
        splash.close()
        if Login().exec_() == QtGui.QDialog.Accepted:
            global window
            window = Main_Window()
            window.show()
        else:
            app.quit()


    QtCore.QTimer.singleShot(2000, login)

    sys.exit(app.exec_())
