def print_even(limit):
    for i in range(2, limit + 1, 2):
        yield i

for even in print_even(10):
    print(even)
