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


import unittest,os,sys,time
sys.path.append('..')
from common.startappium import *
from time import sleep
from common.screenshot import screenshot


class settings(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        config = appium_start()
        config['appPackage'] = 'cn.yunovo.car.settings'  # 测试app包名
        config['appActivity'] = 'cn.yunovo.car.settings.SettingsListActivity'  # 测试appActivity
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', config)  # 启动app
        print("--Start--")

    def test_wifi(self):
        print("wifi")
        driver = self.driver
        for i in range(10):
            count = i
            try:
                driver.find_element_by_id("cn.yunovo.car.settings:id/wlan").click()
                sleep(3)
                wifiSwitch = driver.find_element_by_id("cn.yunovo.car.settings:id/thumb")
                wifiSwitch.click()
                wifiSwitch.click()
                #sleep(1)
                count = count + 1
                print("开关压力测试次数为：",count)
            except Exception as e:
                screenshot(driver)
                continue


    @classmethod
    def tearDownClass(cls):
        sleep(5)
        #cls.driver.quit()
        pass
        print("End")

if __name__ == "__main__":
    unittest.main()
