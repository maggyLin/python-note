### update
> python -m pip install --upgrade pip


### 使用proxy? 公司檔網域
> pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org [package_name]


### Win10 怎麼樣都無法安裝時....(python setup.py egg_info" failed with error code 10...)
> 使用本地install

1. 安裝 pip install wheel
2. 下載對應python的安裝包 [XXX.whl] (https://www.lfd.uci.edu/~gohlke/pythonlibs/)
3. 直接 pip install [XXX.whl]

> 以 PycURL 為例子
1. 確認已經下載 wheel
2. 到 https://www.lfd.uci.edu/~gohlke/pythonlibs/ 下載對應安裝包, python3.8 , win10 64 => pycurl‑7.45.1‑cp38‑cp38‑win_amd64.whl
3. pip install pycurl‑7.45.1‑cp38‑cp38‑win_amd64.whl
