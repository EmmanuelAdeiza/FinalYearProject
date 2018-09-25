from PyQt5 import QtCore
from PyQt5.QtGui import
from PyQt5.QtWidgets import QFrame, QWidget


class Widget(QQWidget):
    widgetSignal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

    def emitWidgetSignal(self):
        self.widgetSignal.emit()


class Frame(QFrame):
    frameSignal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QFrame.__init__(self, parent)

    def emitFrameSignal(self):
        self.frameSignal.emit()


class Child(Frame, Widget):
    widgetSignal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(Child, self).__init__(parent)

        self.frameSignal.connect(self.printtest)
        self.widgetSignal.connect(self.printtest)

        self.emitFrameSignal()
        self.emitWidgetSignal()

    def printtest(self):
        print("test")
