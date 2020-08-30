import random
import math

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def gcd(a, b): #Greatest common denominator
  a_factors = prime_factors(a)
  b_factors = prime_factors(b)
  common_factors = [1]

  for x in a_factors:
    if x in b_factors:
      common_factors.append(x)
  
  return(common_factors[-1])

cofactors = 0
coprimes = 0

for x in range(100000):
  a = random.randint(1, 100000)
  b = random.randint(1, 100000)

  if(gcd(a, b) == 1):
    coprimes += 1
  else:
    cofactors += 1

pi = math.sqrt(6 / (coprimes / (coprimes + cofactors)))
print(pi)
