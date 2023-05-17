import sys
import os
import psutil
import PySide2extn
from PySide2 import *
from GUICodigo import *
from qt_material import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(":/icons/icons/settings1.png"))
        self.setWindowTitle("System Monitor by AOCZ")
        self.setFixedSize(1400,1000)
        
        #CPU
        self.ui.cpuButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.cpu))
        
        #RAM
        self.ui.ramButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.ram))

        #Storage
        self.ui.diskButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.disk))

        #Processes
        self.ui.proButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pro))

        #Network
        self.ui.netButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.net))
        #History
        self.ui.pushButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.history))
        
        self.show()
        self.ram_information()
        self.cpu_information()
        self.processes_information()
        self.network_information()
        self.storage_information()
    
    def cpu_information(self):
        #CPUCores
        count = os.cpu_count()
        self.ui.cpuCountValue.setText(str(count))

        #CPUMainCores
        mainCores = psutil.cpu_count(logical=False)
        self.ui.cpuCoresValue.setText(str(mainCores))

        #CPU Percentage Usage Graph
        cpuPer = psutil.cpu_percent()
        self.ui.cpuPerGraph.rpb_setMaximum(100)
        self.ui.cpuPerGraph.rpb_setValue(cpuPer)
        self.ui.cpuPerGraph.rpb_setLineColor((255,30,99))
        self.ui.cpuPerGraph.rpb_setPieColor((45,74,83))
        self.ui.cpuPerGraph.rpb_setTextColor((255,255,255))
        self.ui.cpuPerGraph.rpb_setInitialPos('North')
        self.ui.cpuPerGraph.rpb_setTextFont('Gill Sans MT')
        self.ui.cpuPerGraph.rpb_setLineWidth(10)
        self.ui.cpuPerGraph.rpb_setPathWidth(15)
        self.ui.cpuPerGraph.rpb_setLineCap('RoundCap')

        #CPU Graph


    def ram_information(self):
        #RAMTotal
        totalRam = 1.0
        totalRam = psutil.virtual_memory()[0]*totalRam
        totalRam = totalRam/(1024*1024*1024)
        self.ui.ramTotalValue.setText(str("{:.2f}".format(totalRam) + ' GB'))
        
        #RAMAvailable
        availRam = 1.0
        availRam = psutil.virtual_memory()[1]*availRam
        availRam = availRam/(1024*1024*1024)
        self.ui.ramAvailValue.setText(str("{:.2f}".format(availRam) + ' GB'))

        #RAMUsed
        usedRam = 1.0
        usedRam = psutil.virtual_memory()[3]*usedRam
        usedRam = usedRam/(1024*1024*1024)
        self.ui.ramUsedValue.setText(str("{:.2f}".format(usedRam) + ' GB'))

        #RAMFree
        freeRam = 1.0
        freeRam = psutil.virtual_memory()[4]*freeRam
        freeRam = freeRam/(1024*1024*1024)
        self.ui.ramFreeValue.setText(str("{:.2f}".format(freeRam) + ' GB'))

        #RAM Percentage Usage Graph
        usageRam = psutil.virtual_memory()[2]
        self.ui.ramPerGraph.rpb_setMaximum(100)
        self.ui.ramPerGraph.rpb_setValue(usageRam)
        self.ui.ramPerGraph.rpb_setLineColor((255,30,99))
        self.ui.ramPerGraph.rpb_setPieColor((45,74,83))
        self.ui.ramPerGraph.rpb_setTextColor((255,255,255))
        self.ui.ramPerGraph.rpb_setInitialPos('North')
        self.ui.ramPerGraph.rpb_setTextFont('Gill Sans MT')
        self.ui.ramPerGraph.rpb_setLineWidth(10)
        self.ui.ramPerGraph.rpb_setPathWidth(15)
        self.ui.ramPerGraph.rpb_setLineCap('RoundCap')

        #RAM Graph
    
    def storage_information(self):
        disk_usage = psutil.disk_usage('/')  
        
        #Disk Total
        total_space = disk_usage.total
        total_space = total_space/(1024*1024*1024)
        self.ui.diskTotalValue.setText(str("{:.2f}".format(total_space) + ' GB'))

        #Disk Used
        used_space = disk_usage.used
        used_space = used_space/(1024*1024*1024)
        self.ui.diskUsedValue.setText(str("{:.2f}".format(used_space) + ' GB'))

        #Disk Free
        free_space = disk_usage.free
        free_space = free_space/(1024*1024*1024)
        self.ui.diskFreeValue.setText(str("{:.2f}".format(free_space) + ' GB'))

        #CPU Percentage Graph
        percentage_used = disk_usage.percent
        self.ui.diskPerGraph.rpb_setMaximum(100)
        self.ui.diskPerGraph.rpb_setValue(percentage_used)
        self.ui.diskPerGraph.rpb_setLineColor((255,30,99))
        self.ui.diskPerGraph.rpb_setPieColor((45,74,83))
        self.ui.diskPerGraph.rpb_setTextColor((255,255,255))
        self.ui.diskPerGraph.rpb_setInitialPos('North')
        self.ui.diskPerGraph.rpb_setTextFont('Gill Sans MT')
        self.ui.diskPerGraph.rpb_setLineWidth(10)
        self.ui.diskPerGraph.rpb_setPathWidth(15)
        self.ui.diskPerGraph.rpb_setLineCap('RoundCap')

    def processes_information(self):
        for x in psutil.pids():
            rowPosition = self.ui.pro_table.rowCount()
            self.ui.pro_table.insertRow(rowPosition)
            try:
                process = psutil.Process(x)
                self.create_table_widget(rowPosition,0,str(process.name()), "pro_table")
                self.create_table_widget(rowPosition,1,str(process.pid), "pro_table")
                self.create_table_widget(rowPosition,2,str(process.status()), "pro_table")
                self.create_table_widget(rowPosition,3,str('{:.2f}'.format(process.memory_percent())) + '%', "pro_table")
                self.create_table_widget(rowPosition,4,str(0), "pro_table")
            except Exception as e:
                print(e)
    
    def create_table_widget(self, rowPosition, columnPositon, text, tableName):
        qtablewidgetitem = QTableWidgetItem() 
        getattr(self.ui,tableName).setItem(rowPosition, columnPositon, qtablewidgetitem)
        qtablewidgetitem = getattr(self.ui, tableName).item(rowPosition, columnPositon)
        qtablewidgetitem.setText(text)

    def network_information(self):
        net_io = psutil.net_io_counters()
        upload_speed = float(net_io.bytes_sent / 1024)
        download_speed = float(net_io.bytes_recv / 1024)
        self.ui.netDownValue.setText(str("{:.2f}".format(download_speed) + ' mbps'))
        self.ui.netUpValue.setText(str("{:.2f}".format(upload_speed) + ' mbps'))
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())