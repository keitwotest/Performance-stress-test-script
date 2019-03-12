from appium import webdriver


def appium_start():
    config = {
        'platformName': 'Android',
        'platformVersion': '5.1',
        'deviceName': '106D111803020337',
        # 'appPackage': 'cn.yunovo.car.settings',
        # 'appActivity': 'cn.yunovo.car.settings.SettingsListActivity',
        'automationName': 'Appium',
        'noReset': True,
        'unicodeKeyboard': True,
        'resetKeyboard': True
    }
    return config
    # return webdriver.Remote('http://localhost:4723/wd/hub', config)


