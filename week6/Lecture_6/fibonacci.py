# Computes the (n+1)st Fibonacci number iteratively and recursively,
# with and without memoisation.
#
# Written by Eric Martin for COMP9021


def iterative_fibonacci(n):
    if n < 2:
        return n
    previous, current = 0, 1
    for _ in range(2, n + 1):
        previous, current = current, previous + current
    return current

def recursive_fibonacci(n):
    if n >= 2:
        return recursive_fibonacci(n - 2) + recursive_fibonacci(n - 1)
    return n

def memoise_fibonacci(n):
    computed_fibonacci = {0: 0, 1: 1}
    return _memoise_fibonacci(n, computed_fibonacci)

def _memoise_fibonacci(n, computed_fibonacci):
    if n not in computed_fibonacci:
        computed_fibonacci[n] = (_memoise_fibonacci(n - 2, computed_fibonacci) +
                                                           _memoise_fibonacci(n - 1, computed_fibonacci))
    return computed_fibonacci[n]


if __name__ == '__main__':
    print('Generating the first 40 nonzero Fibonacci numbers:')
    for n in range(1, 41):
        print(iterative_fibonacci(n), end = ' ')
        if n % 10 == 0:
            print()
    print()
    print('Generating the first 40 nonzero Fibonacci numbers recursively '
          'up to 40, with memoisation:')
    for n in range(1, 41):
        print(memoise_fibonacci(n), end = ' ')
        if n % 10 == 0:
            print()
    print()
    print('Generating the first 40 nonzero Fibonacci numbers recursively '
          'up to 40, without memoisation:')
    for n in range(1, 41):
        print(recursive_fibonacci(n), end = ' ')
        if n % 10 == 0:
            print()

