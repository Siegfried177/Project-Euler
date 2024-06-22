def even (num):
    num = num / 2
    return num

def odd (num):
    num = (3*num)+1
    return num

x = 0
mayor = 0
while x <1000000:
    contador = 0
    x += 1
    i = x
    while i != 1.0:
        if not i % 2:
            i = even(i)
        else:
            i = odd(i)
        contador += 1
        if contador > mayor:
            mayor = contador
            elmayor = x            

print(elmayor)