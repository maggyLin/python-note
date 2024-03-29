from PyQt5 import QtWidgets
import socket, time, sys, cv2

import da3c4
Title = "DA3C1"


app = QtWidgets.QApplication(sys.argv)

ATS = da3c4.MainWindow()
ATS.show()

# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.connect(('8.8.8.8', 80))
# localhost = s.getsockname()[0]
# s.close()

connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect.bind((localhost, 9567))
connect.bind(("127.0.0.1", 9567))
connect.listen()
connect.setblocking(False)

while True:
    try:
        conn, addr = connect.accept()
        start = time.time()
        ATS.btn_status()
        end = time.time()
        title = Title
        result = "OK" if ATS.result else "NG"
        timer = int(end - start)
        conn.send(f"{title},{result},{timer}".encode())
        conn.close()

    except:
        time.sleep(0.1)
        cv2.waitKey(100)

sys.exit(app.exec_())
