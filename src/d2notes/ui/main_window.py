# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalWidget = QWidget(self.centralwidget)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalLayout = QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalWidget = QWidget(self.verticalWidget)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.buttonPhilaeux = QPushButton(self.horizontalWidget)
        self.buttonPhilaeux.setObjectName(u"buttonPhilaeux")

        self.horizontalLayout_2.addWidget(self.buttonPhilaeux)

        self.buttonBububu = QPushButton(self.horizontalWidget)
        self.buttonBububu.setObjectName(u"buttonBububu")

        self.horizontalLayout_2.addWidget(self.buttonBububu)

        self.buttonGrubby = QPushButton(self.horizontalWidget)
        self.buttonGrubby.setObjectName(u"buttonGrubby")

        self.horizontalLayout_2.addWidget(self.buttonGrubby)

        self.inputSteamId = QLineEdit(self.horizontalWidget)
        self.inputSteamId.setObjectName(u"inputSteamId")
        self.inputSteamId.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.inputSteamId)

        self.buttonSearch = QPushButton(self.horizontalWidget)
        self.buttonSearch.setObjectName(u"buttonSearch")

        self.horizontalLayout_2.addWidget(self.buttonSearch)


        self.verticalLayout.addWidget(self.horizontalWidget)

        self.horizontalWidget1 = QWidget(self.verticalWidget)
        self.horizontalWidget1.setObjectName(u"horizontalWidget1")
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalWidget1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.horizontalWidget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.labelMatchId = QLabel(self.horizontalWidget1)
        self.labelMatchId.setObjectName(u"labelMatchId")

        self.horizontalLayout_3.addWidget(self.labelMatchId)

        self.label_3 = QLabel(self.horizontalWidget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setTextFormat(Qt.PlainText)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.labelServerId = QLabel(self.horizontalWidget1)
        self.labelServerId.setObjectName(u"labelServerId")

        self.horizontalLayout_3.addWidget(self.labelServerId)


        self.verticalLayout.addWidget(self.horizontalWidget1)

        self.line_3 = QFrame(self.verticalWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShadow(QFrame.Raised)
        self.line_3.setLineWidth(1)
        self.line_3.setMidLineWidth(1)
        self.line_3.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.line_3)

        self.gridWidget = QWidget(self.verticalWidget)
        self.gridWidget.setObjectName(u"gridWidget")
        self.gridLayout = QGridLayout(self.gridWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.gridWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_5 = QLabel(self.gridWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)

        self.label_6 = QLabel(self.gridWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 0, 3, 1, 1)

        self.label_4 = QLabel(self.gridWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)

        self.labelPlayer0Name = QLabel(self.gridWidget)
        self.labelPlayer0Name.setObjectName(u"labelPlayer0Name")

        self.gridLayout.addWidget(self.labelPlayer0Name, 1, 0, 1, 1)

        self.labelPlayer0ProName = QLabel(self.gridWidget)
        self.labelPlayer0ProName.setObjectName(u"labelPlayer0ProName")

        self.gridLayout.addWidget(self.labelPlayer0ProName, 1, 1, 1, 1)

        self.labelPlayer0CustomName = QLabel(self.gridWidget)
        self.labelPlayer0CustomName.setObjectName(u"labelPlayer0CustomName")
        self.labelPlayer0CustomName.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelPlayer0CustomName, 1, 2, 1, 1)

        self.labelPlayer0GameCount = QLabel(self.gridWidget)
        self.labelPlayer0GameCount.setObjectName(u"labelPlayer0GameCount")
        self.labelPlayer0GameCount.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelPlayer0GameCount, 1, 3, 1, 1)


        self.verticalLayout.addWidget(self.gridWidget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.verticalWidget)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Raised)
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QFrame.VLine)

        self.horizontalLayout.addWidget(self.line)

        self.verticalWidget_2 = QWidget(self.centralwidget)
        self.verticalWidget_2.setObjectName(u"verticalWidget_2")
        self.verticalLayout_2 = QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.horizontalLayout.addWidget(self.verticalWidget_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Dota 2 Notes", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.buttonPhilaeux.setText(QCoreApplication.translate("MainWindow", u"Philaeux", None))
        self.buttonBububu.setText(QCoreApplication.translate("MainWindow", u"Bububu", None))
        self.buttonGrubby.setText(QCoreApplication.translate("MainWindow", u"Grubby", None))
        self.buttonSearch.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Match ID:", None))
        self.labelMatchId.setText(QCoreApplication.translate("MainWindow", u".......................", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Server ID:", None))
        self.labelServerId.setText(QCoreApplication.translate("MainWindow", u".......................", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Custom Name", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Game Count", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Pro Name", None))
        self.labelPlayer0Name.setText("")
        self.labelPlayer0ProName.setText("")
        self.labelPlayer0CustomName.setText("")
        self.labelPlayer0GameCount.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

