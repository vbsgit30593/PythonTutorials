import time
def mydecorator(function):
    def wrapper(*args, **kwargs):
        startTime = time.perf_counter()
        print ("you have been wrapped")
        ret = function(*args, **kwargs)
        endTime = time.perf_counter()
        print (f"Total time for {function.__name__} : {endTime - startTime}")
        return ret
    
    return wrapper

@mydecorator
def myfunc(iters):
    for i in range(iters):
        time.sleep(0.25)
    
    return iters

print (myfunc(5))