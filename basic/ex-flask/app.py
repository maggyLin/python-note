from flask import Flask

app=Flask(__name__) #__name__ 表示目前執行的模組

@app.route("/")
def home():
    return "Hello World!"

@app.route("/test")
def test():
    return "into test page"

# 如果是主程式執行,則啟動伺服器
if __name__=="__main__":
    app.run()