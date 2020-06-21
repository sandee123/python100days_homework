__author__ = 'Administrator'

def foo():
    b = 'hello'

    # Python中可以在函数内部再定义函数
    def bar():
        c = True
        # nonlocal b
        b = "hi"
        print(a)
        print(b)
        print(c)
    print(b)
    bar()
    print(b) # if don't use "nonlocal b" ,b = 'hello'
    # print(c)  # NameError: name 'c' is not defined


if __name__ == '__main__':
    a = 100
    # print(b)  # NameError: name 'b' is not defined
    foo()