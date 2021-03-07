#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Parent:  # 定义父类
    parentAttr = 100
    age = 100

    def __init__(self):
        print ("调用父类构造函数")

    def parentMethod(self):
        print ('调用父类方法')

    def overwriteMethod(self):
        print ('调用父类重写方法')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print ("父类属性 :", Parent.parentAttr)

    def prt(self):
        print(self)
        print(self.__class__)

class Child(Parent):  # 定义子类
    def __init__(self):
        print ("调用子类构造方法")

    def childMethod(self):
        print ('调用子类方法')

    def overwriteMethod(self):
        print ('调用子类重写方法')


c = Child()  # 实例化子类
c.childMethod()  # 调用子类的方法
c.parentMethod()  # 调用父类方法
c.setAttr(200)  # 再次调用父类的方法 - 设置属性值
c.getAttr()  # 再次调用父类的方法 - 获取属性值
c.overwriteMethod()   # 子类调用重写方法
c.prt() # self
setattr(c,'age',103)
print (hasattr(c,'age'))
print (getattr(c,'age'))