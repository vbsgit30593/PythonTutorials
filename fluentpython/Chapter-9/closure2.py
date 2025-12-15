def make_averager():
    series = []

    def averager(num: int):
        series.append(num)
        return sum(series) / len(series)
    
    return averager

avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))
print(avg(13))
print(avg(14))
