import os
import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QStatusBar, QScrollArea, QFrame, QMessageBox, QFileDialog, \
    QGraphicsView, QHBoxLayout, QPushButton, QTableWidget, QTextEdit, QLabel, QTableWidgetItem, QSizePolicy, QVBoxLayout, QWidget, QAbstractItemView
from PyQt5.QtCore import QDateTime, QDate, Qt

import csv

my_database_path = 'C:\\Users\EmmaAdeiza\PycharmProjects\FinalYearProject\project_csv.csv'

class MyTable(QTableWidget):
    def __init__(self, r, c):
        super().__init__(r, c)
        self.init_ui()
        self.setGeometry(0, 35, 600, 700)
        self.col_header = ['Name', 'Type',  'Size', 'Accessed on', 'Analysed on']
        self.setHorizontalHeaderLabels(self.col_header)
        # self.setDisabled(True)
        self.setColumnWidth(0, 200)
        self.setColumnWidth(1, 40)
        self.setColumnWidth(2, 60)
        self.setColumnWidth(3,140)
        self.setColumnWidth(4, 140)
        # self.setShowGrid(False)
        self.setGridStyle(Qt.DashDotDotLine)
        # self.setAlternatingRowColors(True)
        self.verticalHeader().setVisible(False)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        # self.addRow('MyTrial', 'Txt', '22.30 Mb')
        # self.open_sheet()

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

    def open_sheet(self):
        if my_database_path != '' :
            with open(my_database_path, newline= '') as csv_file :
                self.setRowCount(0)
                self.setColumnCount(5)
                my_file = csv.reader(csv_file, dialect = 'excel')
                for row_data in my_file:
                    row = self.rowCount()
                    self.insertRow(row)
                    if len(row_data) > 10 :
                        self.setColumnCount(len(row_data))
                    for column, stuff in enumerate(row_data):
                        item = QTableWidgetItem(stuff)
                        self.setItem(row, column, item)

    # def save_sheet(self):
    #     if my_database_path != '':
    #         with open(my_database_path, 'a') as csv_file:
    #             writer = csv.writer(csv_file, dialect = 'excel')
    #             for row in range(self.rowCount()):
    #                 row_data = []
    #                 for column in range(self.columnCount()):
    #                     item = self.item(row, column)
    #                     if item is not None:
    #                         row_data.append(item.text())
    #                     else :
    #                         row_data.append('')
    #                 writer.writerow(row_data)
    #
    # def addRow(self, name, type, size):
    #
    #     self.setCurrentCell(counter,0)
    #     self.setItem(counter,0, QTableWidgetItem(name))
    #     self.setCurrentCell(counter, 1)
    #     self.setItem(counter, 1, QTableWidgetItem(type))
    #     self.setCurrentCell(counter, 2)
    #     self.setItem(counter, 2, QTableWidgetItem(size))
    #     self.setCurrentCell(counter, 3)
    #     date = QDate.currentDate()
    #     date_accessed = date.toString()
    #     self.setItem(counter, 3, QTableWidgetItem(date_accessed))
    #     self.setCurrentCell(counter, 4)
    #     analysed = False
    #     self.setItem(counter, 4, QTableWidgetItem(analysed))

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
        self.rightAndLeftFrame.setGeometry(0, 35, 800, 700)
        self.rightAndLeftFrame.setStyleSheet("background-color: #;")
        self.rightAndLeftFrame.setLayout(self.rightAndLeftFrameContainer)
        self.rightFrameLayout = QVBoxLayout()
        self.rightFrame = QFrame(self.rightAndLeftFrame)
        self.rightFrame.setFrameShape(QFrame.Panel)
        self.rightFrame.setFrameShadow(QFrame.Sunken)
        self.rightFrame.setStyleSheet("background-color: #72A2C0;")
        self.rightFrame.setLayout(self.rightFrameLayout)
        self.keywordFieldheader = QLabel('Keywords Field')
        # self.keywordFieldheader.setFont(QFont.)
        # self.keywordFieldheader.setFont(QFont.Bold)
        self.keywordField = QTextEdit()
        self.rightFrameLayout.addWidget(self.keywordFieldheader)
        self.rightFrameLayout.addWidget(self.keywordField)
        self.rightFrame.setFrameShape(QFrame.StyledPanel)
        self.rightFrame.setFrameShadow(QFrame.Raised)
        self.rightFrame.setGeometry(600, 35, 200, 700)
        self.rightFrameLayout.addSpacing(20)
        self.leftFrameLayout = QVBoxLayout()
        self.leftFrame = QFrame(self.rightAndLeftFrame)
        self.leftFrame.setFrameShape(QFrame.Panel)
        self.leftFrame.setFrameShadow(QFrame.Sunken)
        self.leftFrame.setStyleSheet("background-color: #B5C1B4;")
        self.leftFrame.setLayout(self.leftFrameLayout)
        self.leftFrame.setFrameShape(QFrame.StyledPanel)
        self.leftFrame.setFrameShadow(QFrame.Raised)
        self.leftFrame.setGeometry(0, 35, 600, 700)
        self.form = MyTable(0, 5)
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
        step_to_greater_unit = 1024.
        fileSize = float(fileSize)
        unit = 'Bytes'
        if (fileSize / step_to_greater_unit) >= 1:
            fileSize /= step_to_greater_unit
            unit = 'KB'
        if (fileSize / step_to_greater_unit) >= 1:
            fileSize /= step_to_greater_unit
            unit = 'MB'
        if (fileSize / step_to_greater_unit) >= 1:
            fileSize /= step_to_greater_unit
            unit = 'GB'
        if (fileSize / step_to_greater_unit) >= 1:
            fileSize /= step_to_greater_unit
            unit = 'TB'
        precision = 1
        fileSize = round(fileSize, precision)
        fileSize = str(fileSize) + ' ' + unit
        print(fileSize)
        print(fileName)

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
        exit.triggered.connect(self.CloseApp)
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

    def CloseApp(self):
        reply = QMessageBox.question(self, 'Close Message', "Are You Sure To Close Window",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()

if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()

    sys.exit(App.exec_())
