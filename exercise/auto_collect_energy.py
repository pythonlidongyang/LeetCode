#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/2/8 9:06
# @Author : Dongyang Li
# @File : auto_collect_energy.py
# 借助Uiautomator2，这些都可以自动化。UiAutomator是Google提供的用来做安卓自动化测试的一个Java库，可以获取屏幕上任意一个APP的任意一个控件属性，并对其进行任意操作。Uiautomator2是在Uiautomator之上的python的接口封装，简单来说 Uiautomator2可以看到手机当前屏幕上有哪些控件，其坐标是啥，并且还可以模拟点击。
# 安装pip install --upgrade --pre uiautomator2
'''原理：
1.打开支付宝
2.打开蚂蚁森林
3.先收取自己的能量
4.跳到下一个有能量的人哪
5.收取ta的能量
6.重复4和5，直到没有能量可以偷'''

import uiautomator2 as u2
import time
import random

d = u2.connect()#通过有线方式连接，手机需要使用usb数据线插在电脑上，并开始开发者模式，USB调试
#d = u2.connect('192.168.0.108')  # 通过无线方式连接，电脑和手机必须在同一局域网内，并且需要先用有线的方式做过初始化

print('打开支付宝')
d.app_start('com.eg.android.AlipayGphone')
time.sleep(2)
print('打开蚂蚁森林，请等待.....')
d(text="蚂蚁森林").click()
time.sleep(3)


def collectEnergy(cnt):
    print("开始第%d次偷能量！% cnt")

    for x in range(150, 1000, 150):
        for y in range(600, 900, 150):
            d.long_click(x + random.randint(10, 20), y + random.randint(10, 20), 0.1)
            time.sleep(0.01)
            if cnt != 1:
                d.click(536, 1816)


cnt = 1
while True:
    collectEnergy(cnt)
    a = d.xpath("//*[@resource-id='J_tree_dialog_wrap']").get().bounds
    d.click(1000,a[3]-80)
    if d.xpath('//*[@text="返回我的森林"]').click_exists(timeout=2.0):
        break
    cnt +=1
print('能量偷完了....')
d.app_stop("com.eg.android.AlipayGphone")

