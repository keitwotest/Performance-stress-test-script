#coding:UTF-8
"""
--------------------------------------
   File Name：  dingweifz
   Description :
   Author :    admin
   Date：     2018/9/18
   E-mail: 3227456102@qq.com
   adb_activity_package：adb shell dumpsys window w |findstr \/ |findstr name=
--------------------------------------
"""

#重写元素定位的方法
class Action(object):
   #初始化
   def __init__(self, se_driver):
      self.driver = se_driver

   #通过resource-i定位
   def findId(self, id):
      try:
         f = self.driver.find_element_by_id(id)
         return f
      except Exception as e:
         print("未找到%s"%(id))

   #通过class定位
   def findClassName(self, name):
      try:
         f = self.driver.find_element_by_class_name(name)
         return f
      except Exception as e:
         print("未找到%s"%(name))

   #通过text定位
   def findAU(self, name):
      try:
         f = self.driver.find_element_by_android_uiautomator('text(\"' + name +'\")')
         return f
      except Exception as e:
         print("未找到%s"%(name))

   #通过xpath定位
   def findXpath(self, xpath):
      try:
         f = self.driver.find_element_by_xpath(xpath)
         return f
      except Exception as e:
         print("未找到%s"%(xpath))

   #通过content-desc
   def findAI(self, content_desc):
      try:
         f = self.driver.find_element_by_accessibility_id(content_desc)
         return f
      except Exception as e:
         print("未找到%s"%(content_desc))