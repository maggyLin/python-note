import pandas as pd

data = pd.Series([30,15,20])
condition = [True,False,True]  # filter 條件
filteredData = data[condition]
print(filteredData)

# 篩選練習 - Series02
data = pd.Series([30,15,20])
condition = data > 18
print(condition)  # 根據條件取得 filter 條件
filteredData = data[condition]  # 根據filter 條件取得符合的資料
print(filteredData)


data = pd.Series(["您好","Python","Pandas"])
condition = data.str.contains("P")
print(condition)
filteredData = data[condition]
print(filteredData)



# 篩選練習 - DataFrame
data = pd.DataFrame({
    "name":["Amy","Bab","Charles"],
    "salary":[30000,50000,40000]
})
condition = data["salary"]>=40000
print(condition)
filteredData = data[condition]
print(filteredData)


data = pd.DataFrame({
    "name":["Amy","Bab","Charles"],
    "salary":[30000,50000,40000]
})
condition = data["name"]=="Amy"
print(condition)
filteredData = data[condition]
print(filteredData)