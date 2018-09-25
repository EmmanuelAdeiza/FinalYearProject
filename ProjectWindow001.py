import os
import sys
import operator
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QStatusBar, QScrollArea, QFrame, QMessageBox, QFileDialog, \
    QGraphicsView, QHBoxLayout, QPushButton, QTableWidget, QTextEdit, QLabel, QTableWidgetItem, QSizePolicy, QVBoxLayout, QWidget, QAbstractItemView
from PyQt5.QtCore import QDateTime, QDate, Qt

import rake

my_database_path = 'C:\\Users\EmmaAdeiza\PycharmProjects\FinalYearProject\project_csv.csv'
debug = False

class Window(QMainWindow):
    def __init__(self, *args):
        QMainWindow.__init__(self, *args)

        self.title = 'My Extractor'
        self.top = 100
        self.left = 100
        self.width = 900
        self.height = 500
        self.setMinimumWidth(self.width)
        self.setMaximumWidth(self.width)
        self.setMinimumHeight(self.height)
        self.setMaximumHeight(self.height)
        self.setWindowIcon(QtGui.QIcon('icons/keyword_icon4.png'))
        self.layoutUI()
        self.InitWindow()
        self.show()

    def layoutUI(self):
        font1 = QtGui.QFont()
        font1.setPointSize(10)
        self.setStyleSheet("background-color: #72A2C0;")
        self.principalLayout = QVBoxLayout()
        self.setLayout(self.principalLayout)
        self.menuBarLayout = QHBoxLayout()
        self.principalLayout.addLayout(self.menuBarLayout)
        self.rightAndLeftFrameContainer = QHBoxLayout()
        self.principalLayout.addLayout(self.rightAndLeftFrameContainer)
        self.rightAndLeftFrame = QFrame(self)
        self.rightAndLeftFrame.setGeometry(0, 35, 900, 500)
        self.rightAndLeftFrame.setLayout(self.rightAndLeftFrameContainer)
        self.rightFrameLayout = QVBoxLayout()
        self.rightFrame = QFrame(self.rightAndLeftFrame)
        self.rightFrame.setFrameShape(QFrame.Panel)
        self.rightFrame.setFrameShadow(QFrame.Sunken)
        self.rightFrame.setStyleSheet("background-color: #72A2C0;")
        self.rightFrame.setLayout(self.rightFrameLayout)
        self.keywordFieldheader = QLabel('Keywords Field')
        self.keywordFieldheader.setStyleSheet(" font-size: 16px; qproperty-aligment: AlignJustify ; font-family: Garamond Bold")
        self.keywordFieldheader.setAlignment(Qt.AlignCenter)
        self.keywordField = QTextEdit()
        self.keywordField.setStyleSheet("background-color: white;")
        self.keywordField.setFont(font1)
        self.rightFrameLayout.addWidget(self.keywordFieldheader)
        self.rightFrameLayout.addWidget(self.keywordField)
        self.rightFrame.setFrameShape(QFrame.StyledPanel)
        self.rightFrame.setFrameShadow(QFrame.Raised)
        self.rightFrame.setGeometry(600, 35, 300, 500)
        self.rightFrameLayout.addSpacing(20)
        self.leftFrameLayout = QVBoxLayout()
        self.leftFrame = QFrame(self.rightAndLeftFrame)
        self.leftFrame.setFrameShape(QFrame.Panel)
        self.leftFrame.setFrameShadow(QFrame.Sunken)
        self.leftFrame.setStyleSheet("background-color: #72A2C0;")
        self.leftFrame.setLayout(self.leftFrameLayout)
        self.welcomeNote1 = QLabel()
        self.welcomeNote1.setText('You are most Welcomed Once more')
        self.welcomeNote2 = QLabel()
        self.welcomeNote2.setText('This Uses An Unsupervised Keyword Extraction Model for its principal function...')
        self.welcomeNote1.setStyleSheet(" font-size:20px ; qproperty-aligment: AlignJustify; font-family: Consolas Bold")
        self.welcomeNote2.setStyleSheet(" font-size:15px ; qproperty-aligment: AlignJustify; font-family: Garamond")
        self.welcomeNote1.setAlignment(Qt.AlignCenter)
        self.welcomeNote2.setAlignment(Qt.AlignCenter)
        self. bodyOfText = QTextEdit()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bodyOfText.setStyleSheet("background-color: white;")
        self.bodyOfText.setFont(font)
        self.bodyOfText.setCursorWidth(3)
        self.leftFrameLayout.addWidget(self.welcomeNote1)
        self.leftFrameLayout.addWidget(self.welcomeNote2)
        self.leftFrameLayout.addWidget(self.bodyOfText)
        self.leftFrame.setFrameShape(QFrame.StyledPanel)
        self.leftFrame.setFrameShadow(QFrame.Raised)
        self.leftFrame.setGeometry(0, 35, 600, 500)
        self.rightAndLeftFrameContainer.addWidget(self.leftFrame)
        self.rightAndLeftFrameContainer.addWidget(self.rightFrame)

    def OpenFile(self):
        fileName= QFileDialog.getOpenFileName(self, 'Open File', 'C:\\Users\EmmaAdeiza\PycharmProjects\FinalYearProject\Hulth2003\Testing')
        with open(fileName[0], 'r') as f :
            file_txt = f.read()
            self.bodyOfText.setText(file_txt)

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
        viewMenu.addAction("Set Interface Font...", lambda: self.setFont(QFontDialog.getFont(self)[0]))
        viewMenu.addAction("Take ScreenShoot...", lambda: self.grab().save(
            QFileDialog.getSaveFileName(self, "Save", os.path.expanduser("~"),
                                        "(*.png) PNG image file", "png")[0]))
        windowMenu = mainMenu.addMenu('Window')
        windowMenu.addAction('New Window', lambda :uuu())
        windowMenu.addAction('Minimize All')

        helpMenu = mainMenu.addMenu('Help')
        helpMenu.addAction('About App')
        helpMenu.addAction('About Developers')
        helpMenu.addAction("About Qt 5", lambda: QMessageBox.aboutQt(self))
        helpMenu.addAction("About Python 3", lambda: open_new_tab('https://www.python.org/about'))

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
        toolbar.addAction(openfolder)
        openwebpage = QAction(self, icon=QIcon('icons/webpage.png'), text="Open Webpage")
        # openwebpage.triggered.connect(self.OpenFolder)
        toolbar.addAction(openwebpage)
        analyse = QAction(self, icon=QIcon('icons/Analyse1.png'), text="Extract")
        toolbar.addAction(analyse)
        analyse.triggered.connect(self.Analyse_Text)
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

    def Analyse_Text(self):
        text = self.bodyOfText.toPlainText()
        self.sentenceList = rake.split_sentences(text)
        # print(sentenceList)
        # #stoppath = "FoxStoplist.txt" #Fox stoplist contains "numbers", so it will not find "natural numbers" like in Table 1.1
        self.stoppath = 'C:\\Users\\EmmaAdeiza\\PycharmProjects\\needed_project_main\\Ok_keyword-rake-master\\SmartStoplist.txt'  # SMART stoplist misses some of the lower-scoring keywords in Figure 1.5, which means that the top 1/3 cuts off one of the 4.0 score words in Table 1.1
        self.stopwordpattern = rake.build_stop_word_regex(self.stoppath)
        #
        # generate candidate keywords
        self.phraseList = rake.generate_candidate_keywords(self.sentenceList, self.stopwordpattern)
        #
        # # calculate individual word scores
        self.wordscores = rake.calculate_word_scores(self.phraseList)

        # generate candidate keyword scores
        self.keywordcandidates = rake.generate_candidate_keyword_scores(self.phraseList, self.wordscores)
        if debug: print(self.keywordcandidates)

        self.sortedKeywords = sorted(self.keywordcandidates.items(), key=operator.itemgetter(1), reverse=True)
        if debug: print(self.sortedKeywords)

        totalKeywords = len(self.sortedKeywords)
        if debug: print(self.totalKeywords)

        self.keyterms = ''
        for i in range(len(self.sortedKeywords[0:20])):
            self.keyterms = self.keyterms + '\n' + self.sortedKeywords[0:20][i][0]

        self.keywordField.setText(self.keyterms)

def uuu():
    App = QApplication(sys.argv)
    window = Window()


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()

    sys.exit(App.exec_())
