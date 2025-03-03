import time

def log_execution_time (func):
    def wrapper (*args, **kwargs):
        start_time = time.time() #something's happening before a function is called
        time_laps = func(*args, **kwargs)
        end_time = time.time() #all this happening after a function is called
        print(f"{func.__name__} took {end_time-start_time:.4f} to run")
        return time_laps
    return wrapper

@log_execution_time
def function():
    time.sleep(3)
    print("Function Executed")

function()