"""
Goal: The goal of this script is implement the tree command for a class such that
we can dump all its subclasses with a clear representation of hierarchy
"""
def tree(cls, level=0):
    yield cls.__name__, level
    for sub_cls in cls.__subclasses__():
        yield from tree(sub_cls, level + 1)

def display(cls):
    for clsname, level in tree(cls):
        indent = ' ' * 4 * level
        print(f"{indent}{clsname}")


if __name__ == "__main__":
    display(BaseException)