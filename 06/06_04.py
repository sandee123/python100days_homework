__author__ = 'Administrator'

"""回文数"""

def is_huiwenshu(num):
    a = num
    b = 0
    while a > 0:
        b = b*10 + a%10
        a = a//10
    return b == num

"""素数"""
def is_sushu(num):
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True if num != 1 else False

"""回文素数"""
def is_huiwensushu(num):
    return True if is_sushu(num) and is_huiwenshu(num) else False


num = int(input("num= "))
print(is_huiwensushu(num))