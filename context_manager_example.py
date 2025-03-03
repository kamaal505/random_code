import time
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.time()
    yield
    end = time.time()
    print(f"Execution time = {end-start:.5f} seconds")

from prime_number_generator import prime_numbers

with timer():
    print(list(prime_numbers(100)))