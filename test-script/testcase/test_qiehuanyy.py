#coding:UTF-8
"""
--------------------------------------
   File Name：  test_calculator2
   Description :
   Author :    admin
   Date：     2018/9/13
   E-mail: 3227456102@qq.com
   adb_activity_package：adb shell dumpsys window w |findstr \/ |findstr name=
   description:在酷我音乐、高德导航、考拉电台、蓝牙电话、设置、语音助手页面中做切换操作
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
        config['appPackage'] = 'com.autonavi.amapauto'  # 测试app包名
        config['appActivity'] = 'com.autonavi.amapauto.MainMapActivity'  # 测试appActivity
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', config)  # 启动app
        print("--Start--")
        sleep(10)

    def test_kw_kl_st(self):
        print("打开酷我音乐")
        driver = self.driver
        count = 1
        while (count < 100):
            print("切换次数为", count)
            try:
                os.popen("adb shell am start -n cn.kuwo.kwmusiccar/cn.kuwo.kwmusiccar.WelcomeActivity")   # 打开酷我
                #os.popen("adb shell input keyevent 3")  #切换至后台
                sleep(4)
                os.popen("adb shell am start -n com.edog.car/com.kaolafm.auto.home.MainActivity")    # 打开考拉电台
                sleep(1)
                os.popen("adb shell am start -n cn.yunovo.car.settings/cn.yunovo.car.settings.SettingsListActivity")   # 打开设置
                sleep(1)
                os.popen("adb shell am start -n cn.yunovo.nxos.bt/cn.yunovo.nxos.bt.activitys.BluetoothActivity")  # 打开蓝牙电话
                sleep(1)
                os.popen("adb shell am start -n com.aispeech.aios/.MainActivity")   #打开语音助手
                sleep(1)
                driver.back()
                sleep(2)
                count = count + 1
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
