__author__ = 'Administrator'
"""
回文数
"""

def is_huiwenshu(num):
    a = num
    b = 0
    while a > 0:
        b = b*10 + a%10
        a = a//10
    return b == num


if __name__ == "__main__":
    num = int(input("num= "))
    print(is_huiwenshu(num))