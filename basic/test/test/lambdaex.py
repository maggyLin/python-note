# lambda 匿名函數就是指一個沒有名稱的函數
# lambda arg1, arg2, ... : expression

# add = lambda x,y : x+y
# print(add(1,3))

# # 次方 **
# pow = lambda x,y: x**y
# print(pow(2,3))

def maxfun():
    return lambda x,y: x if x>y else y

re = maxfun()
print(re(2,5))