# with open(檔案路徑,mode=開啟模式) as 檔案物件:
    # 讀取或寫入檔案的程式
    # 以上區塊會自動、安全地關閉檔案
    # 不需要另外再寫close()
    

file = open("data.txt", mode="w",encoding="utf-8") # 開啟(沒有會建立)
file.write("你好")  # 操作(會直接覆蓋原本內容)
file.close()        # 關閉

# 不用自己寫close
# with open("data.txt", mode="w", encoding="utf-8") as file:
#   file.write("測試中文\n好棒棒")


# 讀取檔案 mode=r , 一定要有讀取的檔案不然會報錯
with open("data.txt", mode="r", encoding="utf-8") as file:
  data = file.read()
print(data)


# # 讀取檔案
# # 把檔案中的數字資料，一行行讀取出，並計算總和
# with open("data.txt", mode="w", encoding="utf-8") as file:
#   file.write("5\n3")
# sum = 0
# with open("data.txt", mode="r", encoding="utf-8") as file:
#   for line in file:  # 一行行讀取
#     sum+=int(line)
# print(print)


# # 使用JSON格式讀取、複寫檔案 ================
import json

with open("config.json",mode="r") as file:
    data = json.load(file)
print("version : ",data["version"])

# 修改資料
data["name"] = "new name"
# 更新回json file
with open("config.json",mode="w") as file:
    json.dump(data,file)