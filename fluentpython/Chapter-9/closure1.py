"""
Target: Write a class such that we keep computing running averages of numbers
"""


class Averager:
    def __init__(self):
        self.nums = []

    def __call__(self, num: int):
        self.nums.append(num)
        return sum(self.nums) / len(self.nums)


avg = Averager()
print(avg(10))
print(avg(11))
print(avg(12))
print(avg(13))
print(avg(14))
print(avg(15))
