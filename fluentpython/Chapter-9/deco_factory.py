registry = set() 
def register(active=True):
    def decorate(func):
        print(f"{func.__name__}: {active=}")
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func
    return decorate

@register(active=False)
def f1():
    pass

@register()
def f2():
    pass

f1()
f2()

print(registry)