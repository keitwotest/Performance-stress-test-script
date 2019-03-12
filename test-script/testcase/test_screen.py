#coding:UTF-8
"""
--------------------------------------
   File Name：  test_calculator2
   Description :
   Author :    admin
   Date：     2018/9/13
   E-mail: 3227456102@qq.com
   adb_activity_package：adb shell dumpsys window w |findstr \/ |findstr name=
   description:在Launcher页面执行熄屏亮屏压测100次
--------------------------------------
"""
__author__ = 'admin'

import unittest,os

from time import sleep
from appium import webdriver
from common.startappium import appium_start
from common.screenshot import screenshot

class screen(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        config = appium_start()
        config['appPackage'] = 'cn.yunovo.car.launcher'  # 测试app包名
        config['appActivity'] = 'cn.yunovo.car.launcher.LauncherActivity'  # 测试appActivity
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', config)  # 启动app
        print("--Start--")

    @classmethod
    def tearDownClass(cls):
        #cls.driver.quit()
        pass
        print("--End--")


    def test_screen(self):
        u"""熄屏亮屏压测"""
        driver = self.driver
        sleep(2)
        count = 1
        while (count < 50):
            print("熄屏操作")
            os.popen("adb shell input keyevent 26")
            sleep(2)
            print("亮屏操作")
            os.popen("adb shell input keyevent 26")
            screenshot(driver)
            sleep(3)
            count = count+1


if __name__ == "__main__":
    unittest.main()