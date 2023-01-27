import urllib.request as request
import json

# data.taipei open api
src = "	https://tinyurl.com/yvtzcthz"

with request.urlopen(src) as response:
    # data = response.read()
    # data = response.read().decode("utf-8") # 指定編碼
    data  = json.load(response)  

# print(data)

# 抓取資料
namelist = data["data"]
# 寫入txt file
with open("ex-req-data.txt","w", encoding="utf-8") as file:
    for name in namelist:
        file.write(name["stationName"]+"\n")