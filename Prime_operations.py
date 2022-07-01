import numpy as np
from decimal import Decimal

def prime_operations(x, y):
    out = {}
    Pair = [x, y]
    Pair.sort()
    M = Pair[1]
    m = Pair[0]
    sqroot = int(Decimal(M).sqrt()) + 1
    sieve = [True]*sqroot
    keys = out.keys
    for p in range(2, sqroot):
        if (sieve[p]):
            while M % p == 0 or m % p == 0:
                if m == M:
                    break
                if M % p == 0:
                    M = M / p
                    if p not in keys():
                        out[p] = 1
                    else:
                        out[p] += 1
                elif m % p == 0:
                    m = m / p
                    if p not in keys():
                        out[p] = -1
                    else:
                        out[p] -= 1

            for i in range(p, sqroot, p):
                sieve[i] = False
                
    if m != 1 and M != m:
        out[m] = 1
    if M != 1 and M != m:
        out[M] = 1
    out_list = np.sum(list(map(abs, out.values())))
    return out_list
	
from datetime import datetime
start_time = datetime.now()
print(prime_operations(1e+12, 9.7836473e+11))
end_time = datetime.now()
print('Duration version Katya: {}'.format(end_time - start_time))