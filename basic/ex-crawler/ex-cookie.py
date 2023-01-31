import urllib.request as req


def getData(url):
    # 此網站需要帶cookie
    request = req.Request(url,headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "cookie":"over18=1"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    # print(data)

    # 解析資料
    import bs4

    root = bs4.BeautifulSoup(data,"html.parser")

    #find 找到1筆, find_all 找到所有
    # articles = root.find_all("div", class_="title")
    # for con in articles:
    #     if con.a != None:
    #         print(con.a.string)
    #     else:
    #         print(con.string) 


    # 抓取上頁標籤,並找到連結
    nextbtn = root.find("a",string="‹ 上頁")
    nextLink = nextbtn["href"]
    return nextLink

# 抓取指定數量頁面資料
pageURL = "https://www.ptt.cc/bbs/Gossiping/index.html"
count = 0
while count<5:
    print(pageURL)
    # 抓取的url為相對路徑
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1