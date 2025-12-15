a = 10


def func():
    global a
    b = 20
    print(a)
    print(b)

    a = 30
    print(a)


func()

from dis import dis

dis(func)
