#Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

n = input("Ingrese el número: ")
Lista = []
Mayor = 0
for i in n:
    Lista.append(int(i))
for i in range (len(Lista)-12):
    V1 = Lista[i]*Lista[i+1]*Lista[i+2]*Lista[i+3]
    V2 = Lista[i+4]*Lista[i+5]*Lista[i+6]*Lista[i+7]
    V3 = Lista[i+8]*Lista[i+9]*Lista[i+10]
    V4 = Lista[i+11]*Lista[i+12]
    if V1*V2*V3*V4 > Mayor:
        Mayor = V1*V2*V3*V4
        
print(Mayor)
