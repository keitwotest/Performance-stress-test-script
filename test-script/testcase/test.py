#coding:UTF-8
"""
--------------------------------------
   *File Name：  test.py
   *Description :
   *Author :    zhong
   *Date：     2019/2/28
   *E-mail: 3227456102@qq.com
--------------------------------------
"""


import time,os
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()


@sched.scheduled_job('interval', seconds=5)
def my_job():
    now = os.popen("adb shell dumpsys meminfo")
    print(now)

sched.start()
print(sched.get_jobs())


if __name__ == '__main__':
    my_job()