from selenium import webdriver
from localstorageModal import LocalStorage


driver = webdriver.Chrome(r'.\chromedriver.exe')
# driver.get('http://10.59.100.50/WebUITest/')
driver.get('http://127.0.0.1/pythontest/test.html')


# 获取 local storage
storage = LocalStorage(driver)
storage.set("aaa","bbbb")
print(storage.get("aaa"))



# driver.execute_script("window.localStorage.setItem('abc','111');")
# lo = driver.execute_script("return window.localStorage.getItem('abc');")
# print(lo)



