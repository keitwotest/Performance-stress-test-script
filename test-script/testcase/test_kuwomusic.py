#coding:UTF-8
"""
--------------------------------------
   File Name：  test_calculator2
   Description :
   Author :    admin
   Date：     2018/9/13
   E-mail: 3227456102@qq.com
   adb_activity_package：adb shell dumpsys window w |findstr \/ |findstr name=
   description:酷我音乐UI自动化测试脚本
--------------------------------------
"""
__author__ = 'admin'


import unittest
from time import sleep
from appium import webdriver
from common.startappium import appium_start
import random
from common.swipeIconMethod import swipeIconUp, swipeIconDown, swipeIconLeft, swipeIconRight
#from common.getDriver import mdriver

class kuwoMusic(unittest.TestCase):
    u"""酷我音乐UI自动化测试"""
    @classmethod
    def setUpClass(cls):
        config = appium_start()
        config['appPackage'] = 'cn.kuwo.kwmusiccar'
        config['appActivity'] = 'cn.kuwo.kwmusiccar.WelcomeActivity'
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', config)
        print("酷我音乐：Start")

    @classmethod
    def tearDownClass(cls):
        sleep(5)
        #cls.driver.quit()
        pass
        print("酷我音乐：End")

    def test_01_lekuView(self):
        u"""乐库界面"""
        driver = self.driver
        driver.find_element_by_id("cn.kuwo.kwmusiccar:id/tv_item_music_lib").click()
        sleep(1)
        # 滑动乐库界面
        for i in range(3):
            try:
                lekuView = driver.find_element_by_id("cn.kuwo.kwmusiccar:id/rv_content")
                swipeIconLeft(lekuView, driver, 1, 500)
                swipeIconRight(lekuView, driver, 1, 500)
                sleep(1)
                # 选取其中一个类型分类进入
                songType = '//*[@resource-id="cn.kuwo.kwmusiccar:id/rv_content"]/android.widget.LinearLayout[' + str(random.randint(1, 4)) + ']'
                driver.find_element_by_xpath(songType).click()
                sleep(1)
                # 滑动歌曲界面
                contenIcon = driver.find_element_by_id("cn.kuwo.kwmusiccar:id/rv_content")
                for i in range(2):
                    swipeIconUp(contenIcon, driver, 1, 500)
                    swipeIconDown(contenIcon, driver, 1, 500)
                    sleep(1)
                try:
                    # 选取界面中歌曲播放
                    for i in range(2):
                        j = random.randint(1, 6)
                        choiceSong = '//*[@resource-id="cn.kuwo.kwmusiccar:id/rv_content"]/android.widget.RelativeLayout[' + str(j) + ']'
                        driver.find_element_by_xpath(choiceSong).click()
                        sleep(3)
                    # 选取界面中歌曲播放收藏
                    for i in range(2):
                        j = random.randint(1, 6)
                        likeSong = '//*[@resource-id="cn.kuwo.kwmusiccar:id/rv_content"]/android.widget.RelativeLayout[' \
                            + str(j) + ']/android.widget.LinearLayout[2]/android.widget.ImageView[2]'
                        driver.find_element_by_xpath(likeSong).click()
                        sleep(1)
                    driver.press_keycode(4)
                    sleep(1)
                except Exception as e:
                    print("当前歌曲类型为电台或网络不佳，无法进入选择歌曲")
                break
            except:
                driver.find_element_by_id("cn.kuwo.kwmusiccar:id/layout_state").click()
                sleep(2)

    def test_02_radioView(self):
        u"""电台界面"""
        driver = self.driver
        driver.find_element_by_id("cn.kuwo.kwmusiccar:id/tv_item_radio").click()
        sleep(1)
        for i in range(3):
            try:
                # 滑动电台界面
                videoView = driver.find_element_by_id("cn.kuwo.kwmusiccar:id/rv_content")
                swipeIconLeft(videoView, driver, 1, 500)
                swipeIconRight(videoView, driver, 1, 500)
                sleep(1)
                # 选取其中一个电台类型播放
                for i in range(2):
                    radioType = '//*[@resource-id="cn.kuwo.kwmusiccar:id/rv_content"]/android.widget.LinearLayout[' + str(
                        random.randint(1, 4)) + ']'
                    driver.find_element_by_xpath(radioType).click()
                    sleep(1)
                break
            except:
                driver.find_element_by_id("cn.kuwo.kwmusiccar:id/layout_state").click()
                sleep(2)
    def test_03_audioView(self):
        u"""有声界面"""
        driver = self.driver
        driver.find_element_by_id("cn.kuwo.kwmusiccar:id/tv_item_audio_content").click()
        sleep(1)
        for i in range(3):
            try:
                # 滑动有声界面
                audioView = driver.find_element_by_id("cn.kuwo.kwmusiccar:id/rv_content")
                swipeIconLeft(audioView, driver, 1, 500)
                swipeIconRight(audioView, driver, 1, 500)
                sleep(1)
                # 选取其中一个类型分类进入
                songType = '//*[@resource-id="cn.kuwo.kwmusiccar:id/rv_content"]/android.widget.LinearLayout[' + str(
                    random.randint(1, 4)) + ']'
                driver.find_element_by_xpath(songType).click()
                sleep(1)
                # 滑动歌曲界面
                contenIcon = driver.find_element_by_id("cn.kuwo.kwmusiccar:id/rv_content")
                for i in range(2):
                    swipeIconUp(contenIcon, driver, 1, 500)
                    swipeIconDown(contenIcon, driver, 1, 500)
                # 选取界面中歌曲播放
                for i in range(2):
                    j = random.randint(1, 6)
                    choiceSong = '//*[@resource-id="cn.kuwo.kwmusiccar:id/rv_content"]/android.widget.RelativeLayout[' + str(
                        j) + ']'
                    driver.find_element_by_xpath(choiceSong).click()
                    sleep(3)
                # 选取界面中歌曲播放收藏
                for i in range(2):
                    j = random.randint(1, 6)
                    likeSong = '//*[@resource-id="cn.kuwo.kwmusiccar:id/rv_content"]/android.widget.RelativeLayout[' \
                       + str(j) + ']/android.widget.LinearLayout[2]/android.widget.ImageView[2]'
                    driver.find_element_by_xpath(likeSong).click()
                    sleep(1)
                driver.press_keycode(4)
                sleep(1)
                break
            except:
                driver.find_element_by_id("cn.kuwo.kwmusiccar:id/layout_state").click()
                sleep(2)

    def test_04_localView(self):
        u"""本地界面"""
        driver = self.driver
        driver.find_element_by_id("cn.kuwo.kwmusiccar:id/tv_item_local").click()
        sleep(1)
        driver.find_element_by_xpath('//*[@text="本地音乐"]').click()
        sleep(1)
        driver.press_keycode(4)

    def test_05_playingMusic(self):
        u"""操作酷我音乐底部当前播放的音乐"""
        driver = self.driver
        # 进入正在播放的音乐界面
        driver.find_element_by_id("cn.kuwo.kwmusiccar:id/layout_song_cover").click()
        sleep(1)
        driver.press_keycode(4)
        sleep(1)
        # 操作正在播放的音乐
        for i in range(2):
            driver.find_element_by_id("cn.kuwo.kwmusiccar:id/iv_play_pause").click()
            sleep(2)
        for i in range(2):
            driver.find_element_by_id("cn.kuwo.kwmusiccar:id/iv_pre").click()
            sleep(2)
            driver.find_element_by_id("cn.kuwo.kwmusiccar:id/iv_next").click()
            sleep(2)
        # 音效切换
        driver.find_element_by_id("cn.kuwo.kwmusiccar:id/iv_sound_effect").click()
        sleep(1)
        for i in range(1, 4):
            driver.find_element_by_xpath('//*[@resource-id="cn.kuwo.kwmusiccar:id/rv_content"]/android.widget.LinearLayout[' + str(i) + ']').click()
            sleep(1)
        driver.press_keycode(4)
        sleep(1)
        # 播放模式
        for i in range(4):
            driver.find_element_by_id("cn.kuwo.kwmusiccar:id/iv_play_mode").click()
            sleep(1)
        # 播放列表
        driver.find_element_by_id("cn.kuwo.kwmusiccar:id/iv_play_list").click()
        sleep(1)
        driver.press_keycode(4)
        sleep(1)
        # 若退出酷我音乐界面弹出，则点击back
        try:
            if driver.find_element_by_xpath('//*[@text="退出酷我"]'):
                driver.press_keycode(4)
                sleep(1)
        except Exception as e:
            sleep(1)
        finally:
            print("播放音乐操作完成")

    def test_06_searchMusic(self):
        u"""搜索音乐"""
        driver = self.driver
        driver.find_element_by_id("cn.kuwo.kwmusiccar:id/iv_search").click()
        sleep(1)
        editText = driver.find_element_by_class_name("android.widget.EditText")
        editText.click()
        sleep(1)
        editText.send_keys("张杰")
        sleep(1)
        driver.find_element_by_id("cn.kuwo.kwmusiccar:id/iv_search").click()
        sleep(7)
        try:
            lists = ["单曲", "MV", "歌手", "专辑", "歌单"]
            for list in lists:
                driver.find_element_by_xpath('//*[@text=' + '\"' + list + '\"]').click()
                sleep(1)
        except Exception as e:
            print("未打开此歌手的歌曲")
        driver.press_keycode(4)
        sleep(1)
        driver.press_keycode(4)
        sleep(1)

    def test_07_mineView(self):
        u"""我的界面"""
        driver = self.driver
        driver.find_element_by_id("cn.kuwo.kwmusiccar:id/tv_item_mine").click()
        sleep(1)
        lists = ["最近播放", "我喜欢听", "皮肤", "音效", "下载管理"]
        for list in lists:
            driver.find_element_by_xpath('//*[@text="' + str(list) + '\"]').click()
            sleep(1)
            driver.press_keycode(4)
            sleep(1)
        # 试听音质,下载音质
        list2s = ["试听音质", "下载音质"]
        contentView = driver.find_element_by_id("cn.kuwo.kwmusiccar:id/rv_content")
        swipeIconLeft(contentView, driver, 1, 1000)
        sleep(2)
        for list in list2s:
            driver.find_element_by_xpath('//*[@text="' + str(list) + '\"]').click()
            sleep(1)
            driver.press_keycode(4)
        # 边听边存
        for i in range(5):
            try:
                for j in range(2):
                    driver.find_element_by_xpath('//*[@text="边听边存"]').click()
                    sleep(1)
                break
            except Exception as e:
                swipeIconLeft(contentView, driver, 1, 800)
                continue
        # 清除缓存
        for i in range(5):
            try:
                driver.find_element_by_xpath('//*[@text="清除缓存"]').click()
                sleep(1)
                break
            except Exception as e:
                swipeIconLeft(contentView, driver, 1, 800)
                continue
        driver.find_element_by_xpath('//*[@text="取消"]').click()
        sleep(1)
        # 检查更新
        for i in range(5):
            try:
                driver.find_element_by_xpath('//*[@text="检查更新"]').click()
                sleep(1)
                break
            except Exception as e:
                swipeIconLeft(contentView, driver, 1, 800)
                sleep(1)
                continue
        try:
            driver.find_element_by_xpath('//*[@text="确定"]').click()
            sleep(1)
        except Exception as e:
            print("网络不佳，未调出检查更新")
        # 登录
        for i in range(5):
            try:
                driver.find_element_by_xpath('//*[@text="登录"]').click()
                sleep(1)
                break
            except Exception as e:
                swipeIconLeft(contentView, driver, 1, 800)
                sleep(1)
                continue
        driver.press_keycode(4)
        sleep(1)
        # 退出
        for i in range(5):
            try:
                driver.find_element_by_xpath('//*[@text="退出"]').click()
                sleep(1)
                break
            except Exception as e:
                swipeIconLeft(contentView, driver, 1, 500)
                sleep(1)
                continue


if __name__ == "__main__":
    unittest.main()
