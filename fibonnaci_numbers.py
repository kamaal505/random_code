import os
def fibonnaci(limit):
    a,b = 0,1 
    for _ in range(limit):
        yield a 
        a, b = b, a+b

fibonnaci_numbers = list(fibonnaci(100))
print(fibonnaci_numbers)
print(os.cpu_count())