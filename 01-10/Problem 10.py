#Find the sum of all the primes below two million.

Primos = [2]
Suma = 2
n = int(input("Introduzca el límite para hallar los números primos: "))

def Primes(num):
    for i in range (2,int((num**0.5)+1)):
        if not num % i:
            return False
    return True

for i in range (3,n,2):
    resto = 0
    if Primes(i):
        Primos.append(i)
        Suma += i
        
print(Suma)