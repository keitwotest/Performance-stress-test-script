#coding:UTF-8
"""
--------------------------------------
   *File Name：  test_setting_btcall.py
   *Description :
   *Author :    zhong
   *Date：     2019/2/27
   *E-mail: 3227456102@qq.com
   adb_activity_package：adb shell dumpsys window w |findstr \/ |findstr name=
   description: WIFI和蓝牙电话开关压力测试脚本
--------------------------------------
"""
import unittest
from time import sleep
from appium import webdriver
from common.startappium import appium_start
from common.screenshot import screenshot
import random

class btPhone(unittest.TestCase):
    u"""WIFI和蓝牙电话开关压力测试脚本"""
    @classmethod
    def setUpClass(cls):
        config = appium_start()
        config['appPackage'] = 'cn.yunovo.nxos.bt'  # 测试app包名
        config['appActivity'] = 'cn.yunovo.nxos.bt.activitys.BluetoothActivity'  # 测试appActivity
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', config)  # 启动app
        print("--Start--")

    @classmethod
    def tearDownClass(cls):
        sleep(5)
        #cls.driver.quit()
        pass
        print("btPhone End")

    def test_pair(self):
        u"""蓝牙电话：蓝牙配对"""
        driver = self.driver
        sleep(3)
        driver.find_element_by_id('cn.yunovo.nxos.bt:id/btn_pairs').click()
        sleep(1)
        for i in range(10):
            count = i
            try:
                pairSwitch = driver.find_element_by_id("cn.yunovo.nxos.bt:id/pair_bt_switch")
                for i in range(2):
                    pairSwitch.click()
                    #sleep(1)
                    count = count + 1
                    print("开关压力测试次数为：",count)
            except Exception as e:
                screenshot(driver)
                continue


if __name__ == "__main__":
    unittest.main()