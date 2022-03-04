'''
The prime numbers are not regularly spaced. For example from 2 to 3 the gap is 1. From 3 to 5 the gap is 2. From 7 to 11 it is 4. Between 2 and 50 we have the following pairs of 2-gaps primes: 3-5, 5-7, 11-13, 17-19, 29-31, 41-43
We will write a function gap with parameters:

g (integer >= 2) which indicates the gap we are looking for
m (integer > 2) which gives the start of the search (m inclusive)
n (integer >= m) which gives the end of the search (n inclusive)

In the example above gap(2, 3, 50) will return [3, 5] or (3, 5) or {3, 5} which is the first pair between 3 and 50 with a 2-gap.
'''

import functools

@functools.lru_cache(maxsize=128)
def gap(g, m, n):
    primes = []
    for possiblePrime in range(m, n+1):
        isPrime = True
        for num in range(2, possiblePrime):
            if possiblePrime % num == 0:
                isPrime = False
        if isPrime:
            primes.append(possiblePrime)
    for i, x in enumerate(primes):
        if x - primes[i-1] == g:
            return [primes[i-1], x]
    return None


#Method 2
import functools
import itertools

@functools.lru_cache(maxsize=128)
def gap(g, m, n):
    def erat2( ):
        D = {  }
        yield 2
        for q in itertools.islice(itertools.count(3), 0, None, 2):
            p = D.pop(q, None)
            if p is None:
                D[q*q] = q
                yield q
            else:
                x = p + q
                while x in D or not (x&1):
                    x += p
                D[x] = p
                
    def get_primes_erat(n):
        return list(itertools.takewhile(lambda p: p<n, erat2()))
    takeClosest = lambda num,collection:min(collection,key=lambda x:abs(x-num))
    primes_lst = get_primes_erat(n)
    primes = primes_lst[primes_lst.index(takeClosest(m,primes_lst)):]

    for i in range(len(primes)-1):
        if (primes[i+1] - primes[i]) == g:
            return [primes[i], primes[i+1]]
    return None