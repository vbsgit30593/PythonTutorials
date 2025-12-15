reg_list = []


def register(func):
    print(f"Registering {func}")
    reg_list.append(func)
    return func


@register
def f1():
    print("f1")


@register
def f2():
    print("f2")


def f3():
    print("f3")


f1()
f2()
f3()

print(f"{reg_list = }")
