"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    primeList = []
    nonPrimeList = []
    
    # Generate a list of non-primes
    for i in range(2,8):
        for j in range(i*2,number_of_primes*5,i):
            nonPrimeList.append(j)

    # Search throgh to find primes
    x = 2
    while len(primeList) < number_of_primes:
        if x not in nonPrimeList:
            primeList.append(x)
        x+=1
    return primeList
