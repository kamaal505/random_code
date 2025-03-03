import math
import os
from concurrent.futures import ProcessPoolExecutor

def calculate_factorial(n):
    try:
        return math.factorial(n)
    except Exception as e:
        print (f"Error in calculating {n}!: {e}")

if __name__ == "__main__":
    max_workers = os.cpu_count()
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        results = executor.map(calculate_factorial, range(101))
    print (list(results))
