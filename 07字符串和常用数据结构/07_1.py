#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
练习1：在屏幕上显示跑马灯文字。

未解决问题：
无法清理屏幕上的输出，报错：
sh: cls: command not found
"""
import os
import time
def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


"""
练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
"""
import random
def create_code():
    chars = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    code = ''
    chars_len = len(chars)
    code_len = 4
    for _ in range(code_len):
        index = random.randint(0, chars_len-1)
        code += chars[index]
    print("the code is: " + code)

# create_code()

"""
练习3：设计一个函数返回给定文件名的后缀名。
"""

def get_suffix(filename,has_dot=False):
    """
    我写的
    """
    if '.' in filename:
        a = filename.split('.')
        return a[1]
    else:
        return ''

    # """
    #     获取文件名的后缀名
    #     :param filename: 文件名
    #     :param has_dot: 返回的后缀名是否需要带点
    #     :return: 文件的后缀名
    # """
    # pos = filename.rfind('.')
    # if 0 < pos < len(filename) - 1:
    #     index = pos if has_dot else pos + 1
    #     return filename[index:]
    # else:
    #     return ''
# return_suffix("aaa.txt")

"""
练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。
"""
def get_max(x):
    m1,m2 = (x[0],x[1]) if x[0] > x[1] else (x[1],x[0])
    for i in range(2,len(x)):
        if x[i] > m1:
            m2 = m1
            m1 = x[i]
        elif x[i] > m2:
            m2 = x[i]
    return m1,m2

# print(get_max([2,4,6,1,3,7]))

# 最小和第二小
def get_min(x):
    n1,n2 = (x[0],x[1]) if x[0]<x[1] else (x[1],x[0])
    for i in range(2,len(x)):
        if x[i] < n1:
            n2 = n1
            n1 = x[i]
        elif x[i] < n2:
            n2 = x[i]
    return (n1,n2)

# print(get_min([2,4,6,1,3,7]))

"""
练习5：计算指定的年月日是这一年的第几天。
"""
import time,datetime
def get_day(date):
    y1 = date.year
    first_day = datetime.date(y1,1,1)
    return ((date - first_day).days +1)

# print(get_day(datetime.date(2020,3,5)))

"""
练习6：打印杨辉三角。
"""
def yh():
    n = int(input("the rows:"))
    yh = [[]] * n
    # print(yh)
    for i in range(len(yh)):
        yh[i] = [None]*(i+1)
        # print(yh[i])
        for j in range(len(yh[i])):
            if j == 0 or j == i:
                yh[i][j] = 1
            else:
                yh[i][j] = yh[i-1][j-1] + yh[i-1][j]
            print(yh[i][j], end="\t")
        print()


yh()