import os
import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QStatusBar, QScrollArea, QFrame, QSplitter, QFileDialog, \
    QGraphicsView, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QSizePolicy, QVBoxLayout, QWidget

class MyTable(QTableWidget):
    def __init__(self, r, c):
        super().__init__(r, c)
        self.init_ui()

    def init_ui(self):
        self.cellChanged.connect(self.c_current)
        self.show()

    def c_current(self):
        row = self.currentRow()
        col = self.currentColumn()
        value = self.item(row, col)
        value = value.text()
        print('The current cell is ', row, ', ', col)
        print("In this cell we have : ", value)

class contentFrame(QFrame):

    def __init__(self, parent=None):
        QFrame.__init__(self, parent)

        self.width = 420
        self.height = 50
        self.setMinimumWidth(self.width)
        self.setMaximumWidth(self.width)
        self.setMinimumHeight(self.height)
        self.setMaximumHeight(self.height)
        self.setStyleSheet("background-color: #F1E0D6;")
        # l1 = QLabel(self)
        # l1.setPixmap(QPixmap("icons/pdf6.PNG"))
        # l1.move(0,90)
        # self.otherDetailFrameLayout= QVBoxLayout()
        # self.otherDetailFrame = QFrame(self)
        # self.otherDetailFrame.setStyleSheet("background-color: #ABA6BF;")
        # self.otherDetailFrame.setGeometry(75, 85, 350,20)
        # self.otherDetailFrame1 = QFrame(self)
        # self.otherDetailFrame1.setStyleSheet("background-color: #3BA63F;")
        # self.otherDetailFrame1.setGeometry(75, 110, 350,20)
        # self.otherDetailFrameLayout.addWidget(self.otherDetailFrame)
        # self.otherDetailFrameLayout.addWidget(self.otherDetailFrame1)
        # layerout = QHBoxLayout()
        # self.otherDetailFrame.setLayout(layerout)
        # self.otherDetailFrame1.setLayout(layerout)
        # self.progress = QProgressBar(self.otherDetailFrame1)
        # # self.progress.setFixedSize(200, 20)
        # # self.progress.setAlignment([Qt.Alignment, Qt.AlignRight])
        # self.progress.setGeometry(100, 0, 200, 20)
        # self.pdfName = QLabel(self.otherDetailFrame, text='dfbdbvfdcxvd')


class Window(QMainWindow, QGraphicsView):
    def __init__(self, *args):
        QMainWindow.__init__(self, *args)

        self.title = 'My Extractor'
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 700
        self.setMinimumWidth(self.width)
        self.setMaximumWidth(self.width)
        self.setMinimumHeight(self.height)
        self.setMaximumHeight(self.height)
        self.setWindowIcon(QtGui.QIcon('icons/keyword_icon4.png'))

        self.layoutUI()
        self.InitWindow()

        self.show()

    def layoutUI(self):
        # self.setStyleSheet("background-color: #0486DB;")
        # self.setStyleSheet("background-color: #72A2C0;")
        self.setStyleSheet("background-color: #1D65A6;")

        self.principalLayout = QVBoxLayout()
        self.setLayout(self.principalLayout)
        self.menuBarLayout = QHBoxLayout()
        self.principalLayout.addLayout(self.menuBarLayout)
        self.rightAndLeftFrameContainer = QHBoxLayout()
        self.principalLayout.addLayout(self.rightAndLeftFrameContainer)
        self.rightAndLeftFrame = QFrame(self)
        self.rightAndLeftFrame.setGeometry(0, 0, 800, 700)
        self.rightAndLeftFrame.setStyleSheet("background-color: #;")
        self.rightAndLeftFrame.setLayout(self.rightAndLeftFrameContainer)

        self.splitter = QSplitter(self.rightAndLeftFrame)

        self.rightFrameLayout = QVBoxLayout()
        self.rightFrame = QFrame(self.rightAndLeftFrame)
        self.rightFrame.setFrameShape(QFrame.Panel)
        self.rightFrame.setFrameShadow(QFrame.Sunken)
        self.rightFrame.setStyleSheet("background-color: black;")
        self.rightFrame.setLayout(self.rightFrameLayout)
        self.exitBtn = QPushButton("Other Side of Life")
        self.rightFrameLayout.addWidget(self.exitBtn)
        self.rightFrame.setFrameShape(QFrame.StyledPanel)
        self.rightFrame.setFrameShadow(QFrame.Raised)
        self.rightFrame.setGeometry(450, 0, 350, 700)
        self.rightFrameLayout.addSpacing(20)

        self.form = MyTable(10, 10)

        self.leftFrameLayout = QVBoxLayout()
        self.leftFrameLayout.setAlignment(Qt.AlignTop)
        self.leftFrameLayout.addStretch()
        self.leftFrameScrollArea = QScrollArea(self.rightAndLeftFrame)
        self.leftFrame = QFrame()
        self.leftFrameScrollArea.setWidget(self.leftFrame)
        self.leftFrameScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.leftFrameScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rightFrame.setFrameShape(QFrame.Box)
        self.leftFrameScrollArea.setGeometry(0, 0, 450, 700)
        self.leftFrameScrollArea.setLayout(self.leftFrameLayout)
        self.leftFrame.setGeometry(0, 0, 430, 700)
        self.leftFrameLayout.addWidget(self.form)

        self.rightAndLeftFrameContainer.addWidget(self.leftFrame)
        self.rightAndLeftFrameContainer.addWidget(self.rightFrame)

    def bytes_2_human_readable(self, size):
        step_to_greater_unit = 1024.

        size = float(size)
        unit = 'Bytes'
        if (size / step_to_greater_unit) >= 1:
            size /= step_to_greater_unit
            unit = 'KB'
        if (size / step_to_greater_unit) >= 1:
            size /= step_to_greater_unit
            unit = 'MB'
        if (size / step_to_greater_unit) >= 1:
            size /= step_to_greater_unit
            unit = 'GB'
        if (size / step_to_greater_unit) >= 1:
            size /= step_to_greater_unit
            unit = 'TB'
        precision = 1
        size = round(size, precision)
        size = str(size) + ' ' + unit
        return size

    def OpenFile(self):
        filePath, _ = QFileDialog.getOpenFileName(self, 'Open File')
        if filePath != "":
            info = QFileInfo(filePath)
            fileSize = info.size()
            fileName = info.fileName()

        fileSize = self.bytes_2_human_readable(fileSize)
        print(fileSize)
        print(fileName)
        frea = Frame(self.leftFrame)
        frea.PdfDetails(fileName, fileSize)
        frea.show()

    def OpenFolder(self):
        folderName = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        # return fileName

    def InitWindow(self):
        mainMenu = self.menuBar()
        mainMenu.setToolTip('This is a <b>MenuBar</b> widget')
        self.menuBarLayout.addWidget(mainMenu)
        fileMenu = mainMenu.addMenu('File')
        OpenFile = QAction('Open File', self)
        fileMenu.addAction(OpenFile)
        fileMenu.addAction('Open Folder')
        fileMenu.addAction('Save File')
        fileMenu.addAction('Save File as')
        fileMenu.addAction('Exit')

        editMenu = mainMenu.addMenu('Edit')
        editMenu.addAction('Cut')
        editMenu.addAction('Copy')
        editMenu.addAction('Paste')
        editMenu.addAction('Delete')
        editMenu.addAction('Preferences')

        viewMenu = mainMenu.addMenu('View')
        viewMenu.addAction('Rotate View')
        viewMenu.addAction('Page Navigation')
        viewMenu.addAction('Page Display')
        viewMenu.addAction('Zoom')
        viewMenu.addAction("Set Interface Font...", lambda:
        self.setFont(QFontDialog.getFont(self)[0]))
        viewMenu.addAction("Take ScreenShoot...", lambda: self.grab().save(
            QFileDialog.getSaveFileName(self, "Save", os.path.expanduser("~"),
                                        "(*.png) PNG image file", "png")[0]))

        windowMenu = mainMenu.addMenu('Window')
        windowMenu.addAction('New Window')
        windowMenu.addAction('Minimize All')

        helpMenu = mainMenu.addMenu('Help')
        helpMenu.addAction('About App')
        helpMenu.addAction('About Developers')
        helpMenu.addAction("About Qt 5", lambda: QMessageBox.aboutQt(self))
        helpMenu.addAction("About Python 3", lambda:
        open_new_tab('https://www.python.org/about'))

        self.setLayout(self.menuBarLayout)
        toolbar_layout = QVBoxLayout()

        self.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.setIconSize(QSize(50, 30))
        toolbar = self.addToolBar("File")
        toolbar.setMovable(False)
        openfile = QAction(self, icon=QIcon("icons/File1.png"), text="Open File ")
        openfile.triggered.connect(self.OpenFile)
        toolbar.addAction(openfile)
        openfolder = QAction(self, icon=QIcon('icons/Folder1.png'), text="Open Folder")
        openfolder.triggered.connect(self.OpenFolder)
        openwebpage = QAction(self, icon=QIcon('icons/webpage.png'), text="Open Webpage")
        # openwebpage.triggered.connect(self.OpenFolder)
        toolbar.addAction(openfolder)
        toolbar.addAction(openwebpage)
        exit = QAction(self, icon=QIcon('icons/Exit2.png'), text="Exit")
        toolbar.addAction(exit)
        exit.triggered.connect(sys.exit)
        restart = QAction(self, icon=QIcon('icons/Restart1.png'), text="Restart")
        toolbar.addAction(restart)
        # exit.triggered.connect(restartMe)
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # Study this later
        toolbar.addWidget(spacer)
        setting = QAction(self, icon=QIcon('icons/Support3.png'), text="Preferences")
        toolbar.addAction(setting)
        help = QAction(self, icon=QIcon('icons/Help1.png'), text="Get Assistance")
        toolbar.addAction(help)
        self.setLayout(toolbar_layout)

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage(" This is My Status Bar's Message")

        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()

    sys.exit(App.exec_())
