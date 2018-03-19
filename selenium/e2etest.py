import unittest
import os
from browser import Browser

"""E2Eテスト
E2Eテストクラスを定義します。
"""
class E2ETest(unittest.TestCase):
    domain = {
        'prod' : 'https://www.qlife.jp',
        'qa'   : 'https://kht.qlife.jp',
        'dev'  : 'https://www.lan.qlife.co.jp',
        'local': 'https://local-www.lan.qlife.co.jp'
    }
    browser = None
    run_env = ''
    wait_ajax_time = 2

    """初期化"""
    def setUp(self):
        self.browser = Browser()
        self.run_env = os.getenv('RUN_ENV', None)

    """テスト終了"""
    def tearDown(self):
        print("ブラウザー終了")
        self.browser.quitBrowser()

    """URLを生成する(QLife)
    Args:
        self: E2ETest instance
        path: string
    Returns:
        string
    """
    def fullUrl(self, path):
        if self.is_production():
            url = self.domain['prod']
        else:
            print("環境変数に「RUN_ENV」が設定されません → KHTでテストになります")
            url = self.domain['qa']
        print(url);

        return url + path

    """環境判定(production)
    本番環境かどうかを判定します。
    Returns:
        boolean
    """
    def is_production(self):
        if self.run_env == 'production':
            return True
        else:
            return False

    """環境判定(testing)
    Staging(QA)環境かどうかを判定します。
    Returns:
        boolean
    """
    def is_testing(self):
        if self.run_env == 'testing':
            return True
        else:
            return False

    """環境判定(development)
    開発環境かどうかを判定します。
    Returns:
        boolean
    """
    def is_development(self):
        if self.run_env == 'development':
            return True
        else:
            return False

    """環境判定(local)
    ローカル環境かどうかを判定します。
    Returns:
        boolean
    """
    def is_local(self):
        if self.run_env == 'local':
            return True
        else:
            return False

    """URLを生成する
    Args:
        self: E2ETest instance
        path: string
    Returns:
        string
    """
    def url(self, path):
        if self.is_production():
            url = self.domain['prod'] + path
        elif self.is_testing():
            url = self.domain['qa'] + path
        elif self.is_local():
            url = self.domain['local'] + path
        else:
            url = self.domain['dev'] + path
        print(url)
        return url
