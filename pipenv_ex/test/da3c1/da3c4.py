from tai import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage, QPixmap, QCloseEvent
from PyQt5 import QtGui, QtWidgets
from configobj import ConfigObj
import threading, serial, time
import cv2, os, sys, socket

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_status)  # start button

        # Read Setting.ini
        self.comport = self.readINI("Setting", "Setting", "COM")
        self.password = self.readINI("Setting", "Setting", "Password")
        self.Baudrate = self.readINI("Setting", "Setting", "Baudrate")
        self.Count_1 = self.readINI("Setting", "Setting", "Count_1")
        self.Count_2 = self.readINI("Setting", "Setting", "Count_2")
        self.localhost = self.readINI("Setting", "Setting", "localhost")
        self.OverTime = self.readINI("Setting", "Setting", "timeout")
        self.status = False
        self.isStop = False
        

    # Read ini File
    def readINI(self, FileName, AppName, KeyName):
        config = ConfigObj(FileName + ".ini", encoding='UTF8')
        KeyName_value = config[AppName][KeyName]
        return KeyName_value

    # write log
    def create_log(self, level, data):
        ntime = time.localtime(time.time())
        path = "log/" + time.strftime("%Y%m%d", ntime)
        name = path + '/' + time.strftime("%H", ntime) + '.txt'

        fformat = '[{} {}]'.format(time.strftime("%Y%m%d %H:%M:%S", ntime), level)

        if not os.path.isdir(path):
            os.mkdir(path)              # create new dir

        f = open(name, "a")
        f.write(fformat + data + "\n")
        f.close() 

    # Close Window Event
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        try:
            self.status = True
        except:
            print('stop working fail')

        try:
            self.server.close()
        except:
            print('close socket fail')

        try:
            self.ser.close()
        except:
            print('Serial Close error')
        
        sys.exit(0)

    def btn_status(self):
        self.status = not self.status
        self.result = True
        
        self.isStop = False
        
        print("btn_status ", self.status)
        
        if self.status:
            self.pushButton.setText("Stop")
            if int(self.Count_1) > 0:
                self.result = self.result and self.signal(4, int(self.Count_1))
            if int(self.Count_2) > 0:
                self.result = self.result and self.signal(5, int(self.Count_2))
            
            # get result 判斷結果
            if self.result:
                self.label.setStyleSheet("background-color: lime")
                self.label.setText("PASS")
                self.pushButton.setText("Start")
            else:
                self.label.setStyleSheet("background-color: red")
                self.label.setText("NG")
                self.pushButton.setText("Start")

            self.status = False
        else:
            self.pushButton.setText("Start")
            self.label.setStyleSheet("background-color: None")
            self.label.setText("Pause")
            self.isStop = True
        

    # serial buffer reset
    def ClearSerialPortBuffer(self, ser):
        ser.flushInput()		# flush input buffer
        ser.flushOutput()		# flush output buffer

    def GcErase(self):
        self.label.setStyleSheet("background-color: yellow")
        self.label.setText("Warning")
        count = 1
        while self.status:
            try:
                # COM port permission denied
                if (self.readINI("Setting", "Setting", "OS") == "linux"):
                    os.system(rf"echo '{self.password}' | sudo -S chmod 777 {self.comport}")
            except Exception as e:
                print(e.args)
                 
            try:
                self.ser.close()
                print('start before Serial Close')
            except:
                print('Serial Close error')

            ser = serial.Serial()
            ser.port = self.comport
            ser.baudrate = self.Baudrate
            ser.timeout = 0.5		# non-block read 0.5s
            ser.writeTimeout = 0.5	# timeout for write 0.5s
            
            try: 
                if not ser.isOpen():
                    ser.open()
                ser.write(b'status\r\n')
                ser.read()
                return ser
            except Exception as ex:
                self.textEdit.append("Retry count : " + str(count))
                self.textEdit.append(str(ex))
                print ("open serial port error " + str(ex))

            time.sleep(2)
            cv2.waitKey(2000)
            count += 1


    def signal(self, CheckPote, CheckCount):
        while self.status:
            self.ser = self.GcErase()
            self.textEdit.clear()
            self.label.setStyleSheet("background-color: aqua")
            self.label.setText("Testing")
            begin = time.time()
            ready = False

            while self.ser and self.ser.isOpen():
                try:
                    
                    self.ClearSerialPortBuffer(self.ser)

                    self.ser.write(b'status\r\n')
                    response = str(self.ser.read())
                    time.sleep(0.1)			# wait 0.1 second
                    cv2.waitKey(100)
                    
                    if not self.isStop :  # 不是在stop下才處理訊號
                        self.textEdit.append(str(response))
                        self.textEdit.moveCursor(QTextCursor.End)
                        
                        if (time.time() - begin) > float(self.OverTime):
                            self.create_log("INFO", "result:Timeout")
                            return False					# return x
                        elif (response[CheckPote] == 'f'):
                        # running code
                            ready = True
                        elif ready and (response[CheckPote] == 'd'):
                        # error code
                            self.create_log("WARN", f"Event:Use Error")
                            return False					# return x
                        elif ready and (response[CheckPote] == 'b'):
                        # seccuss code
                            CheckCount = CheckCount - 1
                            begin = time.time()
                            ready = False
                        elif (response[CheckPote] == 'a'or response[CheckPote] == '3'):
                        # final code
                            if (CheckCount > 1):
                                self.create_log("INFO", f"result:NG")
                                return False				# return x
                            else:
                                self.create_log("INFO", f"result:PASS")
                                return True					# return o
 
                except Exception as ex:
                    self.textEdit.append("error " + str(ex))
                    break
            else:
                self.textEdit.append("open serial port error")

            self.ser.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()

    sys.exit(app.exec_())
