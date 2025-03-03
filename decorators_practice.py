import time
def exec_time (func):
    def wrapper (*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.5f}")
        return result
    return wrapper

@exec_time
def area_rectangle(length, width):
    return length*width

print(area_rectangle(5, 6))
