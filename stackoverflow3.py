# -*- coding: utf-8 -*-
from PySide import QtGui, QtCore


class MainWindow(QtGui.QWidget):
    '''Main window lets user know when window was clicked on non-widget space'''

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.initUI()

    def initUI(self):
        self.myLabel = TalkingQLabel("Don't mess with Breakfast!", self)
        self.myLabel.setGeometry(50, 50, 200, 120)
        self.setGeometry(300, 200, 300, 250)
        self.show()

    def mousePressEvent(self, event):
        print
        "Well, you pressed in main window!"


class TalkingQLabel(QtGui.QLabel):
    '''QLab el that indicates when it was pressed'''

    def __init__(self, txt, parent):
        QtGui.QLabel.__init__(self, txt, parent)
        self.initUI()

    def initUI(self):
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setStyleSheet("QLabel { color: rgb(255, 255, 0); font-size: 15px; background-color: rgb(0,0,0)}")

    def mousePressEvent(self, event):
        print
        "This time you pressed in a label"


def main():
    import sys
    qtApp = QtGui.QApplication(sys.argv)
    myTalker = MainWindow()
    sys.exit(qtApp.exec_())


if __name__ == "__main__":
    main()
