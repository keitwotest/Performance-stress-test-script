#coding:UTF-8
"""
--------------------------------------
   *File Name：  screenshot.py
   *Description :
   *Author :    zhong
   *Date：     2019/2/28
   *E-mail: 3227456102@qq.com
--------------------------------------
"""
import time

def screenshot(driver):
    report_path = "C:/Users/admin/Desktop/appautoTest/report/jietu_log/"
    now = time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))
    screenshotName = report_path + now + '.png'  # 自定义命名截图
    driver.get_screenshot_as_file(screenshotName)

if __name__ == '__main__':
    screenshot()

