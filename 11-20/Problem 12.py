#Find the first triangle number to have five hundred divisors.
from sympy import divisors 

i = 0
Lista = []

while True:
    i += 1
    t = sum(range(1,i+1))
    if len(divisors(t)) > 500:
        print(t)
        break
                
