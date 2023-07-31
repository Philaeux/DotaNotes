# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_window.ui'
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

from d2notes.ui.clickable_label import ClickableLabel

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 800)
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

        self.horizontalWidget2 = QWidget(self.verticalWidget)
        self.horizontalWidget2.setObjectName(u"horizontalWidget2")
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalWidget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.horizontalWidget2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.labelMatchId = QLabel(self.horizontalWidget2)
        self.labelMatchId.setObjectName(u"labelMatchId")

        self.horizontalLayout_3.addWidget(self.labelMatchId)

        self.label_3 = QLabel(self.horizontalWidget2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setTextFormat(Qt.PlainText)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.labelServerId = QLabel(self.horizontalWidget2)
        self.labelServerId.setObjectName(u"labelServerId")

        self.horizontalLayout_3.addWidget(self.labelServerId)


        self.verticalLayout.addWidget(self.horizontalWidget2)

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
        self.labelPlayer4GameCount = ClickableLabel(self.gridWidget)
        self.labelPlayer4GameCount.setObjectName(u"labelPlayer4GameCount")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelPlayer4GameCount.sizePolicy().hasHeightForWidth())
        self.labelPlayer4GameCount.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.labelPlayer4GameCount, 6, 3, 1, 1)

        self.labelPlayer4Name = ClickableLabel(self.gridWidget)
        self.labelPlayer4Name.setObjectName(u"labelPlayer4Name")
        sizePolicy.setHeightForWidth(self.labelPlayer4Name.sizePolicy().hasHeightForWidth())
        self.labelPlayer4Name.setSizePolicy(sizePolicy)
        self.labelPlayer4Name.setMinimumSize(QSize(160, 40))

        self.gridLayout.addWidget(self.labelPlayer4Name, 6, 0, 1, 1)

        self.labelPlayer2GameCount = ClickableLabel(self.gridWidget)
        self.labelPlayer2GameCount.setObjectName(u"labelPlayer2GameCount")
        sizePolicy.setHeightForWidth(self.labelPlayer2GameCount.sizePolicy().hasHeightForWidth())
        self.labelPlayer2GameCount.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.labelPlayer2GameCount, 4, 3, 1, 1)

        self.labelPlayer3ProName = ClickableLabel(self.gridWidget)
        self.labelPlayer3ProName.setObjectName(u"labelPlayer3ProName")
        sizePolicy.setHeightForWidth(self.labelPlayer3ProName.sizePolicy().hasHeightForWidth())
        self.labelPlayer3ProName.setSizePolicy(sizePolicy)
        self.labelPlayer3ProName.setMinimumSize(QSize(160, 40))

        self.gridLayout.addWidget(self.labelPlayer3ProName, 5, 1, 1, 1)

        self.labelPlayer4ProName = ClickableLabel(self.gridWidget)
        self.labelPlayer4ProName.setObjectName(u"labelPlayer4ProName")
        sizePolicy.setHeightForWidth(self.labelPlayer4ProName.sizePolicy().hasHeightForWidth())
        self.labelPlayer4ProName.setSizePolicy(sizePolicy)
        self.labelPlayer4ProName.setMinimumSize(QSize(160, 40))

        self.gridLayout.addWidget(self.labelPlayer4ProName, 6, 1, 1, 1)

        self.labelPlayer4CustomName = ClickableLabel(self.gridWidget)
        self.labelPlayer4CustomName.setObjectName(u"labelPlayer4CustomName")
        sizePolicy.setHeightForWidth(self.labelPlayer4CustomName.sizePolicy().hasHeightForWidth())
        self.labelPlayer4CustomName.setSizePolicy(sizePolicy)
        self.labelPlayer4CustomName.setMinimumSize(QSize(160, 40))

        self.gridLayout.addWidget(self.labelPlayer4CustomName, 6, 2, 1, 1)

        self.labelPlayer3CustomName = ClickableLabel(self.gridWidget)
        self.labelPlayer3CustomName.setObjectName(u"labelPlayer3CustomName")
        sizePolicy.setHeightForWidth(self.labelPlayer3CustomName.sizePolicy().hasHeightForWidth())
        self.labelPlayer3CustomName.setSizePolicy(sizePolicy)
        self.labelPlayer3CustomName.setMinimumSize(QSize(160, 40))

        self.gridLayout.addWidget(self.labelPlayer3CustomName, 5, 2, 1, 1)

        self.labelPlayer1ProName = ClickableLabel(self.gridWidget)
        self.labelPlayer1ProName.setObjectName(u"labelPlayer1ProName")
        sizePolicy.setHeightForWidth(self.labelPlayer1ProName.sizePolicy().hasHeightForWidth())
        self.labelPlayer1ProName.setSizePolicy(sizePolicy)
        self.labelPlayer1ProName.setMinimumSize(QSize(160, 40))

        self.gridLayout.addWidget(self.labelPlayer1ProName, 3, 1, 1, 1)

        self.labelPlayer1CustomName = ClickableLabel(self.gridWidget)
        self.labelPlayer1CustomName.setObjectName(u"labelPlayer1CustomName")
        sizePolicy.setHeightForWidth(self.labelPlayer1CustomName.sizePolicy().hasHeightForWidth())
        self.labelPlayer1CustomName.setSizePolicy(sizePolicy)
        self.labelPlayer1CustomName.setMinimumSize(QSize(160, 40))

        self.gridLayout.addWidget(self.labelPlayer1CustomName, 3, 2, 1, 1)

        self.labelPlayer1GameCount = ClickableLabel(self.gridWidget)
        self.labelPlayer1GameCount.setObjectName(u"labelPlayer1GameCount")
        sizePolicy.setHeightForWidth(self.labelPlayer1GameCount.sizePolicy().hasHeightForWidth())
        self.labelPlayer1GameCount.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.labelPlayer1GameCount, 3, 3, 1, 1)

        self.labelPlayer2Name = ClickableLabel(self.gridWidget)
        self.labelPlayer2Name.setObjectName(u"labelPlayer2Name")
        sizePolicy.setHeightForWidth(self.labelPlayer2Name.sizePolicy().hasHeightForWidth())
        self.labelPlayer2Name.setSizePolicy(sizePolicy)
        self.labelPlayer2Name.setMinimumSize(QSize(160, 40))

        self.gridLayout.addWidget(self.labelPlayer2Name, 4, 0, 1, 1)

        self.labelPlayer3Name = ClickableLabel(self.gridWidget)
        self.labelPlayer3Name.setObjectName(u"labelPlayer3Name")
        sizePolicy.setHeightForWidth(self.labelPlayer3Name.sizePolicy().hasHeightForWidth())
        self.labelPlayer3Name.setSizePolicy(sizePolicy)
        self.labelPlayer3Name.setMinimumSize(QSize(160, 40))

        self.gridLayout.addWidget(self.labelPlayer3Name, 5, 0, 1, 1)

        self.labelPlayer2ProName = ClickableLabel(self.gridWidget)
        self.labelPlayer2ProName.setObjectName(u"labelPlayer2ProName")
        sizePolicy.setHeightForWidth(self.labelPlayer2ProName.sizePolicy().hasHeightForWidth())
        self.labelPlayer2ProName.setSizePolicy(sizePolicy)
        self.labelPlayer2ProName.setMinimumSize(QSize(160, 40))

        self.gridLayout.addWidget(self.labelPlayer2ProName, 4, 1, 1, 1)

        self.labelPlayer2CustomName = ClickableLabel(self.gridWidget)
        self.labelPlayer2CustomName.setObjectName(u"labelPlayer2CustomName")
        sizePolicy.setHeightForWidth(self.labelPlayer2CustomName.sizePolicy().hasHeightForWidth())
        self.labelPlayer2CustomName.setSizePolicy(sizePolicy)
        self.labelPlayer2CustomName.setMinimumSize(QSize(160, 40))

        self.gridLayout.addWidget(self.labelPlayer2CustomName, 4, 2, 1, 1)

        self.label_5 = QLabel(self.gridWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(160, 0))
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)

        self.labelPlayer0Name = ClickableLabel(self.gridWidget)
        self.labelPlayer0Name.setObjectName(u"labelPlayer0Name")
        sizePolicy.setHeightForWidth(self.labelPlayer0Name.sizePolicy().hasHeightForWidth())
        self.labelPlayer0Name.setSizePolicy(sizePolicy)
        self.labelPlayer0Name.setMinimumSize(QSize(160, 40))

        self.gridLayout.addWidget(self.labelPlayer0Name, 2, 0, 1, 1)

        self.label = QLabel(self.gridWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(160, 40))
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.labelPlayer0ProName = ClickableLabel(self.gridWidget)
        self.labelPlayer0ProName.setObjectName(u"labelPlayer0ProName")
        sizePolicy.setHeightForWidth(self.labelPlayer0ProName.sizePolicy().hasHeightForWidth())
        self.labelPlayer0ProName.setSizePolicy(sizePolicy)
        self.labelPlayer0ProName.setMinimumSize(QSize(160, 40))

        self.gridLayout.addWidget(self.labelPlayer0ProName, 2, 1, 1, 1)

        self.label_6 = QLabel(self.gridWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 60))
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 0, 3, 1, 1)

        self.labelPlayer0CustomName = ClickableLabel(self.gridWidget)
        self.labelPlayer0CustomName.setObjectName(u"labelPlayer0CustomName")
        sizePolicy.setHeightForWidth(self.labelPlayer0CustomName.sizePolicy().hasHeightForWidth())
        self.labelPlayer0CustomName.setSizePolicy(sizePolicy)
        self.labelPlayer0CustomName.setMinimumSize(QSize(160, 40))
        self.labelPlayer0CustomName.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelPlayer0CustomName, 2, 2, 1, 1)

        self.labelPlayer0GameCount = ClickableLabel(self.gridWidget)
        self.labelPlayer0GameCount.setObjectName(u"labelPlayer0GameCount")
        sizePolicy.setHeightForWidth(self.labelPlayer0GameCount.sizePolicy().hasHeightForWidth())
        self.labelPlayer0GameCount.setSizePolicy(sizePolicy)
        self.labelPlayer0GameCount.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelPlayer0GameCount, 2, 3, 1, 1)

        self.line_2 = QFrame(self.gridWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 4)

        self.label_4 = QLabel(self.gridWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(160, 0))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)

        self.labelPlayer3GameCount = ClickableLabel(self.gridWidget)
        self.labelPlayer3GameCount.setObjectName(u"labelPlayer3GameCount")
        sizePolicy.setHeightForWidth(self.labelPlayer3GameCount.sizePolicy().hasHeightForWidth())
        self.labelPlayer3GameCount.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.labelPlayer3GameCount, 5, 3, 1, 1)

        self.labelPlayer1Name = ClickableLabel(self.gridWidget)
        self.labelPlayer1Name.setObjectName(u"labelPlayer1Name")
        sizePolicy.setHeightForWidth(self.labelPlayer1Name.sizePolicy().hasHeightForWidth())
        self.labelPlayer1Name.setSizePolicy(sizePolicy)
        self.labelPlayer1Name.setMinimumSize(QSize(160, 40))

        self.gridLayout.addWidget(self.labelPlayer1Name, 3, 0, 1, 1)

        self.line_4 = QFrame(self.gridWidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_4, 7, 0, 1, 4)

        self.labelPlayer5ProName = ClickableLabel(self.gridWidget)
        self.labelPlayer5ProName.setObjectName(u"labelPlayer5ProName")
        sizePolicy.setHeightForWidth(self.labelPlayer5ProName.sizePolicy().hasHeightForWidth())
        self.labelPlayer5ProName.setSizePolicy(sizePolicy)
        self.labelPlayer5ProName.setMinimumSize(QSize(160, 40))

        self.gridLayout.addWidget(self.labelPlayer5ProName, 8, 1, 1, 1)

        self.labelPlayer5Name = ClickableLabel(self.gridWidget)
        self.labelPlayer5Name.setObjectName(u"labelPlayer5Name")
        sizePolicy.setHeightForWidth(self.labelPlayer5Name.sizePolicy().hasHeightForWidth())
        self.labelPlayer5Name.setSizePolicy(sizePolicy)
        self.labelPlayer5Name.setMinimumSize(QSize(160, 40))

        self.gridLayout.addWidget(self.labelPlayer5Name, 8, 0, 1, 1)

        self.labelPlayer6ProName = ClickableLabel(self.gridWidget)
        self.labelPlayer6ProName.setObjectName(u"labelPlayer6ProName")
        sizePolicy.setHeightForWidth(self.labelPlayer6ProName.sizePolicy().hasHeightForWidth())
        self.labelPlayer6ProName.setSizePolicy(sizePolicy)
        self.labelPlayer6ProName.setMinimumSize(QSize(160, 40))

        self.gridLayout.addWidget(self.labelPlayer6ProName, 9, 1, 1, 1)

        self.labelPlayer6Name = ClickableLabel(self.gridWidget)
        self.labelPlayer6Name.setObjectName(u"labelPlayer6Name")
        sizePolicy.setHeightForWidth(self.labelPlayer6Name.sizePolicy().hasHeightForWidth())
        self.labelPlayer6Name.setSizePolicy(sizePolicy)
        self.labelPlayer6Name.setMinimumSize(QSize(160, 40))

        self.gridLayout.addWidget(self.labelPlayer6Name, 9, 0, 1, 1)

        self.labelPlayer7ProName = ClickableLabel(self.gridWidget)
        self.labelPlayer7ProName.setObjectName(u"labelPlayer7ProName")
        sizePolicy.setHeightForWidth(self.labelPlayer7ProName.sizePolicy().hasHeightForWidth())
        self.labelPlayer7ProName.setSizePolicy(sizePolicy)
        self.labelPlayer7ProName.setMinimumSize(QSize(160, 40))

        self.gridLayout.addWidget(self.labelPlayer7ProName, 10, 1, 1, 1)

        self.labelPlayer6CustomName = ClickableLabel(self.gridWidget)
        self.labelPlayer6CustomName.setObjectName(u"labelPlayer6CustomName")
        sizePolicy.setHeightForWidth(self.labelPlayer6CustomName.sizePolicy().hasHeightForWidth())
        self.labelPlayer6CustomName.setSizePolicy(sizePolicy)
        self.labelPlayer6CustomName.setMinimumSize(QSize(160, 40))

        self.gridLayout.addWidget(self.labelPlayer6CustomName, 9, 2, 1, 1)

        self.labelPlayer5GameCount = ClickableLabel(self.gridWidget)
        self.labelPlayer5GameCount.setObjectName(u"labelPlayer5GameCount")
        sizePolicy.setHeightForWidth(self.labelPlayer5GameCount.sizePolicy().hasHeightForWidth())
        self.labelPlayer5GameCount.setSizePolicy(sizePolicy)
        self.labelPlayer5GameCount.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelPlayer5GameCount, 8, 3, 1, 1)

        self.labelPlayer5CustomName = ClickableLabel(self.gridWidget)
        self.labelPlayer5CustomName.setObjectName(u"labelPlayer5CustomName")
        sizePolicy.setHeightForWidth(self.labelPlayer5CustomName.sizePolicy().hasHeightForWidth())
        self.labelPlayer5CustomName.setSizePolicy(sizePolicy)
        self.labelPlayer5CustomName.setMinimumSize(QSize(160, 40))

        self.gridLayout.addWidget(self.labelPlayer5CustomName, 8, 2, 1, 1)

        self.labelPlayer6GameCount = ClickableLabel(self.gridWidget)
        self.labelPlayer6GameCount.setObjectName(u"labelPlayer6GameCount")
        sizePolicy.setHeightForWidth(self.labelPlayer6GameCount.sizePolicy().hasHeightForWidth())
        self.labelPlayer6GameCount.setSizePolicy(sizePolicy)
        self.labelPlayer6GameCount.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelPlayer6GameCount, 9, 3, 1, 1)

        self.labelPlayer7Name = ClickableLabel(self.gridWidget)
        self.labelPlayer7Name.setObjectName(u"labelPlayer7Name")
        sizePolicy.setHeightForWidth(self.labelPlayer7Name.sizePolicy().hasHeightForWidth())
        self.labelPlayer7Name.setSizePolicy(sizePolicy)
        self.labelPlayer7Name.setMinimumSize(QSize(160, 40))

        self.gridLayout.addWidget(self.labelPlayer7Name, 10, 0, 1, 1)

        self.labelPlayer8ProName = ClickableLabel(self.gridWidget)
        self.labelPlayer8ProName.setObjectName(u"labelPlayer8ProName")
        sizePolicy.setHeightForWidth(self.labelPlayer8ProName.sizePolicy().hasHeightForWidth())
        self.labelPlayer8ProName.setSizePolicy(sizePolicy)
        self.labelPlayer8ProName.setMinimumSize(QSize(160, 40))

        self.gridLayout.addWidget(self.labelPlayer8ProName, 11, 1, 1, 1)

        self.labelPlayer8CustomName = ClickableLabel(self.gridWidget)
        self.labelPlayer8CustomName.setObjectName(u"labelPlayer8CustomName")
        sizePolicy.setHeightForWidth(self.labelPlayer8CustomName.sizePolicy().hasHeightForWidth())
        self.labelPlayer8CustomName.setSizePolicy(sizePolicy)
        self.labelPlayer8CustomName.setMinimumSize(QSize(160, 40))

        self.gridLayout.addWidget(self.labelPlayer8CustomName, 11, 2, 1, 1)

        self.labelPlayer8Name = ClickableLabel(self.gridWidget)
        self.labelPlayer8Name.setObjectName(u"labelPlayer8Name")
        sizePolicy.setHeightForWidth(self.labelPlayer8Name.sizePolicy().hasHeightForWidth())
        self.labelPlayer8Name.setSizePolicy(sizePolicy)
        self.labelPlayer8Name.setMinimumSize(QSize(160, 40))

        self.gridLayout.addWidget(self.labelPlayer8Name, 11, 0, 1, 1)

        self.labelPlayer7CustomName = ClickableLabel(self.gridWidget)
        self.labelPlayer7CustomName.setObjectName(u"labelPlayer7CustomName")
        sizePolicy.setHeightForWidth(self.labelPlayer7CustomName.sizePolicy().hasHeightForWidth())
        self.labelPlayer7CustomName.setSizePolicy(sizePolicy)
        self.labelPlayer7CustomName.setMinimumSize(QSize(160, 40))

        self.gridLayout.addWidget(self.labelPlayer7CustomName, 10, 2, 1, 1)

        self.labelPlayer7GameCount = ClickableLabel(self.gridWidget)
        self.labelPlayer7GameCount.setObjectName(u"labelPlayer7GameCount")
        sizePolicy.setHeightForWidth(self.labelPlayer7GameCount.sizePolicy().hasHeightForWidth())
        self.labelPlayer7GameCount.setSizePolicy(sizePolicy)
        self.labelPlayer7GameCount.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelPlayer7GameCount, 10, 3, 1, 1)

        self.labelPlayer8GameCount = ClickableLabel(self.gridWidget)
        self.labelPlayer8GameCount.setObjectName(u"labelPlayer8GameCount")
        sizePolicy.setHeightForWidth(self.labelPlayer8GameCount.sizePolicy().hasHeightForWidth())
        self.labelPlayer8GameCount.setSizePolicy(sizePolicy)
        self.labelPlayer8GameCount.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelPlayer8GameCount, 11, 3, 1, 1)

        self.labelPlayer9Name = ClickableLabel(self.gridWidget)
        self.labelPlayer9Name.setObjectName(u"labelPlayer9Name")
        sizePolicy.setHeightForWidth(self.labelPlayer9Name.sizePolicy().hasHeightForWidth())
        self.labelPlayer9Name.setSizePolicy(sizePolicy)
        self.labelPlayer9Name.setMinimumSize(QSize(160, 40))

        self.gridLayout.addWidget(self.labelPlayer9Name, 12, 0, 1, 1)

        self.labelPlayer9ProName = ClickableLabel(self.gridWidget)
        self.labelPlayer9ProName.setObjectName(u"labelPlayer9ProName")
        sizePolicy.setHeightForWidth(self.labelPlayer9ProName.sizePolicy().hasHeightForWidth())
        self.labelPlayer9ProName.setSizePolicy(sizePolicy)
        self.labelPlayer9ProName.setMinimumSize(QSize(160, 40))

        self.gridLayout.addWidget(self.labelPlayer9ProName, 12, 1, 1, 1)

        self.labelPlayer9CustomName = ClickableLabel(self.gridWidget)
        self.labelPlayer9CustomName.setObjectName(u"labelPlayer9CustomName")
        sizePolicy.setHeightForWidth(self.labelPlayer9CustomName.sizePolicy().hasHeightForWidth())
        self.labelPlayer9CustomName.setSizePolicy(sizePolicy)
        self.labelPlayer9CustomName.setMinimumSize(QSize(160, 40))

        self.gridLayout.addWidget(self.labelPlayer9CustomName, 12, 2, 1, 1)

        self.labelPlayer9GameCount = ClickableLabel(self.gridWidget)
        self.labelPlayer9GameCount.setObjectName(u"labelPlayer9GameCount")
        sizePolicy.setHeightForWidth(self.labelPlayer9GameCount.sizePolicy().hasHeightForWidth())
        self.labelPlayer9GameCount.setSizePolicy(sizePolicy)
        self.labelPlayer9GameCount.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelPlayer9GameCount, 12, 3, 1, 1)


        self.verticalLayout.addWidget(self.gridWidget)


        self.horizontalLayout.addWidget(self.verticalWidget)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Raised)
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QFrame.VLine)

        self.horizontalLayout.addWidget(self.line)

        self.gridWidget2 = QWidget(self.centralwidget)
        self.gridWidget2.setObjectName(u"gridWidget2")
        self.gridLayout_2 = QGridLayout(self.gridWidget2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_9 = QLabel(self.gridWidget2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)

        self.labelDetailsSteamId = QLabel(self.gridWidget2)
        self.labelDetailsSteamId.setObjectName(u"labelDetailsSteamId")

        self.gridLayout_2.addWidget(self.labelDetailsSteamId, 1, 1, 1, 1)

        self.label_8 = QLabel(self.gridWidget2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)

        self.labelDetailsName = QLabel(self.gridWidget2)
        self.labelDetailsName.setObjectName(u"labelDetailsName")

        self.gridLayout_2.addWidget(self.labelDetailsName, 2, 1, 1, 1)

        self.inputDetailsCustomName = QLineEdit(self.gridWidget2)
        self.inputDetailsCustomName.setObjectName(u"inputDetailsCustomName")

        self.gridLayout_2.addWidget(self.inputDetailsCustomName, 4, 1, 1, 1)

        self.labelDetailsProName = QLabel(self.gridWidget2)
        self.labelDetailsProName.setObjectName(u"labelDetailsProName")

        self.gridLayout_2.addWidget(self.labelDetailsProName, 3, 1, 1, 1)

        self.label_13 = QLabel(self.gridWidget2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_13, 4, 0, 1, 1)

        self.label_11 = QLabel(self.gridWidget2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_11, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 6, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 0, 0, 1, 2)

        self.horizontalWidget1 = QWidget(self.gridWidget2)
        self.horizontalWidget1.setObjectName(u"horizontalWidget1")
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalWidget1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.buttonDetailsSave = QPushButton(self.horizontalWidget1)
        self.buttonDetailsSave.setObjectName(u"buttonDetailsSave")
        self.buttonDetailsSave.setMaximumSize(QSize(50, 16777215))
        self.buttonDetailsSave.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.buttonDetailsSave)


        self.gridLayout_2.addWidget(self.horizontalWidget1, 5, 0, 1, 2)


        self.horizontalLayout.addWidget(self.gridWidget2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 21))
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
        self.labelPlayer4GameCount.setText("")
        self.labelPlayer4Name.setText("")
        self.labelPlayer2GameCount.setText("")
        self.labelPlayer3ProName.setText("")
        self.labelPlayer4ProName.setText("")
        self.labelPlayer4CustomName.setText("")
        self.labelPlayer3CustomName.setText("")
        self.labelPlayer1ProName.setText("")
        self.labelPlayer1CustomName.setText("")
        self.labelPlayer1GameCount.setText("")
        self.labelPlayer2Name.setText("")
        self.labelPlayer3Name.setText("")
        self.labelPlayer2ProName.setText("")
        self.labelPlayer2CustomName.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Custom Name", None))
        self.labelPlayer0Name.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.labelPlayer0ProName.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Game Count", None))
        self.labelPlayer0CustomName.setText("")
        self.labelPlayer0GameCount.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Pro Name", None))
        self.labelPlayer3GameCount.setText("")
        self.labelPlayer1Name.setText("")
        self.labelPlayer5ProName.setText("")
        self.labelPlayer5Name.setText("")
        self.labelPlayer6ProName.setText("")
        self.labelPlayer6Name.setText("")
        self.labelPlayer7ProName.setText("")
        self.labelPlayer6CustomName.setText("")
        self.labelPlayer5GameCount.setText("")
        self.labelPlayer5CustomName.setText("")
        self.labelPlayer6GameCount.setText("")
        self.labelPlayer7Name.setText("")
        self.labelPlayer8ProName.setText("")
        self.labelPlayer8CustomName.setText("")
        self.labelPlayer8Name.setText("")
        self.labelPlayer7CustomName.setText("")
        self.labelPlayer7GameCount.setText("")
        self.labelPlayer8GameCount.setText("")
        self.labelPlayer9Name.setText("")
        self.labelPlayer9ProName.setText("")
        self.labelPlayer9CustomName.setText("")
        self.labelPlayer9GameCount.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Steam ID</span></p></body></html>", None))
        self.labelDetailsSteamId.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">In Game Name</span></p></body></html>", None))
        self.labelDetailsName.setText("")
        self.labelDetailsProName.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Custom Name</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Pro Name</span></p></body></html>", None))
        self.buttonDetailsSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

