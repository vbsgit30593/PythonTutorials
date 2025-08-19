import itertools

def execute(cmd: str) -> None:
    print(f"### {cmd} ###")
    res = []
    match cmd:
        case "groupby":
            st = 'AAABBBBCCCC'
            print(f"{st = }")
            res = itertools.groupby(st)
            for ch, group in res:
                print(f"{ch} -> {list(group)}")
            
            animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear',
                       'bat', 'dolphin', 'shark', 'lion']
            print(f'{animals = }')
            animals.sort(key=len)
            print(f'Sorted {animals = }')

            res = itertools.groupby(animals, len)
            for c, group in res:
                print(f'{c} -> {list(group)}')
        case "tee":
            g1, g2 = itertools.tee('ABCBCBC')
            print(list(zip(g1, g2)))

        case _:
            print("Enter a valid command to exectute!!!")

execute("groupby")
execute("tee")