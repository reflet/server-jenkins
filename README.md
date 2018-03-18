
# Jenkins 環境

docker-composeコマンドを使っての操作方法を記載します。

## ミドルウェア構成

- Jenkins
- Selenium (Python3) ※ E2Eテスト
- Selenium-hub
- Chrome
- fabric (Python3) ※デプロイ

## 起動方法について（ RUN ）

下記のコマンドにてコンテナを起動します。 (port 4444 / 5900 is available)

```
$ git clone https://github.com/reflet/server-jenkins.git .
$ docker-compose up -d
```

## Jenkinsの起動
Vagrant (192.168.33.30)で起動した場合は、下記URLで操作画面へアクセスできます。

* http://192.168.33.30:8080

## Jenkinsのロック解除

はじめて上記URLへアクセスした場合、Unlock Jenkinsという画面が表示されます。

ロック解除のパスワードは以下のコマンドから取得可能です。

```
$ docker exec jenkins bash -c "cat /var/jenkins_home/secrets/initialAdminPassword"
```

## Seleniumテストの実行

Jenkinsコンテナへ接続する。
```
$ docker exec -it jenkins bash
```

JenkinsコンテナからSeleniumテストを実行してみる。

```
# docker exec selenium bash -c "python /root/opt/python_org_search.py"
```

以上