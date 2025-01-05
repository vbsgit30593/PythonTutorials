from collections import OrderedDict

class FixedSizeDicts(OrderedDict):
    def __init__(self, size, *args, **kwargs):
        self.size = size
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        l = locals()
        # del l['self'], l['__class__']
        print (l)
        if len(self) >= self.size:
            self.popitem(last=False)
        super().__setitem__(key, value)

d = FixedSizeDicts(2)
d[10] = 20
d[20] = 30
d[30] = 40

print (d)
