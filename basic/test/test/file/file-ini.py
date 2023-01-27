# 解析 ini 檔的內容結構
# 建立 configparser 物件後使用 config.read() 將 ini 檔內容讀取進來，之後再用字典的方式來取得資料
import configparser

config = configparser.ConfigParser()
config.read('Setting.ini')

StartX = config['Camera']['StartX']
StartY = config['Camera']['StartY']
print(StartX)
print(StartY)
