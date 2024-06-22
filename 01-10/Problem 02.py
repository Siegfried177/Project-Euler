#

a = 0
b = 1
Fibonacci = 1
Suma = 0

while Fibonacci < 4000000:
    Fibonacci = a + b
    a = b
    b = Fibonacci
    if Fibonacci % 2 == 0:
        Suma += Fibonacci
        
print(Suma)