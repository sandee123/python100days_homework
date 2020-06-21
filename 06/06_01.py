__author__ = 'Administrator'

"""
最大公约数和最小公倍数
"""



def gys(m,n):
    (m, n) = (n, m) if n > m else (m, n)
    # print("m=",m," ","n=",n)
    for i in range(m,0,-1):
        if m % i == 0 and n % i == 0:

            return i

def gbs(m,n):
    return m * n // gys(m,n)


if __name__ == "__main__":
    m = int(input("m = "))
    n = int(input("n = "))
    print("最大公约数：",gys(m,n))
    print("最小公倍数：",gbs(m,n))
