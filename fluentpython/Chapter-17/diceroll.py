from random import randint


def rollme() -> int:
    return randint(1, 10)


dice = iter(rollme, 7)
for roll in dice:
    print(roll)
