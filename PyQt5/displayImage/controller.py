from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog
import cv2

from UI import Ui_MainWindow

# https://ithelp.ithome.com.tw/articles/10273455

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()


    def setup_control(self):
        # TODO        
        self.img_path = 'cat.jpg'
        self.ui.ZommInButton.clicked.connect(self.func_zoom_in) 
        self.ui.ZommOutButton.clicked.connect(self.func_zoom_out)
        self.ui.scrollArea.setWidgetResizable(True)
        self.ui.imgLabel.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        # self.ui.imgLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter) # 將圖片置中
        self.display_img()

    def display_img(self):
        self.img = cv2.imread(self.img_path)
        height, width, channel = self.img.shape
        bytesPerline = 3 * width
        self.qimg = QImage(self.img, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.qpixmap = QPixmap.fromImage(self.qimg)
        self.qpixmap_height = self.qpixmap.height()
        self.ui.imgLabel.setPixmap(QPixmap.fromImage(self.qimg))
        
    def func_zoom_in(self):
        self.qpixmap_height -= 100
        self.img_resize()

    def func_zoom_out(self):
        self.qpixmap_height += 100
        self.img_resize()

    def img_resize(self):        
        scaled_pixmap = self.qpixmap.scaledToHeight(self.qpixmap_height)
        print(f"current img shape = ({scaled_pixmap.width()}, {scaled_pixmap.height()})")
        self.ui.infoLabel.setText(f"current img shape = ({scaled_pixmap.width()}, {scaled_pixmap.height()})")
        self.ui.imgLabel.setPixmap(scaled_pixmap)