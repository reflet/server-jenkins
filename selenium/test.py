#!/usr/bin/python

import unittest, time
from e2etest import E2ETest
from selenium.common.exceptions import TimeoutException

"""
   検索シナリオ No.1 Qiitaページ
   
    ex)
    $ export RUN_ENV='testing'
    $ python /root/opt/test.py
"""
class TestSearch0001(E2ETest):

    RETRIES = 3
    PAGE_LOAD_TIMEOUT = 10

    def test_hospital_search(self):
        print("""
        ＿／＿／＿／＿／＿／＿／＿／＿／＿／＿／＿／＿／
          検索シナリオ No.1 Qiitaページテスト
          (test.py)
        ＿／＿／＿／＿／＿／＿／＿／＿／＿／＿／＿／＿／
        """)

        # ブラウザ起動
        self.browser.openChrome()
        driver = self.browser.driver
        driver.maximize_window()  # 最大化
        driver.implicitly_wait(2) # 暗黙の待機(2秒)

        # ページの読み込み待ち時間(秒)
        driver.set_page_load_timeout(self.PAGE_LOAD_TIMEOUT)

        i = 0
        while i < self.RETRIES:
            try:
                # 検索フォーム
                driver.get('http://qiita.com/reflet')

            except TimeoutException:
                i = i + 1
                print("Timeout, Retrying... (%(i)s/%(max)s)" % {'i': i, 'max': self.RETRIES})
                continue

            else:
                return True

        msg = "Page was not loaded in time(%(second)s sec)." % {'second': self.PAGE_LOAD_TIMEOUT}
        raise TimeoutException(msg)

##### MAIN #####
if __name__ == "__main__":
    unittest.main()
