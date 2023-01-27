# print("Hello python!!")

# n1 = 333
# print(type(n1))

# s = input()
# print(s)


# grade = 60
# if grade >= 90:
#     print('great')
# elif grade >= 60:
#     print('good')
# else:
#     print('bad')


# myList = ['apple','banana','orange']
# for i in range(len(myList)):
#     print('index '+ str(i) +" : "+ myList[i])

# # 反轉
# for i in reversed(range(5)):
#     print(str(i))

# mylist = ['apple', 'banana', 'orange']
# for i in mylist:
#     print(i)


count = 0
while (count < 5):
   print('Count:' + str(count))
   count += 1
else: # 迴圈結束時會執行這裡, 但 break 跳離時不會執行到這裡
    print('else, Count:' + str(count))
