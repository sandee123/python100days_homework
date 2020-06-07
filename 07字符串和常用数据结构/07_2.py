"""
综合案例
"""

"""
案例1：双色球选号。
红球：1～33，选6个；蓝球：1～16，选1个
"""
import random

def choice_ball():
    n = int(input("机选几注："))
    for _ in range(n):
        # 使用random模块的sample函数来实现从列表中选择不重复的n个元素
        balls = random.sample(range(1, 34), 6)
        balls.sort()
        blue_ball = random.randint(1,16)
        balls.append(blue_ball)
        for i, ball in enumerate(balls):
            if i == len(balls)-1:
                print("|",end=" ")
            print('%02d' %ball, end=' ')
        print()

# choice_ball()


"""
综合案例2：约瑟夫环问题。
《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个
人扔到海里面去，有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到
9的人就扔到海里面，他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔
掉15个人。由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些
位置是基督徒哪些位置是非基督徒。
"""

def Joseph():
    # 初始人数list
    person = []
    for i in range(1,31):
        person.append(i)
    persons = person

    # 循环删除，直到人数等于15
    while len(person) > 15:
        tmp = []
        # 选出当前list里所有9的倍数，放到tmp中
        for j in range(len(person)):
            if (j+1) % 9 == 0:
                tmp.append(person[j])
        # 整理列表，以9为一轮，最后不够9个的，全部放到list的前面，准备下一轮
        # 如果正好没有多余的，位置不变
        if len(person) % 9 != 0:
            n = len(person) % 9
            person_a = person[-n:]
            person = person_a + person[:-n]
        # 把tmp里的数从person list里删除
        for m in range(len(tmp)):
            person.remove(tmp[m])
    # 最后剩下的人，原来的站位编号list
    person_last = person
    person_last.sort()
    print(person_last)

    # 整理哪些位置站的基督徒，哪些站的非基督徒
    p = [None] * 30
    for n in range(len(persons)):
        p[n - 1] = '基' if n in person_last else '非'
    return p
# print(Joseph())

def answer_joseph():
    persons = [True] * 30
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print('基' if person else '非', end='')

# answer_joseph()


"""
综合案例3：井字棋游戏。
"""
