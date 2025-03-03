from concurrent.futures import ProcessPoolExecutor

def compute_square(n):
    return n * n

if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = executor.map(compute_square, range(10))
    
    print(list(results))  # Prints squares of numbers 0-9