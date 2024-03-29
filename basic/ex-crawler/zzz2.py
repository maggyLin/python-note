import urllib.request as req
import ssl
import urllib
from urllib.error import HTTPError

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

get_cookie = ""

print("===============================================================================")
print(" [POST] login")

# url = "https://keyserver2.cloud.d2tech.com/key/keygen"
url = "https://keyserver2.cloud.d2tech.com/auth/login"

reqdata={
    "name": "qualcomm-wnc",
    "pwd": "Qa32Po29"
}
send_data = urllib.parse.urlencode(reqdata)
send_data = send_data.encode()

reqCon = req.Request(url,headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
},data=send_data)

try:
    with req.urlopen(reqCon,timeout=5, context=ctx) as response:
        data = response.read().decode("utf-8")
        print(data)

        # cookie = response.info().get_all('Set-Cookie')
        get_cookie = response.info()['Set-Cookie']
        # content_type = response.info()['Content-Type']
        print(get_cookie)
except HTTPError as err:
    print("err status: {0}".format(err))

print("===============================================================================")
print(" [Get] keygen ")

url = "https://keyserver2.cloud.d2tech.com/key/keygen"
reqCon = req.Request(url,headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    # "Cookie":"session=eyJyb2xlIjozLCJ1aWQiOjYsInVzZXJuYW1lIjoicXVhbGNvbW0td25jIn0.ZQO84A.4wjCyvBqVjK_KVTjkV9LgO6iIHI"
    "Cookie":get_cookie
})
with req.urlopen(reqCon,timeout=5, context=ctx) as response:
    data = response.read().decode("utf-8")
print(data)
