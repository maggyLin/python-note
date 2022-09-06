import cv2
import pyzbar.pyzbar as pyzbar

image=cv2.imread("barEx2.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
texts = pyzbar.decode(gray)
if texts==[]:
    print("未識別成功")
else:
    for text in texts:
        tt = text.data.decode("utf-8")
    print("識別成功")
    print(tt)