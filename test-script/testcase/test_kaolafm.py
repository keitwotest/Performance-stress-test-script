#coding:UTF-8
"""
--------------------------------------
   File Name：  test_kaolaFM
   Description :
   Author :    admin
   Date：     2018/9/13
   E-mail: 3227456102@qq.com
   adb_activity_package：adb shell dumpsys window w |findstr \/ |findstr name=
   description:考拉音乐UI自动化测试脚本
--------------------------------------
"""
__author__ = 'admin'

import unittest,os
from common.startappium import appium_start

from time import sleep
from appium import webdriver
from common.swipeIconMethod import *
from common.screenshot import screenshot

class kaolafm(unittest.TestCase):
    u"""卡拉音乐UI自动化测试"""
    @classmethod
    def setUpClass(cls):
        config = appium_start()
        config['appPackage'] = 'com.edog.car'  # 测试app包名
        config['appActivity'] = 'com.kaolafm.auto.home.MainActivity'  # 测试appActivity
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', config)  # 启动app
        print("考拉FM--Start")

    def test_1_sousuo(self):
        u"""搜索功能"""
        driver = self.driver
        sleep(2)
        try:
            driver.find_element_by_id("com.edog.car:id/player_play_pause").click()  #暂停
            sleep(0.5)
            driver.find_element_by_id("com.edog.car:id/navigation_search_radioButton").click()  #点击搜索
            sleep(0.5)
            driver.find_element_by_id("com.edog.car:id/search_editText").send_keys("放生")
            sleep(0.5)
            driver.find_element_by_id("com.edog.car:id/search_action_text_View").click()  #搜索
            sleep(0.5)
            driver.find_element_by_id("com.edog.car:id/search_result_item_layout").click()  #点击第一个
            sleep(0.5)
            driver.find_element_by_id("com.edog.car:id/player_prev").click()  #上一曲
            driver.find_element_by_id("com.edog.car:id/player_next").click()  #下一曲
            driver.find_element_by_id("com.edog.car:id/player_play_pause").click()
            driver.find_element_by_id("com.edog.car:id/player_play_pause").click()
            # driver.find_element_by_id("com.edog.car:id/player_recommended_img").click()  #好听推荐
            # sleep(2)
            os.popen("adb shell input keyevent 3")  #按home键退至后台播放
        except Exception as e:
            screenshot(driver)

    # def test_2_diantai(self):
    #     print("""电台广播""")
    #     driver = self.driver
    #     sleep(0.5)
    #     driver.find_element_by_id("com.edog.car:id/navigation_new_radioButton").click()
    #     sleep(1)
    #     """"向左滑动"""
    #     scrollXpath = '//*[@resource-id="com.edog.car:id/common_view_pager"]'
    #     scrollView = driver.find_element_by_xpath(scrollXpath)
    #     swipeIconLeft(scrollView, driver, 1, 500)
    #     sleep(0.5)
    #     """"向右滑动"""
    #     scrollXpath = '//*[@resource-id="com.edog.car:id/common_view_pager"]'
    #     scrollView = driver.find_element_by_xpath(scrollXpath)
    #     swipeIconRight(scrollView, driver, 1, 500)
    #     driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "搞笑频道")]').click()
    #     sleep(1)
    #     driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "在线广播")]').click()
    #     sleep(0.5)
    #     print("""在线广播""")
    #     """"左侧菜单向上滑动"""
    #     scrollXpath = '//*[@resource-id="com.edog.car:id/left_listView"]'
    #     scrollView = driver.find_element_by_xpath(scrollXpath)
    #     swipeIconUp(scrollView, driver, 2, 200)
    #     """"左侧菜单向下滑动"""
    #     scrollXpath = '//*[@resource-id="com.edog.car:id/left_listView"]'
    #     scrollView = driver.find_element_by_xpath(scrollXpath)
    #     swipeIconDown(scrollView, driver, 2, 200)
    #     driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "网络台")]').click()
    #     """"右边菜单向上滑动"""
    #     scrollXpath = '//*[@resource-id="com.edog.car:id/right_viewPager"]'
    #     scrollView = driver.find_element_by_xpath(scrollXpath)
    #     swipeIconUp(scrollView, driver, 2, 200)
    #     """"右侧菜单向下滑动"""
    #     scrollXpath = '//*[@resource-id="com.edog.car:id/right_viewPager"]'
    #     scrollView = driver.find_element_by_xpath(scrollXpath)
    #     swipeIconDown(scrollView, driver, 2, 200)
    #     driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "态度电台")]').click()
    #     driver.find_element_by_id("com.edog.car:id/navigation_player_radioButton").click()
    #
    # def test_3_podcast(self):
    #     print("""精选节目""")
    #     driver = self.driver
    #     sleep(0.5)
    #     driver.find_element_by_id("com.edog.car:id/navigation_podcast_radioButton").click()
    #     sleep(0.5)
    #     """顶部菜单向左滑动操作"""
    #     scrollXpath = '//*[@resource-id="com.edog.car:id/common_category_tab_page_indicator"]'
    #     scrollView = driver.find_element_by_xpath(scrollXpath)
    #     swipeIconLeft(scrollView, driver, 2, 50)
    #     """顶部菜单向右滑动操作"""
    #     scrollXpath = '//*[@resource-id="com.edog.car:id/common_category_tab_page_indicator"]'
    #     scrollView = driver.find_element_by_xpath(scrollXpath)
    #     swipeIconRight(scrollView, driver, 2, 50)
    #     driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "音乐")]').click()
    #     sleep(0.5)
    #     driver.find_element_by_id("com.edog.car:id/btn_choose").click()  #点击全部
    #     sleep(2)
    #     driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "动感")]').click()
    #     sleep(1)
    #     """底部菜单向左滑动操作"""
    #     # scrollXpath = '//*[@resource-id="com.edog.car:id/common_view_pager"]'
    #     scrollXpath = '//*[@resource-id="com.edog.car:id/layout_program_library_loading_view"]'
    #     scrollView = driver.find_element_by_xpath(scrollXpath)
    #     swipeIconLeft(scrollView, driver, 1, 500)
    #     sleep(1)
    #     driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "开车必备醒脑嗨曲")]').click()
    #     sleep(0.5)
    #     driver.find_element_by_id("com.edog.car:id/layout_collect").click()  #收藏
    #     sleep(0.5)
    #     driver.find_element_by_id("com.edog.car:id/title_right_asc_textView").click()  #正序
    #     driver.find_element_by_id("com.edog.car:id/title_right_asc_textView").click()  #倒序
    #     """右侧菜单向下滑动操作"""
    #     scrollXpath = '//*[@resource-id="com.edog.car:id/album_detail_refresh_lv"]'
    #     scrollView = driver.find_element_by_xpath(scrollXpath)
    #     swipeIconDown(scrollView, driver, 1, 50)
    #     """右侧菜单向上滑动操作"""
    #     scrollXpath = '//*[@resource-id="com.edog.car:id/album_detail_refresh_lv"]'
    #     scrollView = driver.find_element_by_xpath(scrollXpath)
    #     swipeIconUp(scrollView, driver, 1, 50)
    #     # # driver.find_element_by_xpath("//android.widget.TextView[@text='2期 : Save Me From Myself']").click()
    #     driver.find_element_by_id("com.edog.car:id/navigation_player_radioButton").click()
    #     driver.find_element_by_id("com.edog.car:id/navigation_new_radioButton").click()
    #     driver.find_element_by_id("com.edog.car:id/navigation_new_radioButton").click()
    #     #driver.back()
    #
    # def test_4_user(self):
    #     print("""用户中心""")
    #     driver = self.driver
    #     sleep(0.5)
    #     driver.find_element_by_id("com.edog.car:id/navigation_user_center_radioButton").click()   #user
    #     sleep(0.5)
    #     #判断是否有收藏节目
    #     try:
    #         driver.find_element_by_id("com.edog.car:id/item_base_root")
    #         a = True
    #     except:
    #         a =False
    #     if a == True:
    #         print("元素存在")
    #         driver.find_element_by_id("com.edog.car:id/item_base_root").click()
    #         driver.find_element_by_id("com.edog.car:id/layout_collect").click()  # 取消收藏
    #         driver.back()
    #     else:
    #         print("元素不存在")
    #         pass
    #     driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "下载")]').click()
    #     driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "收听历史")]').click()
    #     #判断清空按钮是否存在
    #     try:
    #         driver.find_element_by_id("com.edog.car:id/history_clear_tv")
    #         a = True
    #     except:
    #         a =False
    #     if a == True:
    #         print("元素存在")
    #         driver.find_element_by_id("com.edog.car:id/history_clear_tv").click()
    #         driver.find_element_by_id("com.edog.car:id/dialog_remove_btn_cancel").click()
    #         driver.find_element_by_id("com.edog.car:id/history_clear_tv").click()  # 清空按钮
    #         driver.find_element_by_id("com.edog.car:id/dialog_remove_btn_sure").click()
    #     else:
    #         print("元素不存在")
    #         pass
    #     driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "语音指导")]').click()
    #     """"菜单向上滑动"""
    #     scrollXpath = '//*[@resource-id="com.edog.car:id/vRecyclerView"]'
    #     scrollView = driver.find_element_by_xpath(scrollXpath)
    #     swipeIconUp(scrollView, driver, 1, 50)
    #     """"菜单向下滑动"""
    #     scrollXpath = '//*[@resource-id="com.edog.car:id/vRecyclerView"]'
    #     scrollView = driver.find_element_by_xpath(scrollXpath)
    #     swipeIconDown(scrollView, driver, 1, 50)
    #     driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "设置")]').click()
    #     driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "点击登录")]').click()
    #     sleep(2)
    #     driver.find_element_by_id("com.edog.car:id/about_us_image_close_imageButton").click()   #点击x按钮
    #     driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "播放音质")]').click()
    #     driver.find_element_by_id("com.edog.car:id/tone_high_textview").click()
    #     sleep(0.5)
    #     driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "清除缓存")]').click()
    #     sleep(0.5)
    #     driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "检测更新")]').click()
    #     sleep(0.5)
    #     driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "下载手机端")]').click()
    #     sleep(1)
    #     driver.find_element_by_id("com.edog.car:id/about_us_image_close_imageButton").click()  #点击x按钮
    #     driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "关于我们")]').click()
    #     """"菜单向上滑动"""
    #     scrollXpath = '//*[@class="android.widget.ScrollView"]'
    #     scrollView = driver.find_element_by_xpath(scrollXpath)
    #     swipeIconUp(scrollView, driver, 1, 50)
    #     driver.back()
    #     driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "意见反馈")]').click()
    #     driver.find_element_by_id("com.edog.car:id/about_us_image_close_imageButton").click()  # 点击x按钮
    #     driver.back()

    @classmethod
    def tearDownClass(cls):
        sleep(3)
        #cls.driver.quit()
        pass
        print("考拉FM--End")


if __name__ == "__main__":
    unittest.main()