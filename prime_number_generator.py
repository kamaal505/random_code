def prime_numbers (limit):
    x = 2
    count = 0
    while count < limit:
        for n in range(2, int(x**0.5)+1):
            if x % n == 0:
                break
        else:
            yield x
            count += 1
        x += 1

primes = prime_numbers(100)
for prime in primes:
    print(prime)