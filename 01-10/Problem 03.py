#

A = [2]
cantidad = len(A)

for i in range (2,10000):
    resto = 0
    for y in range (cantidad):
        if i % A[y] == 0:
            resto += 1
    if resto == 0:
        A.append(i)
        cantidad = len(A)
        
primes = []

for j in range (cantidad):
    if 600851475143 % A[j] == 0:
        primes.append(A[j])
        
print(primes)
        