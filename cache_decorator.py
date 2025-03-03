def results_cache(func):
    cache = {}
    def wrapper (*args, **kwargs):
        if args in cache:
            print ("Retrieving result from cache: ")
            return cache[args]
        else:
            result = func(*args, *kwargs)
            cache[args]= result
            return cache[args]
        
    return wrapper

@results_cache
def product(x, y):
    return x*y

print (product(5, 7))
print (product(5, 7))