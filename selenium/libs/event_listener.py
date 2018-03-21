from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
import os, time, sys, traceback, datetime
from time import sleep

dir = os.path.dirname
SCREEN_SHOT_DIR = dir(dir(dir(os.path.abspath(__file__)))) + '/screen_shot/'

"""
  MyListener Class
  ※ MyListenerクラスは、AbstractEventListenerクラスのサブクラスです
  ※ AbstractEventListenerクラスでは、関数がダミー実装されており、MyListenerクラスで関数をオーバーライドします

"""
class MyListener(AbstractEventListener):

    def on_exception(self, exception, driver):
        """
          Exception発生後の処理
          ※ スクリーンショット
        """
        sleep(1)
        dt = datetime.datetime.today()
        screenshot_name = 'error.' + dt.strftime("%Y%m%d%H%M%S") + '.png'
        driver.save_screenshot(SCREEN_SHOT_DIR + screenshot_name)
        print("[Error] exception: error occurred. (screenshot saved as '%s')" % screenshot_name)

    def before_navigate_to(self, url, driver):
        """
          URLが遷移する直前の処理
          ※ driver.get()
        """
        #print("[debug] before navigate To: " + driver.current_url)
        pass

    def after_navigate_to(self, url, driver):
        """
          URLが遷移する直後の処理
          ※ driver.get()
        """
        #print("[debug] after navigate To: " + driver.current_url)
        pass

    def before_change_value_of(self, element, driver):
        """
          要素の値が変更される直前の処理
          ※ driver.send_keys()
          ※ driver.clear()
        """
        #print("[debug] before change value of: " + element.get_attribute("value"))
        pass

    def after_change_value_of(self, element, driver):
        """
          要素の値が変更される直後の処理
          ※ driver.send_keys()
          ※ driver.clear()
        """
        #print("[debug] after change value of: " + element.get_attribute("value"))
        pass

    def before_click(self, element, driver):
        """
          要素がクリックされる直前の処理
          ※ driver.click()
        """
        #print("[debug] before click: " + driver.current_url)
        pass

    def after_click(self, element, driver):
        """
          要素がクリックされる直後の処理
          ※ driver.click()
        """
        #print("[debug] after click: " + driver.current_url)
        pass

    def before_navigate_back(self, driver):
        """
          ブラウザの『戻る』直前の処理
          ※ driver.back()
        """
        #print("[debug] before navigate(back): Title is " + driver.title)
        pass

    def after_navigate_back(self, driver):
        """
          ブラウザの『戻る』直後の処理
          ※ driver.back()
        """
        #print("[debug] after navigate(back): Title is " + driver.title)
        pass

    def before_navigate_forward(self, driver):
        """
          ブラウザの『進む』直前の処理
          ※ driver.forward()
        """
        #print("[debug] before navigate(forward): Title is " + driver.title)
        pass

    def after_navigate_forward(self, driver):
        """
          ブラウザの『進む』直後の処理
          ※ driver.forward()
        """
        #print("[debug] after navigate(forward): Title is " + driver.title)
        pass

    def before_find(self, by, value, driver):
        """
          要素を検索する直前の処理
          ※ driver.find_element(), driver.find_element_***()
          ※ driver.find_elements(), driver.find_elements_***()
        """
        #print("[debug] before find element")
        pass

    def after_find(self, by, value, driver):
        """
          要素を検索する直後の処理
          ※ driver.find_element(), driver.find_element_***()
          ※ driver.find_elements(), driver.find_elements_***()
        """
        #print("[debug] after find element")
        pass

    def before_execute_script(self, script, driver):
        """
          Javascriptを実行した前の処理
          ※ driver.execute_script()
          ※ driver.execute_async_script()
        """
        #print("[debug] before javaScript")
        pass

    def after_execute_script(self, script, driver):
        """
          Javascriptを実行した後の処理
          ※ driver.execute_script()
          ※ driver.execute_async_script()
        """
        #print("[debug] after javaScript")
        pass

    def before_close(self, driver):
        """
          ブラウザ(タブ別)が終了する前の処理
          ※ driver.close()
        """
        #print("[debug] before close")
        pass

    def after_close(self, driver):
        """
          ブラウザ(タブ別)が終了した後の処理
          ※ driver.close()
        """
        #print("[debug] after close")
        pass

    def before_quit(self, driver):
        """
          ブラウザ(すべて)が終了する前の処理
          ※ driver.quit()
        """
        #print("[debug] before quit")
        pass

    def after_quit(self, driver):
        """
          ブラウザ(すべて)が終了した後の処理
          ※ driver.quit()
        """
        #print("[debug] after quit")
        pass
