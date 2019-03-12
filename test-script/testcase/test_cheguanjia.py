#coding:UTF-8
"""
--------------------------------------
   File Name：  test_cheguanjia
   Description :
   Author :    admin
   Date：     2018/9/10
   E-mail: 3227456102@qq.com
   adb_activity_package：adb shell dumpsys window w |findstr \/ |findstr name=
--------------------------------------
"""
__author__ = 'admin'

import datetime,time
import unittest

from time import sleep
from appium import webdriver
from common.screenshot import screenshot
from common.keyevent import keyevent


class cheguanjia(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # cls.driver = appium_start()
        # sleep(10)
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 设备系统
        desired_caps['platformVersion'] = '5.1'  # 设备系统版本
        desired_caps['deviceName'] = '106D111805004868'  # 设备名称
        desired_caps['appPackage'] = 'cn.yunovo.car.manager'  # 测试app包名
        desired_caps['appActivity'] = 'cn.yunovo.car.manager.MainActivity'  # 测试appActivity
        desired_caps['noReset'] = 'true'
        desired_caps['unicodeKeyboard'] = 'True'  # 使用unicodeKeyboard的编码方式来发送字符串
        desired_caps['resetKeyboard'] = 'true'  # 将键盘给隐藏
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 启动app
        print("车管家--Start")

    @classmethod
    def tearDownClass(cls):
        sleep(5)
        cls.driver.quit()
        print("End")

    def test_qinglijiasu(self):
        print("""清理加速""")
        driver = self.driver
        driver.find_element_by_id("cn.yunovo.car.manager:id/boost").click()
        sleep(1)
        driver.find_element_by_id("cn.yunovo.car.manager:id/btn_boosting").click()  #扫描
        sleep(20)
        driver.find_element_by_id("cn.yunovo.car.manager:id/btn_boosting").click()  #清理
        sleep(2)
        driver.back()
        #driver.keyevent(keyevent.KEYCODE_BACK)  # 执行返回操作


    def test_shenduqingli(self):
        print("""深度清理""")
        driver = self.driver
        driver.find_element_by_id("cn.yunovo.car.manager:id/advance_clean").click()
        sleep(2)
        driver.find_element_by_id("cn.yunovo.car.manager:id/space_root").click()
        # sleep(1)
        # t = ['视频文件','图片文件','音乐文件','应用数据','压缩包','安装包','地图数据','其他']
        sleep(2)
        pass_1 = False
        print("""视频文件""")
        try:
            driver.find_element_by_id("cn.yunovo.car.manager:id/video_file").click()
            sleep(1)
            driver = self.select_all()
        except:
            pass_1 = True

        sleep(2)
        print("""图片文件""")
        try:
            driver.find_element_by_id("cn.yunovo.car.manager:id/image_file").click()
            sleep(1)
            driver = self.select_all()
        except:
            pass_1 = True

        sleep(2)
        print("""音乐文件""")
        try:
            driver.find_element_by_id("cn.yunovo.car.manager:id/audio_file").click()
            sleep(1)
            driver = self.select_all()
        except:
            pass_1 = True

        sleep(2)
        print("""应用数据""")
        try:
            driver.find_element_by_id("cn.yunovo.car.manager:id/appData_file").click()
            sleep(1)
            driver = self.select_all()
        except:
            pass_1 = True

        sleep(2)
        print("""压缩包""")
        try:
            driver.find_element_by_id("cn.yunovo.car.manager:id/compress_file").click()
            sleep(1)
            driver = self.select_all()
        except:
            pass_1 = True

        sleep(2)
        print("""安装包""")
        try:
            driver.find_element_by_id("cn.yunovo.car.manager:id/install_pkg").click()
            sleep(1)
            driver = self.select_all()
        except:
            pass_1 = True

        sleep(2)
        print("""地图数据""")
        try:
            driver.find_element_by_id("cn.yunovo.car.manager:id/map_list").click()
            sleep(1)
            driver = self.select_all()
        except:
            pass_1 = True

        sleep(2)
        print("""其他""")
        try:
            driver.find_element_by_id("cn.yunovo.car.manager:id/other_files").click()
            sleep(1)
            driver = self.select_all()
        except:
            pass_1 = True

    def select_all(self):
        driver = self.driver
        driver.find_element_by_id("cn.yunovo.car.manager:id/detail_select_all").click()  # 全选
        sleep(2)
        driver.find_element_by_id("cn.yunovo.car.manager:id/detail_delete").click()  # 删除
        driver.back()

    @classmethod
    def tearDownClass(cls):
        sleep(5)
        cls.driver.quit()
        print("End")


if __name__ == "__main__":
    unittest.main()