def deco(function):
    def inner():
        print(f"Hello from {inner.__name__}")
    return inner

@deco
def target():
    print("Hello from target")

target()
print(target)