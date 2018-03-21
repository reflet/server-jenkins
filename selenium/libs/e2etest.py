import unittest, os

from libs.browser import Browser
from libs.event_listener import MyListener
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

"""
 E2Eテスト Class
 ※ E2Eテストクラスを定義します
"""
class E2ETest(unittest.TestCase):
    domain = {
        'prod' : 'https://www.example.com',
        'qa'   : 'https://www.qa-example.com',
        'dev'  : 'https://www.dev-example.com',
        'local': 'https://www.local-example.com'
    }
    run_env = ''
    browser = None
    wait_ajax_time = 2

    """初期化"""
    def setUp(self):
        self.run_env = os.getenv('RUN_ENV', None)
        self.browser = Browser()

    """テスト終了"""
    def tearDown(self):
        print("close browser")
        self.browser.quit()

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
