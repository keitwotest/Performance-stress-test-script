# rect可获取控件的起始x和y坐标，控件的width和height
from time import sleep


def swipeIconUp(icon, driver, n, t):
    """向上滑动"""
    iconRect = icon.rect
    print(iconRect)
    iconStartX = iconRect['x']
    iconStartY = iconRect['y']
    iconWidth = iconRect['width']
    iconHeight = iconRect['height']
    x1 = iconStartX + iconWidth / 2
    y1 = iconStartY + iconHeight * 0.75
    y2 = iconStartY + iconHeight * 0.25
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)
        sleep(1)


def swipeIconDown(icon, driver, n, t):
    """向下滑动"""
    iconRect = icon.rect
    print(iconRect)
    iconStartX = iconRect['x']
    iconStartY = iconRect['y']
    iconWidth = iconRect['width']
    iconHeight = iconRect['height']
    x1 = iconStartX + iconWidth / 2
    y1 = iconStartY + iconHeight * 0.25
    y2 = iconStartY + iconHeight * 0.75
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)
        sleep(1)


def swipeIconRight(icon, driver, n, t):
    """向右滑动"""
    iconRect = icon.rect
    print(iconRect)
    iconStartX = iconRect['x']
    iconStartY = iconRect['y']
    iconWidth = iconRect['width']
    iconHeight = iconRect['height']
    x1 = iconStartX + iconWidth * 0.25
    x2 = iconStartX + iconWidth * 0.75
    y1 = iconStartY + iconHeight / 2
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)
        sleep(1)


def swipeIconLeft(icon, driver, n, t):
    """向左滑动"""
    iconRect = icon.rect
    print(iconRect)
    iconStartX = iconRect['x']
    iconStartY = iconRect['y']
    iconWidth = iconRect['width']
    iconHeight = iconRect['height']
    x1 = iconStartX + iconWidth * 0.75
    x2 = iconStartX + iconWidth * 0.25
    y1 = iconStartY + iconHeight / 2
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)
        sleep(1)