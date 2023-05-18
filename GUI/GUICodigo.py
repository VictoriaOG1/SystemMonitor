# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2extn.RoundProgressBar import roundProgressBar
from pyqtgraph import PlotWidget

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(778, 516)
        MainWindow.setStyleSheet(u"*{\n"
"	border:none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	background-color: rgb(34, 34, 34);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuContainer = QFrame(self.header)
        self.menuContainer.setObjectName(u"menuContainer")
        self.menuContainer.setMinimumSize(QSize(100, 0))
        font = QFont()
        font.setFamily(u"Gill Sans MT")
        font.setPointSize(15)
        self.menuContainer.setFont(font)
        self.menuContainer.setStyleSheet(u"background-color: rgb(51, 51, 51);")
        self.menuContainer.setFrameShape(QFrame.StyledPanel)
        self.menuContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.menuContainer)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.menuLabel = QLabel(self.menuContainer)
        self.menuLabel.setObjectName(u"menuLabel")
        self.menuLabel.setFont(font)
        self.menuLabel.setStyleSheet(u"background-color: rgb(51, 51, 51);")

        self.verticalLayout_15.addWidget(self.menuLabel, 0, Qt.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.menuContainer, 0, Qt.AlignHCenter)

        self.statsContainer = QFrame(self.header)
        self.statsContainer.setObjectName(u"statsContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statsContainer.sizePolicy().hasHeightForWidth())
        self.statsContainer.setSizePolicy(sizePolicy)
        self.statsContainer.setMinimumSize(QSize(550, 1))
        self.statsContainer.setFont(font)
        self.statsContainer.setFrameShape(QFrame.StyledPanel)
        self.statsContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.statsContainer)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.statsLabel = QLabel(self.statsContainer)
        self.statsLabel.setObjectName(u"statsLabel")
        self.statsLabel.setFont(font)

        self.verticalLayout_16.addWidget(self.statsLabel, 0, Qt.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.statsContainer, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.header)

        self.body = QFrame(self.centralwidget)
        self.body.setObjectName(u"body")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(8)
        self.body.setFont(font1)
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.body)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu_options_container = QFrame(self.body)
        self.menu_options_container.setObjectName(u"menu_options_container")
        sizePolicy.setHeightForWidth(self.menu_options_container.sizePolicy().hasHeightForWidth())
        self.menu_options_container.setSizePolicy(sizePolicy)
        self.menu_options_container.setMinimumSize(QSize(0, 0))
        self.menu_options_container.setFrameShape(QFrame.StyledPanel)
        self.menu_options_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.menu_options_container)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.menu_options = QFrame(self.menu_options_container)
        self.menu_options.setObjectName(u"menu_options")
        self.menu_options.setMinimumSize(QSize(200, 0))
        self.menu_options.setMaximumSize(QSize(16777215, 16777215))
        self.menu_options.setStyleSheet(u"*{color: rgb(255, 255, 255);\n"
"background-color: rgb(51, 51, 51);}")
        self.menu_options.setFrameShape(QFrame.StyledPanel)
        self.menu_options.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.menu_options)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 5, 0)
        self.cpuButton = QPushButton(self.menu_options)
        self.cpuButton.setObjectName(u"cpuButton")
        font2 = QFont()
        font2.setFamily(u"Gill Sans MT")
        font2.setPointSize(12)
        self.cpuButton.setFont(font2)
        icon = QIcon()
        icon.addFile(u":/icons/icons/cpu-tower (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.cpuButton.setIcon(icon)
        self.cpuButton.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.cpuButton, 0, Qt.AlignHCenter)

        self.ramButton = QPushButton(self.menu_options)
        self.ramButton.setObjectName(u"ramButton")
        self.ramButton.setFont(font2)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/ram.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ramButton.setIcon(icon1)
        self.ramButton.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.ramButton, 0, Qt.AlignHCenter)

        self.diskButton = QPushButton(self.menu_options)
        self.diskButton.setObjectName(u"diskButton")
        self.diskButton.setFont(font2)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/drive.png", QSize(), QIcon.Normal, QIcon.Off)
        self.diskButton.setIcon(icon2)
        self.diskButton.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.diskButton, 0, Qt.AlignHCenter)

        self.proButton = QPushButton(self.menu_options)
        self.proButton.setObjectName(u"proButton")
        self.proButton.setFont(font2)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/engineering.png", QSize(), QIcon.Normal, QIcon.Off)
        self.proButton.setIcon(icon3)
        self.proButton.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.proButton, 0, Qt.AlignHCenter)

        self.netButton = QPushButton(self.menu_options)
        self.netButton.setObjectName(u"netButton")
        self.netButton.setFont(font2)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/wifi-signal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.netButton.setIcon(icon4)
        self.netButton.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.netButton, 0, Qt.AlignHCenter)

        self.pushButton = QPushButton(self.menu_options)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font2)
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/history.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon5)
        self.pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.pushButton, 0, Qt.AlignHCenter)


        self.horizontalLayout_6.addWidget(self.menu_options, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.menu_options_container, 0, Qt.AlignLeft)

        self.body_content = QFrame(self.body)
        self.body_content.setObjectName(u"body_content")
        sizePolicy.setHeightForWidth(self.body_content.sizePolicy().hasHeightForWidth())
        self.body_content.setSizePolicy(sizePolicy)
        self.body_content.setMinimumSize(QSize(0, 0))
        self.body_content.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.body_content.setFrameShape(QFrame.StyledPanel)
        self.body_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.body_content)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget = QStackedWidget(self.body_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.cpu = QWidget()
        self.cpu.setObjectName(u"cpu")
        self.horizontalLayout_7 = QHBoxLayout(self.cpu)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.cpuContainer = QFrame(self.cpu)
        self.cpuContainer.setObjectName(u"cpuContainer")
        self.cpuContainer.setFrameShape(QFrame.StyledPanel)
        self.cpuContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.cpuContainer)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.cpuHeader = QFrame(self.cpuContainer)
        self.cpuHeader.setObjectName(u"cpuHeader")
        self.cpuHeader.setMinimumSize(QSize(0, 150))
        self.cpuHeader.setFrameShape(QFrame.StyledPanel)
        self.cpuHeader.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.cpuHeader)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 10)
        self.cpuInfo = QFrame(self.cpuHeader)
        self.cpuInfo.setObjectName(u"cpuInfo")
        self.cpuInfo.setFrameShape(QFrame.StyledPanel)
        self.cpuInfo.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.cpuInfo)
        self.gridLayout.setObjectName(u"gridLayout")
        self.cpuCoresValue = QLabel(self.cpuInfo)
        self.cpuCoresValue.setObjectName(u"cpuCoresValue")

        self.gridLayout.addWidget(self.cpuCoresValue, 1, 1, 1, 1, Qt.AlignHCenter)

        self.cpuCoresLabel = QLabel(self.cpuInfo)
        self.cpuCoresLabel.setObjectName(u"cpuCoresLabel")

        self.gridLayout.addWidget(self.cpuCoresLabel, 1, 0, 1, 1)

        self.cpuCountValue = QLabel(self.cpuInfo)
        self.cpuCountValue.setObjectName(u"cpuCountValue")

        self.gridLayout.addWidget(self.cpuCountValue, 0, 1, 1, 1, Qt.AlignHCenter)

        self.cpuCountLabel = QLabel(self.cpuInfo)
        self.cpuCountLabel.setObjectName(u"cpuCountLabel")

        self.gridLayout.addWidget(self.cpuCountLabel, 0, 0, 1, 1)


        self.horizontalLayout_8.addWidget(self.cpuInfo)

        self.cpuPerGraph = roundProgressBar(self.cpuHeader)
        self.cpuPerGraph.setObjectName(u"cpuPerGraph")
        self.cpuPerGraph.setMinimumSize(QSize(150, 100))

        self.horizontalLayout_8.addWidget(self.cpuPerGraph)


        self.verticalLayout_6.addWidget(self.cpuHeader)

        self.cpuGraph = PlotWidget(self.cpuContainer)
        self.cpuGraph.setObjectName(u"cpuGraph")
        sizePolicy1.setHeightForWidth(self.cpuGraph.sizePolicy().hasHeightForWidth())
        self.cpuGraph.setSizePolicy(sizePolicy1)

        self.verticalLayout_6.addWidget(self.cpuGraph)

        self.cpuFoot = QFrame(self.cpuContainer)
        self.cpuFoot.setObjectName(u"cpuFoot")
        self.cpuFoot.setFrameShape(QFrame.StyledPanel)
        self.cpuFoot.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.cpuFoot)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.cpuSave = QPushButton(self.cpuFoot)
        self.cpuSave.setObjectName(u"cpuSave")
        self.cpuSave.setMinimumSize(QSize(100, 15))
        font3 = QFont()
        font3.setFamily(u"Gill Sans MT")
        font3.setPointSize(9)
        self.cpuSave.setFont(font3)
        self.cpuSave.setStyleSheet(u"background-color: rgb(51, 51, 51);")

        self.verticalLayout_11.addWidget(self.cpuSave, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_6.addWidget(self.cpuFoot, 0, Qt.AlignBottom)


        self.horizontalLayout_7.addWidget(self.cpuContainer)

        self.stackedWidget.addWidget(self.cpu)
        self.ram = QWidget()
        self.ram.setObjectName(u"ram")
        self.verticalLayout_7 = QVBoxLayout(self.ram)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.ramContainer = QFrame(self.ram)
        self.ramContainer.setObjectName(u"ramContainer")
        self.ramContainer.setFrameShape(QFrame.StyledPanel)
        self.ramContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.ramContainer)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.ramHeader = QFrame(self.ramContainer)
        self.ramHeader.setObjectName(u"ramHeader")
        self.ramHeader.setFrameShape(QFrame.StyledPanel)
        self.ramHeader.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.ramHeader)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 10)
        self.ramInfo = QFrame(self.ramHeader)
        self.ramInfo.setObjectName(u"ramInfo")
        self.ramInfo.setFrameShape(QFrame.StyledPanel)
        self.ramInfo.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.ramInfo)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.ramUsedValue = QLabel(self.ramInfo)
        self.ramUsedValue.setObjectName(u"ramUsedValue")

        self.gridLayout_2.addWidget(self.ramUsedValue, 2, 1, 1, 1, Qt.AlignHCenter)

        self.ramFreeLabel = QLabel(self.ramInfo)
        self.ramFreeLabel.setObjectName(u"ramFreeLabel")

        self.gridLayout_2.addWidget(self.ramFreeLabel, 3, 0, 1, 1)

        self.ramFreeValue = QLabel(self.ramInfo)
        self.ramFreeValue.setObjectName(u"ramFreeValue")

        self.gridLayout_2.addWidget(self.ramFreeValue, 3, 1, 1, 1, Qt.AlignHCenter)

        self.ramTotalLabel = QLabel(self.ramInfo)
        self.ramTotalLabel.setObjectName(u"ramTotalLabel")

        self.gridLayout_2.addWidget(self.ramTotalLabel, 0, 0, 1, 1)

        self.ramTotalValue = QLabel(self.ramInfo)
        self.ramTotalValue.setObjectName(u"ramTotalValue")

        self.gridLayout_2.addWidget(self.ramTotalValue, 0, 1, 1, 1, Qt.AlignHCenter)

        self.ramAvailValue = QLabel(self.ramInfo)
        self.ramAvailValue.setObjectName(u"ramAvailValue")

        self.gridLayout_2.addWidget(self.ramAvailValue, 1, 1, 1, 1, Qt.AlignHCenter)

        self.ramUsedLabel = QLabel(self.ramInfo)
        self.ramUsedLabel.setObjectName(u"ramUsedLabel")

        self.gridLayout_2.addWidget(self.ramUsedLabel, 2, 0, 1, 1)

        self.ramAvailLabel = QLabel(self.ramInfo)
        self.ramAvailLabel.setObjectName(u"ramAvailLabel")

        self.gridLayout_2.addWidget(self.ramAvailLabel, 1, 0, 1, 1)


        self.horizontalLayout_9.addWidget(self.ramInfo)

        self.ramPerGraph = roundProgressBar(self.ramHeader)
        self.ramPerGraph.setObjectName(u"ramPerGraph")

        self.horizontalLayout_9.addWidget(self.ramPerGraph)


        self.verticalLayout_12.addWidget(self.ramHeader)

        self.ramGraph = PlotWidget(self.ramContainer)
        self.ramGraph.setObjectName(u"ramGraph")
        sizePolicy1.setHeightForWidth(self.ramGraph.sizePolicy().hasHeightForWidth())
        self.ramGraph.setSizePolicy(sizePolicy1)

        self.verticalLayout_12.addWidget(self.ramGraph)

        self.ramFoot = QFrame(self.ramContainer)
        self.ramFoot.setObjectName(u"ramFoot")
        self.ramFoot.setFrameShape(QFrame.StyledPanel)
        self.ramFoot.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.ramFoot)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.ramSave = QPushButton(self.ramFoot)
        self.ramSave.setObjectName(u"ramSave")
        self.ramSave.setMinimumSize(QSize(100, 15))
        self.ramSave.setSizeIncrement(QSize(0, 0))
        self.ramSave.setFont(font3)
        self.ramSave.setStyleSheet(u"background-color: rgb(51, 51, 51);")

        self.verticalLayout_13.addWidget(self.ramSave, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_12.addWidget(self.ramFoot, 0, Qt.AlignBottom)


        self.verticalLayout_7.addWidget(self.ramContainer)

        self.stackedWidget.addWidget(self.ram)
        self.disk = QWidget()
        self.disk.setObjectName(u"disk")
        self.verticalLayout_8 = QVBoxLayout(self.disk)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.diskContainer = QFrame(self.disk)
        self.diskContainer.setObjectName(u"diskContainer")
        self.diskContainer.setFrameShape(QFrame.StyledPanel)
        self.diskContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.diskContainer)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.diskHeader = QFrame(self.diskContainer)
        self.diskHeader.setObjectName(u"diskHeader")
        self.diskHeader.setMinimumSize(QSize(0, 150))
        self.diskHeader.setFrameShape(QFrame.StyledPanel)
        self.diskHeader.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.diskHeader)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 10)
        self.diskInfo = QFrame(self.diskHeader)
        self.diskInfo.setObjectName(u"diskInfo")
        self.diskInfo.setFrameShape(QFrame.StyledPanel)
        self.diskInfo.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.diskInfo)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.diskTotalLabel = QLabel(self.diskInfo)
        self.diskTotalLabel.setObjectName(u"diskTotalLabel")

        self.gridLayout_3.addWidget(self.diskTotalLabel, 0, 0, 1, 1)

        self.diskTotalValue = QLabel(self.diskInfo)
        self.diskTotalValue.setObjectName(u"diskTotalValue")

        self.gridLayout_3.addWidget(self.diskTotalValue, 0, 1, 1, 1, Qt.AlignHCenter)

        self.diskUsedLabel = QLabel(self.diskInfo)
        self.diskUsedLabel.setObjectName(u"diskUsedLabel")

        self.gridLayout_3.addWidget(self.diskUsedLabel, 1, 0, 1, 1)

        self.diskUsedValue = QLabel(self.diskInfo)
        self.diskUsedValue.setObjectName(u"diskUsedValue")

        self.gridLayout_3.addWidget(self.diskUsedValue, 1, 1, 1, 1, Qt.AlignHCenter)

        self.diskFreeLabel = QLabel(self.diskInfo)
        self.diskFreeLabel.setObjectName(u"diskFreeLabel")

        self.gridLayout_3.addWidget(self.diskFreeLabel, 2, 0, 1, 1)

        self.diskFreeValue = QLabel(self.diskInfo)
        self.diskFreeValue.setObjectName(u"diskFreeValue")

        self.gridLayout_3.addWidget(self.diskFreeValue, 2, 1, 1, 1, Qt.AlignHCenter)


        self.horizontalLayout_10.addWidget(self.diskInfo)

        self.diskPerGraph = roundProgressBar(self.diskHeader)
        self.diskPerGraph.setObjectName(u"diskPerGraph")

        self.horizontalLayout_10.addWidget(self.diskPerGraph)


        self.verticalLayout_14.addWidget(self.diskHeader)

        self.diskGraph = PlotWidget(self.diskContainer)
        self.diskGraph.setObjectName(u"diskGraph")

        self.verticalLayout_14.addWidget(self.diskGraph)


        self.verticalLayout_8.addWidget(self.diskContainer)

        self.stackedWidget.addWidget(self.disk)
        self.pro = QWidget()
        self.pro.setObjectName(u"pro")
        self.verticalLayout_5 = QVBoxLayout(self.pro)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.proInfo = QFrame(self.pro)
        self.proInfo.setObjectName(u"proInfo")
        self.proInfo.setFrameShape(QFrame.StyledPanel)
        self.proInfo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.proInfo)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pro_table = QTableWidget(self.proInfo)
        if (self.pro_table.columnCount() < 5):
            self.pro_table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.pro_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.pro_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.pro_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.pro_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.pro_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.pro_table.setObjectName(u"pro_table")
        font4 = QFont()
        font4.setFamily(u"Gill Sans MT")
        font4.setPointSize(8)
        font4.setBold(False)
        font4.setWeight(50)
        self.pro_table.setFont(font4)
        self.pro_table.setStyleSheet(u"QHeaderView::section {\n"
"	font: 8pt \"Gill Sans MT\";\n"
"    background-color:  rgb(51, 51, 51);\n"
"    color: white;\n"
"}\n"
"*{\n"
"	background-color: rgb(53, 53, 53);\n"
"}")

        self.verticalLayout_4.addWidget(self.pro_table)


        self.verticalLayout_5.addWidget(self.proInfo)

        self.stackedWidget.addWidget(self.pro)
        self.net = QWidget()
        self.net.setObjectName(u"net")
        self.verticalLayout_9 = QVBoxLayout(self.net)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.netInfo = QFrame(self.net)
        self.netInfo.setObjectName(u"netInfo")
        self.netInfo.setFrameShape(QFrame.StyledPanel)
        self.netInfo.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.netInfo)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.netDownLabel = QLabel(self.netInfo)
        self.netDownLabel.setObjectName(u"netDownLabel")

        self.gridLayout_4.addWidget(self.netDownLabel, 0, 0, 1, 1, Qt.AlignHCenter)

        self.netUpLabel = QLabel(self.netInfo)
        self.netUpLabel.setObjectName(u"netUpLabel")

        self.gridLayout_4.addWidget(self.netUpLabel, 1, 0, 1, 1, Qt.AlignHCenter)

        self.netUpValue = QLabel(self.netInfo)
        self.netUpValue.setObjectName(u"netUpValue")

        self.gridLayout_4.addWidget(self.netUpValue, 1, 1, 1, 1, Qt.AlignHCenter)

        self.netDownValue = QLabel(self.netInfo)
        self.netDownValue.setObjectName(u"netDownValue")

        self.gridLayout_4.addWidget(self.netDownValue, 0, 1, 1, 1, Qt.AlignHCenter)


        self.verticalLayout_9.addWidget(self.netInfo)

        self.netGraph = PlotWidget(self.net)
        self.netGraph.setObjectName(u"netGraph")
        sizePolicy1.setHeightForWidth(self.netGraph.sizePolicy().hasHeightForWidth())
        self.netGraph.setSizePolicy(sizePolicy1)

        self.verticalLayout_9.addWidget(self.netGraph)

        self.stackedWidget.addWidget(self.net)
        self.history = QWidget()
        self.history.setObjectName(u"history")
        self.verticalLayout_10 = QVBoxLayout(self.history)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.cpuHisGraph = QFrame(self.history)
        self.cpuHisGraph.setObjectName(u"cpuHisGraph")
        self.verticalLayout_18 = QVBoxLayout(self.cpuHisGraph)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.imageCPUGraph = QLabel(self.cpuHisGraph)
        self.imageCPUGraph.setObjectName(u"imageCPUGraph")

        self.verticalLayout_18.addWidget(self.imageCPUGraph)


        self.verticalLayout_10.addWidget(self.cpuHisGraph)

        self.ramHisGraph = QFrame(self.history)
        self.ramHisGraph.setObjectName(u"ramHisGraph")
        self.verticalLayout_17 = QVBoxLayout(self.ramHisGraph)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.imageRAMGraph = QLabel(self.ramHisGraph)
        self.imageRAMGraph.setObjectName(u"imageRAMGraph")

        self.verticalLayout_17.addWidget(self.imageRAMGraph)


        self.verticalLayout_10.addWidget(self.ramHisGraph)

        self.stackedWidget.addWidget(self.history)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.body_content)


        self.verticalLayout.addWidget(self.body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Menu</span></p></body></html>", None))
        self.statsLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Statistics</span></p></body></html>", None))
        self.cpuButton.setText(QCoreApplication.translate("MainWindow", u" CPU", None))
        self.ramButton.setText(QCoreApplication.translate("MainWindow", u" RAM", None))
        self.diskButton.setText(QCoreApplication.translate("MainWindow", u" Storage", None))
        self.proButton.setText(QCoreApplication.translate("MainWindow", u" Processes", None))
        self.netButton.setText(QCoreApplication.translate("MainWindow", u" Network", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u" History", None))
        self.cpuCoresValue.setText(QCoreApplication.translate("MainWindow", u"NA", None))
        self.cpuCoresLabel.setText(QCoreApplication.translate("MainWindow", u"CPU main cores:", None))
        self.cpuCountValue.setText(QCoreApplication.translate("MainWindow", u"NA", None))
        self.cpuCountLabel.setText(QCoreApplication.translate("MainWindow", u"CPU Count:", None))
        self.cpuSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.ramUsedValue.setText(QCoreApplication.translate("MainWindow", u"NA", None))
        self.ramFreeLabel.setText(QCoreApplication.translate("MainWindow", u"Free RAM:", None))
        self.ramFreeValue.setText(QCoreApplication.translate("MainWindow", u"NA", None))
        self.ramTotalLabel.setText(QCoreApplication.translate("MainWindow", u"Total RAM:", None))
        self.ramTotalValue.setText(QCoreApplication.translate("MainWindow", u"NA", None))
        self.ramAvailValue.setText(QCoreApplication.translate("MainWindow", u"NA", None))
        self.ramUsedLabel.setText(QCoreApplication.translate("MainWindow", u"Used RAM:", None))
        self.ramAvailLabel.setText(QCoreApplication.translate("MainWindow", u"Available RAM:", None))
        self.ramSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.diskTotalLabel.setText(QCoreApplication.translate("MainWindow", u"Total Space:", None))
        self.diskTotalValue.setText(QCoreApplication.translate("MainWindow", u"NA", None))
        self.diskUsedLabel.setText(QCoreApplication.translate("MainWindow", u"Used Space:", None))
        self.diskUsedValue.setText(QCoreApplication.translate("MainWindow", u"NA", None))
        self.diskFreeLabel.setText(QCoreApplication.translate("MainWindow", u"Free Space:", None))
        self.diskFreeValue.setText(QCoreApplication.translate("MainWindow", u"NA", None))
        ___qtablewidgetitem = self.pro_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.pro_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem2 = self.pro_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem3 = self.pro_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"RAM Usage", None));
        ___qtablewidgetitem4 = self.pro_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"CPU Usage", None));
        self.netDownLabel.setText(QCoreApplication.translate("MainWindow", u"Download Speed:", None))
        self.netUpLabel.setText(QCoreApplication.translate("MainWindow", u"Upload Speed:", None))
        self.netUpValue.setText(QCoreApplication.translate("MainWindow", u"0 mpbs", None))
        self.netDownValue.setText(QCoreApplication.translate("MainWindow", u"0 mpbs", None))
        self.imageCPUGraph.setText("")
        self.imageRAMGraph.setText("")
    # retranslateUi

