from PyQt5 import QtWidgets, QtGui, QtCore

from UI import Ui_MainWindow

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        # TODO
        # qpushbutton doc: https://doc.qt.io/qt-5/qpushbutton.html
        self.ui.buttonTest.setText('Print message!')
        self.clicked_counter = 0
        self.ui.buttonTest.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        self.clicked_counter += 1
        print(f"You clicked {self.clicked_counter} times.")


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow_controller()
    window.show()
    sys.exit(app.exec_())