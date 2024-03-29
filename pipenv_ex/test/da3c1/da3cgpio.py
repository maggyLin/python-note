from tai import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage, QPixmap, QCloseEvent
from PyQt5 import QtGui, QtWidgets
from configobj import ConfigObj
import RPi.GPIO as GPIO
import cv2, os, sys, time, socket

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_status)

        # Read Setting.ini
        self.comport = self.readINI("Setting", "Setting", "COM")
        self.Baudrate = self.readINI("Setting", "Setting", "Baudrate")
        self.Count_1 = self.readINI("Setting", "Setting", "Count_1")
        self.Count_2 = self.readINI("Setting", "Setting", "Count_2")
        self.localhost = self.readINI("Setting", "Setting", "localhost")
        self.OverTime = self.readINI("Setting", "Setting", "timeout")
        
        self.pote = [[17, 27, 22], [10, 9, 11], [13, 19, 26], [14, 15, 18], [8, 7, 1], [16, 20, 21]]

        self.status = False

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
            print('stop running fail')

        try:
            self.server.close()
        except:
            print('close socket fail')
        
        sys.exit(0)

    def btn_status(self):
        self.status = not self.status

        if self.status:
            self.pushButton.setText("Stop")
            result = True

            if int(self.Count_1) > 0:
                result = result and self.run(self.pote[1], int(self.Count_1))

            if int(self.Count_2) > 0:
                result = result and self.run(self.pote[2], int(self.Count_2))

            if result:
                self.label.setStyleSheet("background-color: lime")
                self.label.setText("PASS")
            else:
                self.label.setStyleSheet("background-color: red")
                self.label.setText("NG")

        else:
            self.pushButton.setText("Start")
            self.label.setStyleSheet("background-color: None")
            self.label.setText("Pause")

    def running(self):
        # building socket connect
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.localhost, 9567))
        self.server.listen()
        self.server.setblocking(False)
        
        while True:
            try:
                conn, addr = self.server.accept()
                self.status = True
                self.pushButton.setEnabled(False)
                result = True
                
                if int(self.Count_1) > 0:
                    result = result and self.run(self.pote[1], int(self.Count_1))

                if int(self.Count_2) > 0:
                    result = result and self.run(self.pote[2], int(self.Count_2))

                if result:
                    self.label.setStyleSheet("background-color: lime")
                    self.label.setText("PASS")
                    conn.send("DA3C1,PASS,30".encode())
                else:
                    self.label.setStyleSheet("background-color: red")
                    self.label.setText("NG")
                    conn.send("DA3C1,NG,30".encode())
                
                self.pushButton.setEnabled(True)
                self.status = False
                conn.close()
            except:
                time.sleep(0.1)
                cv2.waitKey(100)

    def GcErase(self, p1, p2, p3):
        self.label.setStyleSheet("background-color: yellow")
        self.label.setText("Warning")
        count = 1
        
        while self.status:
            try:
                GPIO.setmode(GPIO.BCM)
                GPIO.setwarnings(False)
            except Exception as e:
                 print(e.args)

            GPIO.setup(p1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.setup(p2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.setup(p3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            
            try: 
                GPIO.input(p1)
                GPIO.input(p2)
                GPIO.input(p3)
                break
            except Exception as ex:
                self.textEdit.append("Retry count : " + str(count))
                self.textEdit.append(str(ex))
                print ("open GPIO port error " + str(ex))

            time.sleep(2)
            cv2.waitKey(2000)
            count += 1

    def run(self, CheckPote, CheckCount):
        while self.status:
            p1, p2, p3 = CheckPote
            self.GcErase(p1, p2, p3)
            self.textEdit.clear()
            self.label.setStyleSheet("background-color: aqua")
            self.label.setText("Testing")
            begin = time.time()
            ready = False

            while self.status:
                try:
                    response = f"{GPIO.input(p1)}{GPIO.input(p2)}{GPIO.input(p3)}"
                    time.sleep(0.1)		# wait 0.1 second
                    cv2.waitKey(100)
                    self.textEdit.append(str(response))
                    self.textEdit.moveCursor(QTextCursor.End)
                    
                    if (time.time() - begin) > float(self.OverTime):
                        self.create_log("INFO", "result:Timeout")
                        return False					# return x
                    elif (response == '111'):
                    # running code
                        ready = True
                    elif ready and (response == '110'):
                    # error code
                        self.create_log("WARN", f"Event:Use Error")
                        ready = False
                    elif ready and (response == '101'):
                    # seccuss code
                        CheckCount = CheckCount - 1
                        begin = time.time()
                        ready = False
                    elif (response == '010'):
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

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()

    sys.exit(app.exec_())
