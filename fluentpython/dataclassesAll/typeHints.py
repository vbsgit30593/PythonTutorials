class Demo:
    var1: int
    var2: int = 10
    var3 = 20

obj = Demo()
print (obj.__annotations__)
print (Demo.var2)
print (Demo.var3)
print (Demo.var1)
