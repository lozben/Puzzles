import numpy as np
from decimal import Decimal
from math import gcd

def count_primes(n):
    p = 0

    for i in range(2, int(np.sqrt(n)) + 1):
        while n % i == 0 :
            n = n / i 
            p += 1
    if n != 1:
        p += 1
    
    return p

def prime_operations(x, y):
    d = gcd(int(x), int(y))
    x = x // d
    y = y // d

    return count_primes(x) + count_primes(y)

	
from datetime import datetime
start_time = datetime.now()
print(prime_operations(1e+12, 9.7836473e+11))
end_time = datetime.now()
print('Duration version 1: {}'.format(end_time - start_time))

