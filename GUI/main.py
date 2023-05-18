import sys
import os
import psutil
import PySide2extn
from PySide2 import *
from GUICodigo import *
from qt_material import *
from PyQt5.QtCore import *
import pyqtgraph as pg
from pyqtgraph.exporters import Exporter, SVGExporter
from PIL import Image
from pyqtgraph.Qt import QtGui
import numpy as np

class CPUMonitorThread(QThread):
    cpu_data_updated = pyqtSignal(list)

    def run(self):
        while True:
            cpu_usage = psutil.cpu_percent() 
            self.cpu_data_updated.emit([cpu_usage])
            self.msleep(1000)

class MemoryMonitorThread(QThread):
    mem_data_updated = pyqtSignal(list)

    def run(self):
        while True:
            mem_percent = psutil.virtual_memory().percent
            self.mem_data_updated.emit([mem_percent])
            self.msleep(1000)

class StorageMonitorThread(QThread):
    storage_data_updated = pyqtSignal(list)

    def run(self):
        while True:
            disk_usage = psutil.disk_usage('/')
            disk_io = psutil.disk_io_counters()
            self.storage_data_updated.emit([disk_usage.percent, disk_io.write_bytes/10000000, disk_io.read_bytes /10000000])
            self.msleep(1000)

class ProcessMonitorThread(QThread):
    process_data_updated = pyqtSignal(list)

    def run(self):
        while True:
            process_list = []
            for process in psutil.process_iter():
                try:
                    name = str(process.name())
                    pid = str(process.pid)
                    status = str(process.status())
                    memory_usage = str('{:.2f}'.format(process.memory_percent())) + '%'
                    cpu_usage = str('{:.2f}'.format(process.cpu_percent())) + '%'  
                    process_list.append([name, pid, status, memory_usage, cpu_usage])
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
            self.process_data_updated.emit(process_list)
            self.msleep(1000)

class NetworkMonitorThread(QThread):
    update_stats = pyqtSignal(list)  # Signal for updating stats

    def run(self):
        while True:
            net_io = psutil.net_io_counters()
            upload_speed = float(net_io.bytes_sent / 1024)
            download_speed = float(net_io.bytes_recv / 1024)
            self.update_stats.emit([upload_speed, download_speed])
            self.msleep(1000)  # Delay in milliseconds

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #Set icon, title and a fixed size to main window
        self.setWindowIcon(QIcon(":/icons/icons/settings1.png"))
        self.setWindowTitle("System Monitor by AOCZ")
        self.setFixedSize(900,600)

        #CPU button connect to CPU page 
        self.ui.cpuButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.cpu))
        
        #RAM button connect to RAM page
        self.ui.ramButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.ram))

        #Storage button connect to Storage page
        self.ui.diskButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.disk))

        #Processes button connect to Processes page
        self.ui.proButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pro))

        #Network button connect to Network page
        self.ui.netButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.net))
        
        #History button connect to History page 
        self.ui.pushButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.history))

        # Load information to each page
        self.ram_information()
        self.cpu_information()
        self.processes_information()
        self.network_information()
        self.storage_information()

        #Threads
        self.cpu_monitor_thread = CPUMonitorThread()
        self.cpu_monitor_thread.cpu_data_updated.connect(self.update_CPU_data)
        self.cpu_monitor_thread.start()

        self.mem_monitor_thread = MemoryMonitorThread()
        self.mem_monitor_thread.mem_data_updated.connect(self.update_RAM_data)
        self.mem_monitor_thread.start()

        self.storage_monitor_thread = StorageMonitorThread()
        self.storage_monitor_thread.storage_data_updated.connect(self.update_Disk_data)
        self.storage_monitor_thread.start()

        self.network_monitor_thread = NetworkMonitorThread()
        self.network_monitor_thread.update_stats.connect(self.update_Net_data)
        self.network_monitor_thread.start()

        # Update widgets every second
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_widgets)
        self.timer.start()

        #Show main window
        self.show()
    
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
        self.ui.cpuPerGraph.rpb_setLineColor((255, 193, 7))
        self.ui.cpuPerGraph.rpb_setPieColor((255, 193, 7))
        self.ui.cpuPerGraph.rpb_setTextColor((255,255,255))
        self.ui.cpuPerGraph.rpb_setInitialPos('North')
        self.ui.cpuPerGraph.rpb_setTextFont('Gill Sans MT')
        self.ui.cpuPerGraph.rpb_setLineWidth(10)
        self.ui.cpuPerGraph.rpb_setPathWidth(15)
        self.ui.cpuPerGraph.rpb_setLineCap('RoundCap')

        #CPU Graph
        self.ui.cpuGraph.setBackground(background=(50,50,50))
        self.ui.cpuGraph.setTitle('CPU Usage')
        self.ui.cpuGraph.setYRange(0,100)
        self.ui.cpuGraph.showGrid(False, False)
        self.cpu_curve = self.ui.cpuGraph.plot(pen=pg.mkPen(color='#FFC107', width=3))
        
        # Customize the axis labels
        label_style = {'color': '#ffffff', 'size': '20pt'}
        self.ui.cpuGraph.setLabel('left', '%', **label_style)
        self.ui.cpuGraph.setLabel('bottom', 'Time', **label_style)
        self.cpu_data = [0]

        # Save CPU data button 
        self.ui.cpuSave.clicked.connect(self.CPU_SAVE_clicked)

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
        self.ui.ramPerGraph.rpb_setLineColor((255, 105, 97))
        self.ui.ramPerGraph.rpb_setPieColor((255, 105, 97))
        self.ui.ramPerGraph.rpb_setTextColor((255,255,255))
        self.ui.ramPerGraph.rpb_setInitialPos('North')
        self.ui.ramPerGraph.rpb_setTextFont('Gill Sans MT')
        self.ui.ramPerGraph.rpb_setLineWidth(10)
        self.ui.ramPerGraph.rpb_setPathWidth(15)
        self.ui.ramPerGraph.rpb_setLineCap('RoundCap')

        #RAM Graph
        self.ui.ramGraph.setBackground(background=(50,50,50))
        self.ui.ramGraph.setTitle('RAM Usage')
        self.ui.ramGraph.setYRange(0,100)
        self.ui.ramGraph.showGrid(False, False)
        self.ram_curve = self.ui.ramGraph.plot(pen=pg.mkPen(color='#FF6961', width=3))
        
        # Customize the axis labels
        label_style = {'color': '#ffffff', 'size': '20pt'}
        self.ui.ramGraph.setLabel('left', '%', **label_style)
        self.ui.ramGraph.setLabel('bottom', 'Time', **label_style)
        
        self.ram_data = [0]

        # Save CPU data button 
        self.ui.ramSave.clicked.connect(self.RAM_SAVE_clicked)
    
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

        #Disk Percentage Graph
        percentage_used = disk_usage.percent
        self.ui.diskPerGraph.rpb_setMaximum(100)
        self.ui.diskPerGraph.rpb_setValue(percentage_used)
        self.ui.diskPerGraph.rpb_setLineColor((33, 150, 243))
        self.ui.diskPerGraph.rpb_setPieColor((33, 150, 243))
        self.ui.diskPerGraph.rpb_setTextColor((255,255,255))
        self.ui.diskPerGraph.rpb_setInitialPos('North')
        self.ui.diskPerGraph.rpb_setTextFont('Gill Sans MT')
        self.ui.diskPerGraph.rpb_setLineWidth(10)
        self.ui.diskPerGraph.rpb_setPathWidth(15)
        self.ui.diskPerGraph.rpb_setLineCap('RoundCap')

        #Disk Graph
        self.ui.diskGraph.setBackground(background=(50,50,50))
        self.ui.diskGraph.setTitle('Storage Usage')
        self.ui.diskGraph.showGrid(False, False)
        self.disk_write_curve = self.ui.diskGraph.plot(pen=pg.mkPen(color='#2196F3', width=3))
        self.disk_read_curve = self.ui.diskGraph.plot(pen=pg.mkPen(color='#219693', width=3))
        
        # Add legend
        legend = pg.LegendItem(offset=(70, 30))
        legend.setParentItem(self.ui.diskGraph.graphicsItem())
        legend.addItem(self.disk_write_curve, 'Write')
        legend.addItem(self.disk_read_curve, 'Read')

        # Customize the axis labels
        label_style = {'color': '#ffffff', 'size': '20pt'}
        self.ui.diskGraph.setLabel('left', 'MB', **label_style)
        self.ui.diskGraph.setLabel('bottom', 'Time', **label_style)
        
        self.disk_write_data = [0]
        self.disk_read_data = [0]


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
                self.create_table_widget(rowPosition,4,str('{:.2f}'.format(process.cpu_percent())) + '%', "pro_table")
            except Exception as e:
                print(e)
    
    def create_table_widget(self, rowPosition, columnPositon, text, tableName):
        qtablewidgetitem = QTableWidgetItem() 
        getattr(self.ui,tableName).setItem(rowPosition, columnPositon, qtablewidgetitem)
        qtablewidgetitem = getattr(self.ui, tableName).item(rowPosition, columnPositon)
        qtablewidgetitem.setText(text)

    def network_information(self):

        #Network info
        net_io = psutil.net_io_counters()
        upload_speed = float(net_io.bytes_sent / (1024*1024*1024))
        download_speed = float(net_io.bytes_recv / (1024*1024*1024))
        self.ui.netDownValue.setText(str("{:.2f}".format(download_speed) + ' mbps'))
        self.ui.netUpValue.setText(str("{:.2f}".format(upload_speed) + ' mbps'))
        
        #Network graph
        self.ui.netGraph.setBackground(background=(50,50,50))
        self.ui.netGraph.setTitle('Network Usage')
        self.ui.netGraph.showGrid(False, False)
        self.net_upload_curve = self.ui.netGraph.plot(pen=pg.mkPen(color='#4CAF51', width=5))
        self.net_download_curve = self.ui.netGraph.plot(pen=pg.mkPen(color='#4CAF91', width=5))
        
        # Add legend
        legend = pg.LegendItem(offset=(70, 30))
        legend.setParentItem(self.ui.netGraph.graphicsItem())
        legend.addItem(self.net_upload_curve, 'Upload')
        legend.addItem(self.net_download_curve, 'Download')

        # Customize the axis labels
        label_style = {'color': '#ffffff', 'size': '20pt'}
        self.ui.netGraph.setLabel('left', 'Mb', **label_style)
        self.ui.netGraph.setLabel('bottom', 'Time', **label_style)

        self.net_upload_data = [0]
        self.net_download_data = [0]

    #Update graphs information 
    def update_CPU_data(self, data):
        self.cpu_data.append(data[0])
        self.cpu_curve.setData(self.cpu_data)
        self.ui.cpuPerGraph.rpb_setValue(data[0])
    
    def update_RAM_data(self, data):
        self.ram_data.append(data[0])
        self.ram_curve.setData(self.ram_data)
        self.ui.ramPerGraph.rpb_setValue(data[0])

    def update_Disk_data(self, data):
        if (data[0]<59000 and data[1]<59000):
            self.disk_write_data.append(data[0])
            self.disk_read_data.append(data[1])
            self.disk_write_curve.setData(self.disk_write_data)
            self.disk_read_curve.setData(self.disk_read_data)

    def update_Net_data(self, data):
        if (data[0]<59000 and data[1]<59000):
            self.net_upload_data.append(data[0])
            self.net_download_data.append(data[1])
            self.net_upload_curve.setData(self.net_upload_data)
            self.net_download_curve.setData(self.net_download_data)
            self.ui.netUpValue.setText(str("{:.2f}".format(data[0]) + ' Mbps'))
            self.ui.netDownValue.setText(str("{:.2f}".format(data[1]) + ' Mbps'))
    

    def update_widgets(self):
        # Update CPU usage
        cpu_percent = psutil.cpu_percent()
        self.update_CPU_data([cpu_percent])

        # Update memory usage
        mem_percent = psutil.virtual_memory().percent
        self.update_RAM_data([mem_percent])

        # Update disk I/O counters
        disk_io_counters = psutil.disk_io_counters()
        write_bytes = disk_io_counters.write_bytes/(1024*1024)
        read_bytes = disk_io_counters.read_bytes/(1024*1024)
        self.update_Disk_data([write_bytes, read_bytes])

        #Update network data
        net_io1 = psutil.net_io_counters()
        upload_speed1 = (float(net_io1.bytes_sent)*8)/1000000
        download_speed1 = (float(net_io1.bytes_recv)*8)/1000000
        self.update_Net_data([upload_speed1, download_speed1])

        
    
    def CPU_SAVE_clicked(self):
        filename = 'plotCPU.png'
        exporter = pg.exporters.ImageExporter(self.ui.cpuGraph.plotItem)
        exporter.export(filename)
        
        # Load the image using QImage
        qimage = QImage(filename)

       # Convert QImage to numpy array
        width = qimage.width()
        height = qimage.height()
        arr = np.zeros((height, width, 4), dtype=np.uint8)
        for y in range(height):
            for x in range(width):
                color = QColor(qimage.pixel(x, y))
                arr[y, x, 0] = color.red()
                arr[y, x, 1] = color.green()
                arr[y, x, 2] = color.blue()
                arr[y, x, 3] = color.alpha()

        # Rotate the image by 90 degrees counterclockwise
        arr = np.rot90(arr, 3)

        # Create an ImageItem
        image_item = pg.ImageItem()
        image_item.setImage(arr)

        # Clear the plot before adding the new image
        self.ui.cpuHisGraph.clear()

        # Add the ImageItem to the plot
        self.ui.cpuHisGraph.addItem(image_item)
        
    
    def RAM_SAVE_clicked(self):
        filename = 'plotRAM.svg'
        exporter = SVGExporter(self.ui.ramGraph.plotItem)
        exporter.export(filename)

        # Load the image using QImage
        qimage = QImage(filename)

       # Convert QImage to numpy array
        width = qimage.width()
        height = qimage.height()
        arr = np.zeros((height, width, 4), dtype=np.uint8)
        for y in range(height):
            for x in range(width):
                color = QColor(qimage.pixel(x, y))
                arr[y, x, 0] = color.red()
                arr[y, x, 1] = color.green()
                arr[y, x, 2] = color.blue()
                arr[y, x, 3] = color.alpha()

        # Rotate the image by 90 degrees counterclockwise
        arr = np.rot90(arr, 3)

        # Create an ImageItem
        image_item = pg.ImageItem()
        image_item.setImage(arr)

        # Clear the plot before adding the new image
        self.ui.ramHisGraph.clear()

        # Add the ImageItem to the plot
        self.ui.ramHisGraph.addItem(image_item)



    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())