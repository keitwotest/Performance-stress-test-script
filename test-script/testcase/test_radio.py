#coding:UTF-8
"""
--------------------------------------
   File Name：  test_radio
   Description :
   Author :    admin
   Date：     2018/9/13
   E-mail: 3227456102@qq.com
   adb_activity_package：adb shell dumpsys window w |findstr \/ |findstr name=
--------------------------------------
"""

import unittest

from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from common.swipeIconMethod import *

class radio(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # cls.driver = appium_start()
        # sleep(10)
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 设备系统
        desired_caps['platformVersion'] = '5.1'  # 设备系统版本
        desired_caps['deviceName'] = '106D111805004868'  # 设备名称
        desired_caps['appPackage'] = 'cn.yunovo.car.radio'  # 测试app包名
        desired_caps['appActivity'] = 'cn.yunovo.car.radio.RadioActivity'  # 测试appActivity
        desired_caps['noReset'] = 'true'
        desired_caps['unicodeKeyboard'] = 'True'  # 使用unicodeKeyboard的编码方式来发送字符串
        desired_caps['resetKeyboard'] = 'true'  # 将键盘给隐藏
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 启动app
        print("收音机--Start")

    @classmethod
    def tearDownClass(cls):
        sleep(5)
        cls.driver.quit()
        print("End")

    def test_shouyinji(self):
        print("""收音机面板功能""")
        driver = self.driver
        sleep(2)
        driver.find_element_by_id("cn.yunovo.car.radio:id/main_toast_btn").click()
        sleep(0.5)
        driver.find_element_by_id("cn.yunovo.car.radio:id/btn_8").click()
        driver.find_element_by_id("cn.yunovo.car.radio:id/btn_9").click()
        driver.find_element_by_id("cn.yunovo.car.radio:id/btn_5").click()
        sleep(0.5)
        driver.find_element_by_id("cn.yunovo.car.radio:id/btn_ok").click()
        sleep(1)
        print("""搜索电台""")
        driver.find_element_by_id("cn.yunovo.car.radio:id/main_scan_btn").click()  #搜索电台
        driver.find_element_by_id("cn.yunovo.car.radio:id/main_scan_btn").click()
        sleep(0.5)
        driver.find_element_by_id("cn.yunovo.car.radio:id/main_down_btn").click()
        sleep(0.5)
        driver.find_element_by_id("cn.yunovo.car.radio:id/main_up_btn").click()
        sleep(1)
        driver.find_element_by_id("cn.yunovo.car.radio:id/main_rssi_btn").click()  #收音机设置
        sleep(0.5)
        driver.back()
        sleep(0.5)
        driver.find_element_by_id("cn.yunovo.car.radio:id/main_channel_btn").click()
        sleep(0.5)
        try:
            driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "FM")]')
            scrollXpath = '//*[@resource-id="cn.yunovo.car.radio:id/listview"]'
            scrollView = driver.find_element_by_xpath(scrollXpath)
            swipeIconUp(scrollView, driver, 1, 500)
        except:
            pass
        driver.back()
        sleep(0.5)
        print("""长按操作""")
        action1 = TouchAction(self.driver)
        el = self.driver.find_element_by_id("cn.yunovo.car.radio:id/tv_favor_value")
        action1.long_press(el).wait(500).perform()
        sleep(3)
        print("""向左滑动""")
        scrollXpath = '//*[@resource-id="cn.yunovo.car.radio:id/collectionContainer"]'
        scrollView = driver.find_element_by_xpath(scrollXpath)
        swipeIconLeft(scrollView,driver,1,500)
        driver.back()


if __name__ == "__main__":
    unittest.main()