
# Selenium + python3 Server

docker-composeコマンドを使っての操作方法を記載します。

## 起動方法について（ RUN ）

下記のコマンドにてコンテナを起動します。 (port 4444 / 5900 is available)

```
$ git clone https://github.com/reflet/server-selenium-python3.git .
$ docker-compose up -d
```

## pythonコンテナにseleniumをインストール

下記のコマンドにてコンテナ内に入ってインストールの作業を行う。

```
$ docker exec -it python bash
```

コンテナ内での作業

```
# python --version
Python 3.6.2

# apt-get -y update && apt-get install -y vim

# pip install --upgrade pip
# pip install selenium
Collecting selenium
  Downloading selenium-3.5.0-py2.py3-none-any.whl (921kB)
    100% |████████████████████████████████| 921kB 1.2MB/s 
Installing collected packages: selenium
Successfully installed selenium-3.5.0
```

## テストについて（ TEST ）

下記コマンドにて、簡易テストを実行してみる

```
# python
Python 3.6.2 (default, Aug 29 2017, 05:52:11) 
[GCC 4.9.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from selenium import webdriver
>>> from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
>>> driver = webdriver.Remote(
    command_executor='http://selenium-hub:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME)
>>> driver.get("http://qiita.com/reflet")
>>> driver.close()
```

※ VNCでサーバへ接続していれば、画面にてchromeが起動し、qiitaの画面へ移動することが確認できます。


