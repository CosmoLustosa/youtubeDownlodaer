# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'youtube.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from mhyt import yt_download

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(415, 322)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(415, 322))
        MainWindow.setMaximumSize(QtCore.QSize(415, 322))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_download = QtWidgets.QPushButton(self.centralwidget)
        self.btn_download.setGeometry(QtCore.QRect(150, 230, 131, 41))
        self.btn_download.setObjectName("btn_download")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 130, 47, 13))
        self.label.setObjectName("label")
        self.txt_url = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_url.setGeometry(QtCore.QRect(100, 130, 241, 20))
        self.txt_url.setObjectName("txt_url")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 190, 47, 13))
        self.label_2.setObjectName("label_2")
        self.txt_titulo = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_titulo.setGeometry(QtCore.QRect(100, 180, 241, 20))
        self.txt_titulo.setObjectName("txt_titulo")
        self.radio_mp3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_mp3.setGeometry(QtCore.QRect(60, 227, 46, 17))
        self.radio_mp3.setObjectName("radio_mp3")
        self.radio_mp4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_mp4.setGeometry(QtCore.QRect(60, 250, 46, 17))
        self.radio_mp4.setChecked(True)
        self.radio_mp4.setObjectName("radio_mp4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 20, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 10, 121, 81))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/cv/youtube.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        ########### click do botão
        self.btn_download.clicked.connect(self.download)

    def download(self):
        if self.radio_mp4.isChecked():
            url = self.txt_url.text()
            titulo = self.txt_titulo.text() + '.mp4'
            yt_download(url, titulo)
        elif self.radio_mp3.isChecked:
            try:
                url = self.txt_url.text()
                titulo = self.txt_titulo.text() + '.mp3'
                yt_download(url, titulo, ismusic=True, codec = 'mp3')
            except:
                pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YouTube Download"))
        self.btn_download.setText(_translate("MainWindow", "Download"))
        self.label.setText(_translate("MainWindow", "URL:"))
        self.label_2.setText(_translate("MainWindow", "Título:"))
        self.radio_mp3.setText(_translate("MainWindow", "MP3"))
        self.radio_mp4.setText(_translate("MainWindow", "MP4"))
        self.label_3.setText(_translate("MainWindow", "Download"))

#busca a img do youtube
import youtube

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

