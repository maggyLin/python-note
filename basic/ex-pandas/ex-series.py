# 載入 pandas 模組
import pandas as pd

# 資料索引
# data=pd.Series([5,4,-2,3,7])  # 預設index 0,1,2...
data=pd.Series([5,4,-2,3,7],index=["a","b","c","d","e"]) # 要注意 : 要建立自己的索引，索引數量要和資料數量一樣
print(data)
print("================")

# 觀察資料
print("資料型態",data.dtype)
print("資料數量",data.size)  
print("資料索引",data.index)
print("================")

# 取得資料 : 根據順序、根據索引
print(data[2],data[0])
print(data["e"],data["d"])  
print("================")

# 數字運算 : 基本、統計、順序
print("最大值",data.max())
print("總和",data.sum())
print("標準差",data.std())
print("中位數",data.median())
print("最大的三個數",data.nlargest(3))
print("最小的兩個數",data.nsmallest(2))
print("================")

# 字串運算 : 基本、串接、搜尋、取代
data=pd.Series(["您好","Python","Pandas"])
print("全部變小寫",data.str.lower())   # 中文不受影響
print("每個字串的長度",data.str.len())
print(data.str.cat(sep=",")) # 把字串串起來，可以自訂串接的符號
print(data.str.cat(sep="-"))  
print(data.str.contains("P")) # 判斷每個字串是否包含特定的字元
print(data.str.contains("好")) # 會回傳 bool 的 series
print(data.str.replace("您好","Hello"))  #取代