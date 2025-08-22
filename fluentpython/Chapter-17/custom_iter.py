s = "Iterator"

it = iter(s)
while True:
    try:
        n = next(it)
        print(n)
    except StopIteration:
        del it
        break
