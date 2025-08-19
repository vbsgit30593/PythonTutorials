sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
print(f"{sample=}")
import itertools
import operator

def execute(cmd: str) -> None:
    print(f"### {cmd} ###")
    res = []
    match cmd:
        case "accumulate1":
            res = itertools.accumulate(sample)
        case "accumulate2":
            print("running min")
            res = itertools.accumulate(sample, min)
        case "accumulate3":
            print("running multipliers")
            res = itertools.accumulate(sample, operator.mul)
        case "factorial":
            print("running factorial of 1 to 10")
            res = itertools.accumulate(range(1, 11), operator.mul)
        case "starmap":
            print("compute a running average of the sample")
            # In case of a running average, we divide the running sum with current
            # number of sample. The running sum can be computed using accumulate.
            # That running sum can be enumerated. The result would be a tuple of
            # running sum and number of samples
            res = enumerate(itertools.accumulate(sample), start=1)
            res = itertools.starmap(lambda a, b: round(b / a, 2), res)
        
        case _:
            print("Enter a valid command to exectute!!!")
    
    print(list(res))

execute("accumulate1")
execute("accumulate2")
execute("accumulate3")
execute("factorial")
execute("starmap")

"""
sample=[5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
### accumulate1 ###
[5, 9, 11, 19, 26, 32, 35, 35, 44, 45]
### accumulate2 ###
running min
[5, 4, 2, 2, 2, 2, 2, 0, 0, 0]
### accumulate3 ###
running multipliers
[5, 20, 40, 320, 2240, 13440, 40320, 0, 0, 0]
### factorial ###
running factorial of 1 to 10
[1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
### starmap ###
compute a running average of the sample
[5.0, 4.5, 3.67, 4.75, 5.2, 5.33, 5.0, 4.38, 4.89, 4.5]
"""