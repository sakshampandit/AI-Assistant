from ZenUi import Ui_MainWindow 
from PyQt5 import QtGui , QtCore , QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt,QTimer,QTime,QDate
from PyQt5.uic import loadUiType
import zen
import sys
import os
import webbrowser as web


# import Pylance


class MainThread(QThread):

    def __init__(self):

        super(MainThread,self).__init__()

    def run(self):
        zen.taskexecution()

startExe = MainThread()


class Gui_Start(QMainWindow):

    def __init__(self):  

        super().__init__()
        self.gui=Ui_MainWindow()
        self.gui.setupUi(self)

        self.gui.pushButton_start.clicked.connect(self.startTask)
        self.gui.pushButton_exit.clicked.connect(self.close)
        self.gui.pushButton_chrome.clicked.connect(self.chrome_app)
        self.gui.pushbutton_whatsapp.clicked.connect(self.whatsapp_app)
        self.gui.pushButton_youtube.clicked.connect(self.yt_app)

    def chrome_app(self):
        zen.Speak("Opening Chrome..")
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    def yt_app(self):
        web.open("https://www.youtube.com/")

    def whatsapp_app(self):
        web.open("https://www.whatsapp.com/")

    def startTask(self):
        self.gui.label1= QtGui.QMovie(".//G.U.I Material//B.G//Iron_Template_1.gif")
        self.gui.Gif_1.setMovie(self.gui.label1)
        self.gui.label1.start()

        self.gui.label2= QtGui.QMovie(".//G.U.I Material//ExtraGui//live.gif")
        self.gui.Gif_2.setMovie(self.gui.label2)
        self.gui.label2.start()

        self.gui.label3= QtGui.QMovie(".//G.U.I Material//VoiceReg/Siri_1.gif")
        self.gui.Gif_3.setMovie(self.gui.label3)
        self.gui.label3.start()

        self.gui.label4= QtGui.QMovie(".//G.U.I Material//ExtraGui//Earth.gif")
        self.gui.Gif_4.setMovie(self.gui.label4)
        self.gui.label4.start()

        startExe.start()

GuiApp = QApplication(sys.argv)
zen_gui=Gui_Start()
zen_gui.show()
exit(GuiApp.exec_())













