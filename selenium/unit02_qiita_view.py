#!/usr/bin/python
import unittest, time

from libs.e2etest import E2ETest

"""
   シナリオ No.02 Qiitaページを閲覧する
   
    ex)
    $ RUN_ENV='testing' && python /root/opt/unit02_qiita_view.py
"""
class TestSample(E2ETest):

    def test_page_view(self):
        print("""
        ＿／＿／＿／＿／＿／＿／＿／＿／＿／＿／＿／＿／
          シナリオ No.02 Qiitaページを閲覧する
          (unit02_qiita_view.py)
        ＿／＿／＿／＿／＿／＿／＿／＿／＿／＿／＿／＿／
        """)

        # ブラウザ起動
        self.browser.openChrome()
        driver = self.browser.driver

        # ページを開く
        driver.get('http://qiita.com/reflet')

##### MAIN #####
if __name__ == "__main__":
    unittest.main()