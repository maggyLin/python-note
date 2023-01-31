import urllib.request as req

url = "https://www.ptt.cc/bbs/movie/index.html"

# 直接抓取會報 403:forbidden
# with req.urlopen(url) as response:
#     data = response.read().decode("utf-8")
# print(data)

request = req.Request(url,headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
# print(data)

# 解析資料
import bs4

root = bs4.BeautifulSoup(data,"html.parser")
# print(root.title)  #抓到標籤
# print(root.title.string)  #抓到標籤內文字


#find 找到1筆, find_all 找到所有
articles = root.find_all("div", class_="title")
for con in articles:
    if con.a != None:
        print(con.a.string)
    else:
        print(con.string) 