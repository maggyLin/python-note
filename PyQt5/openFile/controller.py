from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog
import cv2

from UI import Ui_MainWindow

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.ui.openFile.clicked.connect(self.open_file) 
        self.ui.openFolder.clicked.connect(self.open_folder)

    def open_file(self):
        #回傳路徑與副檔名
        filename, filetype = QFileDialog.getOpenFileName(self,
                  "Open file",          # 視窗上方標題列的名稱
                  "./")                 # start path ,「"./"」就是當前目錄
        print(filename, filetype)
        self.ui.fileText.setText(filename)

    def open_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self,
                  "Open folder",
                  "./")                 # start path
        print(folder_path)
        self.ui.folderText.setText(folder_path)