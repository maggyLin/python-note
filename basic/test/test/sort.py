#list.sort(cmp=None, key=None, reverse=False)
# cmp︰ 指定一個比較函式的話，會使用該比較函式進行排序
# key︰ 指定元素的某一列為key鍵值, 也就是按照元素的某一列來進行排序
# reverse︰排序規則，reverse=True 降序，reverse=False 升序（預設）。

# list1 = [4, 5, 8, 3, 7, 1, 2, 6, 10, 9]
# list1.sort()
# print("result:", list1)
# list1.sort(reverse=True)  #True寫法固定(不可以小寫)
# print("result re:", list1)


# import numpy as np
# a = np.array([[7, 5, 9],
#               [4, 8, 6],
#               [1, 2, 3]])

# print(a[a[:1].argsort()])
