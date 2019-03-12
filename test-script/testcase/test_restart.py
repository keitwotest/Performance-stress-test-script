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
    U"""重启压力测试100次"""
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


    def test_restart(self):
        print("""重启压测脚本""")
        driver = self.driver
        sleep(2)
        count = 1
        while (count < 100):
            print("重启次数为",count)
            screenshot(driver)
            os.popen("adb reboot")
            sleep(30)
            screenshot(driver)
            count = count+1


if __name__ == "__main__":
    unittest.main()