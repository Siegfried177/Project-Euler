#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

maximo = int(input('''Hasta qué número hallar la diferencia? 
'''))
Suma = Squares = 0

for i in range (maximo+1):
    Suma += i
    Squares += i**2

print(f'La diferencia entre el cuadrado de la suma de los primeros {maximo} números y la suma de sus cuadrados es {Suma**2-Squares}')