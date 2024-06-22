# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?.

def Primes (n):
    Primos = [2]
    cantidad = len(Primos)
    for i in range (2,n):
        resto = 0
        for y in range (cantidad):
            if i % Primos[y] == 0:
                resto += 1
        if resto == 0:
            Primos.append(i)
            cantidad = len(Primos)
    return Primos

maximo = int(input('''Hasta que número tiene que ser múltiplo el resultado?
'''))
Num = 1
Primos = Primes(maximo)
for i in Primos:
    a = 0
    b = 2
    while a == 0:
        if i**b < maximo:
            b += 1
        else:
            Num *= i**(b-1)
            a = 1
print(Num)
        
