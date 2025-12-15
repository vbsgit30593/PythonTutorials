"""
Write a closure which calculates a running average
"""


def make_averager():
    total = 0
    count = 0

    def averager(num: int):
        nonlocal total, count
        total += num
        count += 1
        return total / count

    return averager


avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))
print(avg(13))
print(avg(14))
