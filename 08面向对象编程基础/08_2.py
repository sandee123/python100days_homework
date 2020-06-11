"""
练习2：定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法。
"""
from math import fabs,sqrt

class Point(object):
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        self.point = (self.x,self.y)

    def move_to(self,x,y):
        """
        移动点到新到位置
        :param x: 新的横坐标
        :param y: 新的纵坐标
        :return: 新的位置
        """
        self.x = x
        self.y = y
        point = (self.x, self.y)
        return point

    def distance_to(self,p):
        """
        计算point到point2的距离
        :param x2: point2的横坐标
        :param y2: point2的纵坐标
        :return: 两个点的距离
        """
        dx = fabs(self.x - p.x)
        dy = fabs(self.y - p.y)
        return sqrt(dx**2 + dy**2)

    def move_by(self,x3,y3):
        """
        移动指定的增量
        :param x3: 横坐标的增量
        :param y3: 纵坐标的增量
        :return:
        """
        self.x += x3
        self.y += y3
        point = (self.x, self.y)
        return point

def main():
    p1 = Point(0,0)
    print(p1)
    print(p1.move_to(3,4))
    p2 = Point(-2,-5)
    print(p1.distance_to(p2))
    print(p2.move_by(2,3))



if __name__ == "__main__":
    main()