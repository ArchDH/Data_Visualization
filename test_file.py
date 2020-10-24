import time

def timer(f):
    def wrapper(*args, **kwrs):
        start = time.time()
        rv = f()
        execution_time = time.time()-start
        print(f"Execution time : {execution_time}")
        return rv

    return wrapper

@timer
def time_test():
    for _ in range(100000000):
        pass

time_test()