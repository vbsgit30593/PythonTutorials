import os


def dirwalk(curdir: str):
    for x in os.walk(curdir):
        print(tuple(x))
    # while True:
    #     try:
    #         print(tuple(cur))
    #         cur = next(cur)
    #
    #     except StopIteration:
    #         del cur
    #         break
    #


dirwalk("../")
