"""
练习1：定义一个类描述数字时钟。
"""
from time import sleep


class NumClock(object):
    def __init__(self,hour,minute,sec):
        self._hh = hour
        self._mm = minute
        self._ss = sec

    def run(self):
        self._ss += 1
        if self._ss == 60:
            self._ss = 0
            self._mm += 1
            if self._mm == 60:
                self._mm = 0
                self._hh += 1
                if self._hh == 24:
                    self._hh = 0

    def show(self):
        return "%02d:%02d:%02d" %(self._hh,self._mm,self._ss)


def main():
    clock = NumClock(23,59,58)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == "__main__":
    main()
