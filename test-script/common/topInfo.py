import os


def top_start():
    # logPath = os.path.join(os.getcwd(), 'log')
    # topResult = logPath + "\\top.txt"
    # print(topResult)
    topResult = "F:\\PythonWorkSpace\\autoTest\\logInfo\\top.txt"
    os.popen("adb shell top -m 10 -d 15 -s cpu > " + topResult).readlines()
    print(topResult)
    file = open(topResult, "wb")
    file.close()


if __name__ == '__main__':
    top_start()
