#coding:UTF-8
"""
--------------------------------------
   File Name：  test_movie
   Description :
   Author :    admin
   Date：     2018/9/14
   E-mail: 3227456102@qq.com
   adb_activity_package：adb shell dumpsys window w |findstr \/ |findstr name=
   description:
--------------------------------------
"""
import unittest

from appium import webdriver
from common.swipeIconMethod import *

class movie(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # cls.driver = appium_start()
        # sleep(10)
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 设备系统
        desired_caps['platformVersion'] = '5.1'  # 设备系统版本
        desired_caps['deviceName'] = '106D111805004868'  # 设备名称
        desired_caps['appPackage'] = 'cn.yunovo.car.movie'  # 测试app包名
        desired_caps['appActivity'] = 'cn.yunovo.car.movie.ThumbActivity'  # 测试appActivity
        desired_caps['noReset'] = 'true'
        desired_caps['unicodeKeyboard'] = 'True'  # 使用unicodeKeyboard的编码方式来发送字符串
        desired_caps['resetKeyboard'] = 'true'  # 将键盘给隐藏
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 启动app
        print("视频--Start")

    def test_shiping(self):
        u"""视频面板功能"""
        driver = self.driver
        sleep(2)
        try:
            driver.find_elements_by_id("cn.yunovo.car.movie:id/thumb_lay")
            scrollXpath = '//*[@resource-id="cn.yunovo.car.movie:id/thumbnailsContainer"]'
            scrollView = driver.find_element_by_xpath(scrollXpath)
            swipeIconLeft(scrollView, driver, 1, 500)
            sleep(1)
            driver.find_element_by_class_name("android.widget.LinearLayout").click()
            sleep(1)
            #driver.find_element_by_id("android:id/button1").click()
            driver.back()
        except:
            #a == False
            print("元素不存在")


    @classmethod
    def tearDownClass(cls):
        sleep(3)
        #cls.driver.quit()
        pass
        print("End")

if __name__ == "__main__":
    unittest.main()