import pandas as pd

# 建立 series
# data = pd.Series([20,10,15])
# print(data)
# print(data.max())
# print(data.median())
# getDouble = data*2 #將資料都*2

#將每個資料都執行 ==20 判斷式,回傳bool Series
# checkdata = data==20
# print(checkdata)



# 建立 DataFrame
data = pd.DataFrame({
    "name":["Mary","John","Bob"],
    "salary":[300,400,500]
})
print(data)

# 特定 row
print(data.iloc[0])