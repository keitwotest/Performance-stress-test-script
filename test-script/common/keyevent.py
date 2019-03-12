#coding:UTF-8
"""
--------------------------------------
   File Name：  keyevent
   Description :
   Author :    admin
   Date：     2018/9/10
   E-mail: 3227456102@qq.com
   adb_activity_package：adb shell dumpsys window w |findstr \/ |findstr name=
--------------------------------------
"""
__author__ = 'admin'

import os

class keyevent():
    KEYCODE_HOME = 3
    KEYCODE_MENU = 82
    KEYCODE_BACK = 4
    KEYCODE_POWER = 26



def adbKeyEvent(keyname = keyevent.KEYCODE_BACK):
    adb = "adb shell input keyevent %s" % keyname
    os.system(adb)


if __name__ == "__main__":
    adbKeyEvent(keyevent.KEYCODE_BACK)  #执行返回操作




