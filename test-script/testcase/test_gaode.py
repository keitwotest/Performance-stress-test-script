#coding:UTF-8
"""
--------------------------------------
   File Name：  test_gaode
   Description :
   Author :    admin
   Date：     2018/9/8
   E-mail: 3227456102@qq.com
   adb_activity_package：adb shell dumpsys window w |findstr \/ |findstr name=
   description:参数化执行模拟导航操作
--------------------------------------
"""
__author__ = 'admin'


from common.startappium import appium_start
from time import sleep
from appium import webdriver
from common.screenshot import screenshot
import datetime,time
import unittest,os

class gaode(unittest.TestCase):
    u"""高德地图UI自动化测试脚本"""
    @classmethod
    def setUpClass(cls):
        config = appium_start()
        config['appPackage'] = 'com.autonavi.amapauto'  # 测试app包名
        config['appActivity'] = 'com.autonavi.amapauto.MainMapActivity'  # 测试appActivity
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', config)  # 启动app
        print("导航--Start")

    def test_kaiqdaohang(self):
        """开启导航模式"""
        count = 1
        while (count < 3):
            driver = self.driver
            print("测试次数为：", count)
            source = open("C:\\Users\\admin\\Desktop\\appautoTest\\common\\dizhicanshuhua.txt", "r")
            values = source.readlines()
            source.close()
            try:
                for dizhi in values:
                    pass_1 = False
                    print("""模拟导航""")
                    try:
                        driver.find_element_by_class_name(
                            "android.widget.TextView[@text='高德地图使用提示']").click()  # 判断是否第一次使用地图时的使用提示界面
                        sleep(3)
                        driver.find_element_by_class_name("android.widget.TextView[@text='不在提示']").click()  # 勾选不在提示
                        sleep(3)
                        driver.find_element_by_class_name("android.widget.TextView[@text='同意']").click()  # 点击同意
                    except:
                        pass_1 = True
                    sleep(5)
                    driver.find_element_by_id("com.autonavi.amapauto:id/siv_arrow").click()  # 点击三角导航图标
                    # sleep(1)
                    # driver.find_element_by_id("com.autonavi.amapauto:id/cl_home").click()  #回家
                    # sleep(1)
                    # driver.back()
                    # sleep(1)
                    # driver.find_element_by_id("com.autonavi.amapauto:id/cl_company").click()  #去公司
                    # sleep(1)
                    # driver.back()
                    # sleep(1)
                    # driver.find_element_by_id("com.autonavi.amapauto:id/cl_collected").click()  #收藏点
                    # sleep(1)
                    # driver.back()
                    # sleep(1)
                    # driver.find_element_by_id("com.autonavi.amapauto:id/cl_bathroom").click()  #卫生间
                    # sleep(5)
                    # driver.back()
                    # sleep(1)
                    # driver.find_element_by_id("com.autonavi.amapauto:id/cl_gas_station").click()  #加油站
                    # sleep(5)
                    # driver.back()
                    # sleep(1)
                    # driver.find_element_by_id("com.autonavi.amapauto:id/cl_parking").click()  #停车场
                    # sleep(5)
                    # driver.back()
                    # sleep(1)
                    # driver.find_element_by_id("com.autonavi.amapauto:id/cl_cleancar").click()  #洗车
                    # sleep(5)
                    # driver.back()
                    # sleep(1)
                    # driver.find_element_by_id("com.autonavi.amapauto:id/cl_maintenance").click()   #汽车维修
                    # sleep(5)
                    # driver.back()
                    # sleep(1)
                    # driver.find_element_by_id("com.autonavi.amapauto:id/cl_more").click()  #更多
                    # sleep(0.5)
                    # driver.find_element_by_id("com.autonavi.amapauto:id/cl_auto_search_more_group_view").click()
                    # sleep(2)
                    # print("""向上滑动""")
                    # scrollXpath = '//*[@resource-id="com.autonavi.amapauto:id/elv_search_category_listview"]'
                    # scrollView = driver.find_element_by_xpath(scrollXpath)
                    # scrollViewSize = scrollView.size
                    # scrollViewSize1 = scrollView.location
                    # scrollViewSize2 = scrollView.rect
                    # print(scrollViewSize)
                    # print(scrollViewSize1)
                    # print(scrollViewSize2)
                    # x1 = scrollViewSize['width'] * 0.5
                    # y1 = scrollViewSize['height'] * 0.75
                    # y2 = scrollViewSize['height'] * 0.25
                    #
                    # print(x1, y1, y2)
                    # for i in range(1):
                    #     driver.swipe(x1, y1, x1, y2, 1000)
                    # sleep(2)
                    # driver.back()
                    sleep(3)
                    driver.find_element_by_id("com.autonavi.amapauto:id/stv_text_title_hint").click()
                    sleep(2)
                    driver.find_element_by_id("com.autonavi.amapauto:id/set_search_around").send_keys(dizhi)
                    sleep(3)
                    driver.find_element_by_id(
                        "com.autonavi.amapauto:id/cl_auto_search_history_listview_item").click()  # 选择目的地
                    sleep(4)
                    driver.find_element_by_id("com.autonavi.amapauto:id/cl_search_result_btn").click()  # 点击去这里按钮
                    sleep(8)
                    driver.find_element_by_id("com.autonavi.amapauto:id/stv_auto_panel_content_title_des").click()
                    sleep(2)
                    driver.find_element_by_id("com.autonavi.amapauto:id/stv_text_startnavi").click()  # 模拟导航
                    sleep(2)
                    driver.back()
                    sleep(3)
                    driver.find_element_by_id("com.autonavi.amapauto:id/stv_text_go").click()  # 点击开始导航
                    sleep(3)
                    driver.back()  # 返回键
                    sleep(1)
                    driver.find_element_by_id("com.autonavi.amapauto:id/cbm_left_btn_bg").click()  # 点击确定按钮
                    count = count + 1
            except Exception as e:
                screenshot(driver)
                continue

    # def monidaohang(self):
    #     print("""导航配置""")
    #     driver = self.driver
    #     driver.find_element_by_id("com.autonavi.amapauto:id/cl_more").click()
    #     sleep(1)
    #     driver.find_element_by_id("com.autonavi.amapauto:id/cl_head").click()  #点击头像登录
    #     sleep(2)
    #     driver.find_element_by_id("com.autonavi.amapauto:id/cbm_signin").click()  #点击验证码登录
    #     sleep(2)
    #     driver.find_element_by_id("com.autonavi.amapauto:id/sftv_back").click()
    #     sleep(1)
    #     driver.find_element_by_id("com.autonavi.amapauto:id/cbm_register").click()  #点击注册
    #     sleep(2)
    #     driver.find_element_by_id("com.autonavi.amapauto:id/sftv_back").click()
    #     sleep(1)
    #     driver.find_element_by_id("com.autonavi.amapauto:id/sftv_back").click()
    #     sleep(1)
    #     driver.find_element_by_id("com.autonavi.amapauto:id/siv_rectanglecar").click()  #我的爱车
    #     sleep(1)
    #     driver.back()
    #     sleep(1)
    #     driver.find_element_by_id("com.autonavi.amapauto:id/siv_rectanglemeeg").click()  #我的消息
    #     sleep(2)
    #     driver.find_element_by_id("com.autonavi.amapauto:id/cnbi_message2").click()  #广播消息
    #     driver.back()
    #     sleep(1)
    #     print("""常用配置""")
    #     driver.find_element_by_id("com.autonavi.amapauto:id/ctb_collection").click()  #收藏夹
    #     sleep(1)
    #     driver.back()
    #     sleep(2)
    #     driver.find_element_by_id("com.autonavi.amapauto:id/ctb_data").click() # 离线数据
    #     sleep(1)
    #     driver.back()
    #     sleep(2)
    #     driver.find_element_by_id("com.autonavi.amapauto:id/ctb_set").click()  #设置
    #     sleep(1)
    #     driver.find_element_by_id("com.autonavi.amapauto:id/siv_box_bg_playvoice_select").click()  #播报
    #     sleep(1)
    #     driver.find_element_by_id("com.autonavi.amapauto:id/siv_box_bg_map_select").click()  #地图
    #     sleep(1)
    #     driver.find_element_by_id("com.autonavi.amapauto:id/siv_box_bg_other_select").click()  #其他
    #     sleep(1)
    #     driver.back()
    #     sleep(2)
    #     print("""更多配置""")
    #     driver.find_element_by_id("com.autonavi.amapauto:id/ctb_interconnection").click()  #互联
    #     sleep(1)
    #     driver.back()
    #     sleep(1)
    #     driver.find_element_by_id("com.autonavi.amapauto:id/ctb_myjourney").click() #我的行程
    #     sleep(1)
    #     driver.back()
    #     driver.find_element_by_id("com.autonavi.amapauto:id/ctb_toolbox").click()  #组队出行
    #     sleep(1)
    #     driver.back()
    #     driver.back()
    #     print("""地图界面""")
    #     sleep(1)
    #     driver.find_element_by_id("com.autonavi.amapauto:id/siv_bg").click() #查看定位和时间
    #     sleep(2)
    #     driver.find_element_by_id("com.autonavi.amapauto:id/siv_theme_bg1").click()  #GPS定位
    #     sleep(1)
    #     driver.back()
    #     sleep(1)
    #     driver.find_element_by_id("com.autonavi.amapauto:id/cl_item_phone_connect").click()  #手机未连接
    #     sleep(1)
    #     driver.back()
    #     driver.back()
    #     sleep(1)
    #     driver.find_element_by_id("com.autonavi.amapauto:id/crc_road_codition").click()   #关闭路况
    #     sleep(1)
    #     driver.find_element_by_id("com.autonavi.amapauto:id/crc_road_codition").click()  #开启路况
    #     sleep(1)
    #     driver.find_element_by_id("com.autonavi.amapauto:id/cv_2d_carup").click()  #3D车头朝上模式
    #     sleep(1)
    #     driver.find_element_by_id("com.autonavi.amapauto:id/cv_2d_carup").click()  #2D正北朝上
    #     sleep(1)
    #     driver.find_element_by_id("com.autonavi.amapauto:id/cv_2d_carup").click()  #2D车头朝上
    #     sleep(1)
    #     driver.find_element_by_id("com.autonavi.amapauto:id/sftv_enlarge").click()  #+  放大地图
    #     sleep(0.5)
    #     driver.find_element_by_id("com.autonavi.amapauto:id/sftv_enlarge").click()  # +  放大地图
    #     sleep(1)
    #     driver.find_element_by_id("com.autonavi.amapauto:id/sftv_narrow").click()  #-  缩小地图
    #     sleep(0.5)
    #     driver.find_element_by_id("com.autonavi.amapauto:id/sftv_narrow").click()  # -  缩小地图
    #     sleep(1)
    #     driver = self.closegaode()

    # def closegaode(self):
    #     """退出\关闭导航"""
    #     driver = self.driver
    #     sleep(3)
    #     i = 0
    #     while i < 3:
    #         driver.back()  # 模拟手机按返回键
    #         print(u"退出导航到设备主界面")
    #         i += 1

    @classmethod
    def tearDownClass(cls):
        sleep(5)
        #cls.driver.quit()
        pass
        print("导航结束")

if __name__ == "__main__":
    unittest.main()