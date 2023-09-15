import urllib.request as req
from bs4 import BeautifulSoup
import requests
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager
import ssl

# Python 3 urllib ignore SSL certificate verification (for urlopen para context)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://keyserver2.cloud.d2tech.com/auth/login"

# method 1
reqCon = req.Request(url,headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
})
with req.urlopen(reqCon,timeout=5, context=ctx) as response:
    data = response.read().decode("utf-8")
print(data)


# method 2 
# verify=False (ignore SSL certificate verification)
# r = requests.get("https://keyserver2.cloud.d2tech.com/auth/login",verify=False) #將此頁面的HTML GET下來
# print(r.text) #印出HTML


