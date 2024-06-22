#What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the grid.

n = input("Ingrese la matriz: ")
Lista= n.split(" ")
Matriz = []
Mayor = k = 0

for i in range(20):
    A = []
    for j in range (20):
        A.append(int(Lista[k]))
        k += 1
    Matriz.append(A)
dimension = len(Matriz)

for i in range (dimension):
    for j in range (dimension-3):
        Product = Matriz[i][j]*Matriz[i][j+1]*Matriz[i][j+2]*Matriz[i][j+3] 
        if Product > Mayor:
            Mayor = Product
    
for i in range (dimension-3):
    for j in range (dimension):
        Product = Matriz[i][j]*Matriz[i+1][j]*Matriz[i+2][j]*Matriz[i+3][j] 
        if Product > Mayor:
            Mayor = Product
        
for i in range (dimension-3):
    for j in range (dimension-3):
        Product = Matriz[i][j]*Matriz[i+1][j+1]*Matriz[i+2][j+2]*Matriz[i+3][j+3] 
        if Product > Mayor:
            Mayor = Product
        
for i in range (dimension-3):
    for j in range (dimension-3):
        Product = Matriz[i][j]*Matriz[i+1][j-1]*Matriz[i+2][j-2]*Matriz[i+3][j-3] 
        if Product > Mayor:
            Mayor = Product

print(Mayor)