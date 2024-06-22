#What is the 10001st prime number?

n = int(input('''Qué número de primo quiere encontrar?
'''))
Primos = [2]
cantidad = len(Primos)
i = 2
while cantidad != n:
    i += 1
    resto = 0
    for y in Primos:
        if i % y == 0:
            resto += 1
    if resto == 0:
        Primos.append(i)
    cantidad = len(Primos)
    
print(i)