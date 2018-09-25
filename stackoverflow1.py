import sys

from PyQt5.QtWidgets import QApplication, QFrame, QGridLayout, QHBoxLayout, QPushButton, QSizePolicy, QSpacerItem, \
    QVBoxLayout, QWidget, QLabel


class Widget(QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent=parent)
        self.layoutUI()

    def layoutUI(self):
        self.setStyleSheet("background-color: brown;")

        self.principalLayout = QHBoxLayout(self)

        self.rightFrame = QFrame(self)
        self.rightFrame.setFrameShape(QFrame.StyledPanel)
        self.rightFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.rightFrame)
        self.gridLayout = QGridLayout()
        label1 = QLabel(self.rightFrame, text="The Right Frame ")

        self.verticalLayout.addLayout(self.gridLayout)
        self.principalLayout.addWidget(self.rightFrame)

        self.verticalLayoutR = QVBoxLayout()
        self.verticalLayoutR.setSpacing(0)
        self.exitFrame = QFrame(self)
        self.exitFrame.setStyleSheet("background-color: red;")
        self.exitverticalLayout = QVBoxLayout(self.exitFrame)
        self.exitBtn = QPushButton("Exit", self.exitFrame)
        self.exitverticalLayout.addWidget(self.exitBtn)
        self.verticalLayoutR.addWidget(self.exitFrame)

        self.numpadFrame = QFrame(self)
        self.numpadFrame.setStyleSheet("background-color: yellow;")
        self.numpadFrame.setFrameShape(QFrame.StyledPanel)
        self.numpadFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.numpadFrame)
        spacerItem = QSpacerItem(2, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QVBoxLayout()
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        label2 = QLabel(self.numpadFrame, text="The Number Pad Frame ")

        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayoutR.addWidget(self.numpadFrame)

        self.adminFrame = QFrame(self)
        self.adminFrame.setStyleSheet("background-color: blue;")
        self.adminFrame.setFrameShape(QFrame.StyledPanel)
        self.adminFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.adminFrame)
        self.adminBtn = QPushButton("Admin", self.adminFrame)
        self.horizontalLayout.addWidget(self.adminBtn)
        self.verticalLayoutR.addWidget(self.adminFrame)
        self.principalLayout.addLayout(self.verticalLayoutR)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())
