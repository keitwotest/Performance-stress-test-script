#coding:UTF-8
"""
--------------------------------------
   File Name：  test_cheguanjia
   Description :
   Author :    admin
   Date：     2018/9/10
   E-mail: 3227456102@qq.com
   adb_activity_package：adb shell dumpsys window w |findstr \/ |findstr name=
   description:运行全部*.py测试用例
--------------------------------------
"""
__author__ = 'admin'

import unittest,HTMLTestRunner_cn,time,os
from sendemail.send_email import sendreport
import threading
from common.topInfo import top_start

testcase_path = ".\\testcase\\"
report_path = ".\\report\\"

# testcase_path = os.path.join(os.getcwd(),'testcase')
# report_path = os.path.join(os.getcwd(),'report')


def create_suite():
    suit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(testcase_path, pattern="test_gaode.py")
    for test_suit in discover:
        for test_case in test_suit:
            suit.addTest(test_case)
    return suit


if __name__ == "__main__":
    suite = create_suite()
    now = time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))
    reportName = report_path + now + '.html'
    reportFile = open(reportName, "wb")
    runner = HTMLTestRunner_cn.HTMLTestRunner(stream=reportFile, title="应用自动化测试报告", description="各应用自动化测试结果")

    threads = []
    thread1 = threading.Thread(target=top_start)
    threads.append(thread1)

    for t in threads:
        t.setDaemon(True)
        t.start()

    runner.run(suite)
    reportFile.close()
    sendreport()




