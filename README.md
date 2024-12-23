# Random big prime number generator

## Algorithm Overview

The prime finding process follows these steps:

1. Generates a random odd number of specified length
2. Performs initial screening using trial division
3. Applies Fermat Primality Test
4. Confirms primality using Miller-Rabin test

## 1. Installation

`pip install -r requirements.txt`

## 2. Configuration (Optional)

Feel free to change CONSTANTS and also find_random_prime parameters.

Constants:

- `DIGITS`: Length of the generating number
- `FIRST_PRIMES`: List of first 25 prime numbers

Parameters:

- `mili_k`: Number of Miller-Rabin test iterations
- `fermat_k`: Number of Fermat test iterations
- `prime_count`: Number of small primes to use in trial division

## 3. Run

`python find.py`
