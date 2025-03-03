def squares (limit):
    x = 1
    while x < limit:
        yield x**2
        x += 1

for num in squares(10):
    print(num)