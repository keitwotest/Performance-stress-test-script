#coding:UTF-8
"""
--------------------------------------
   File Name：  test_music
   Description :
   Author :    admin
   Date：     2018/9/14
   E-mail: 3227456102@qq.com
   adb_activity_package：adb shell dumpsys window w |findstr \/ |findstr name=
   description: 本地音乐UI自动化测试脚本
--------------------------------------
"""
import unittest

from SeleniumLibrary.keywords import element
from appium import webdriver
from common.swipeIconMethod import *

from common.swipeIconMethod import *
from common.startappium import appium_start

class music(unittest.TestCase):
    u"""本地音乐UI自动化测试脚本"""
    @classmethod
    def setUpClass(cls):
        config = appium_start()
        config['appPackage'] = 'cn.yunovo.car.music'  # 测试app包名
        config['appActivity'] = 'cn.yunovo.car.music.activity.MusicActivity'  # 测试appActivity
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', config)  # 启动app
        print("音乐--Start")



    def test_yinye(self):
        u"""音乐面板功能"""
        driver = self.driver
        sleep(2)
        t = 0
        while t < 4:
            driver.find_element_by_id("cn.yunovo.car.music:id/btn_mode").click()  #切换模式
            t = t + 1
        sleep(2)
        print("""存在音乐文件""")
        """向左滑动操作"""
        scrollXpath = '//*[@resource-id="cn.yunovo.car.music:id/container"]'
        scrollView = driver.find_element_by_xpath(scrollXpath)
        swipeIconLeft(scrollView, driver, 1, 500)
        sleep(2)
        driver.find_element_by_id("cn.yunovo.car.music:id/btn_open_list").click()
        sleep(1)
        try:
            """向下滑动操作"""
            scrollXpath = '//*[@resource-id="cn.yunovo.car.music:id/music_list"]'
            scrollView = driver.find_element_by_xpath(scrollXpath)
            swipeIconDown(scrollView, driver, 1, 500)
        except:
            pass
        driver.back()
        driver.back()
        sleep(1)
        driver.find_element_by_id("cn.yunovo.car.music:id/btn_cancel").click()
        sleep(1)
        driver.back()
        sleep(0.5)
        driver.find_element_by_id("cn.yunovo.car.music:id/btn_nin").click()
        sleep(1)
        driver.launch_app()  #启动应用
        sleep(1)
        driver.back()
        sleep(0.5)
        driver.find_element_by_id("cn.yunovo.car.music:id/btn_exit").click()  #退出音乐
        driver.launch_app()  # 启动应用

    @classmethod
    def tearDownClass(cls):
        sleep(3)
        #cls.driver.quit()
        pass
        print("---End---")


if __name__ == "__main__":
    unittest.main()