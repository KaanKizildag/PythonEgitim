def decorator(func):
    import time
    def wrapper(a,b):
        start = time.time()
        time.sleep(1)
        func(a,b)
        finish = time.time()
        print('Geçen süre: '+ str(finish - start))

    return wrapper

@decorator
def toplama(a, b):
    return a+b
@decorator
def carpma(a, b):
    return a*b

carpma(10,20)
toplama(20,0)