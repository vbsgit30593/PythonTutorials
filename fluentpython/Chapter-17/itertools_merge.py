import itertools
import operator

def execute(cmd: str) -> None:
    print(f"### {cmd} ###")
    res = []
    match cmd:
        case "chain":
            res = itertools.chain(range(0, 10), range(20, 30), range(1, 3))
        case "chain_from_iterable":
            print(list(enumerate(range(10))))
            res = itertools.chain.from_iterable(enumerate(range(10)))
        case "zip":
            res = zip(range(0, 10), range(2, 6))
        case "zip_longest":
            res = itertools.zip_longest(range(0, 10), range(2, 6), fillvalue="#")
        case "product":
            res = itertools.product('ABC', range(2))
        case _:
            print("Enter a valid command to exectute!!!")
    
    print(list(res))

execute("chain")
execute("chain_from_iterable")
execute("zip")
execute("zip_longest")
execute("product")