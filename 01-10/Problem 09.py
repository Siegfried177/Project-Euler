#Find the Pythagorean triplet.

limit = int(input("Qué número debe ser la suma? "))
i = 1
Lista = []
Answer = 0
for i in range (1,limit):
    Lista.append(i)

for i in range (len(Lista)):
    for j in range (len(Lista)-1):
        for k in range (len(Lista)-2):
            if i and j and k:
                if i+j+k == limit:
                    if ((i**2) + (j**2)) == (k**2):
                        Answer = i*j*k
                    
print(Answer)


    