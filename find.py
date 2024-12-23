import gmpy2
import os
import time


DIGITS = 7000

FIRST_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                    43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def generate_random_number(a, b):
    """
    Generate a random number between a and b
    """
    seed = int.from_bytes(os.urandom(16), "big")
    random_state = gmpy2.random_state(seed)
    random_number = gmpy2.mpz_random(random_state, b - a) + a
    return random_number | 1


def is_divisible_by_first_primes(n, first_primes):
    """
    Check if a number is divisible by the first primes
    """
    for prime in first_primes:
        if n % prime == 0:
            return True
    return False


def is_prime_fermat(n, k):
    """
    Perform the Fermat Primality Test.
    """
    # Perform k tests
    for _ in range(k):
        # Choose a random integer a in the range [2, n-2]
        a = generate_random_number(2, n - 2)
        # Test Fermat's Little Theorem
        if pow(a, n - 1, n) != 1:
            return False  # n is composite

    return True


def is_prime_mili(n, k):
    """
    Perform the Miller-Rabin Primality Test.
    """

    # find r and s
    s = gmpy2.mpz(0)
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2

    # do k tests
    for _ in range(k):
        a = generate_random_number(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = gmpy2.mpz(1)
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True


def find_random_prime(mili_k, fermat_k, prime_count):
    """
    Find a random prime number
    """
    first_primes = FIRST_PRIMES[:prime_count]
    A = gmpy2.mpz("1" + "0" * (DIGITS - 1))
    B = gmpy2.mpz("9" * DIGITS)

    start = time.time()
    while True:
        maybe_prime = generate_random_number(A, B)
        x = maybe_prime % 10**10
        print(x)
        if is_divisible_by_first_primes(maybe_prime, first_primes):
            continue
        if not is_prime_fermat(maybe_prime, fermat_k):
            continue
        if not is_prime_mili(maybe_prime, mili_k):
            continue

        end = time.time()
        print("The prime is:", maybe_prime)
        print("Time taken:", (end - start) / 60, "minutes")
        break


find_random_prime(5, 15, 15)
