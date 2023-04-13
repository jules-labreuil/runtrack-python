def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def print_primes():
    for i in range(2, 1001):
        if is_prime(i):
            print(i)

print_primes()