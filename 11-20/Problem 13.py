#

n = input()
k = Suma = 0
Lista1 = []

for i in range (100):
    Lista = []
    for j in range (50):
        Lista.append(n[k])
        k += 1
    num = "".join(Lista)
    Suma += int(num)
numero = str(Suma)

print(f'el numero es{numero[-1:-5]}',Suma)