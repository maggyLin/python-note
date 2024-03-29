import urllib.request as req
import requests
import ssl


# import requests
# from urllib3.exceptions import InsecureRequestWarning

# # Suppress only the single warning from urllib3 needed.
# requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# session = requests.Session()
# session.verify = False


# ssl._create_default_https_context = ssl._create_unverified_context

# r = requests.get("https://keyserver2.cloud.d2tech.com/auth/login") 
# # r = requests.get("https://keyserver2.cloud.d2tech.com/auth/login",verify=False) 
# print(r.text)


import requests, os
session = requests.Session()
session.verify = False
session.trust_env = False
os.environ['CURL_CA_BUNDLE']="" # or whaever other is interfering with 
session.get("https://keyserver2.cloud.d2tech.com/auth/login")
