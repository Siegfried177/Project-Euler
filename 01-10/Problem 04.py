#Find the largest palindrome made from the product of two 3-digit numbers.

Mayor = 800000

for i in range (100,1000):
    for j in range (100,1000):
        num = i*j
        if num % 10 == num // 100000:
                if (num //10) % 10 == (num //10000) % 10:
                    if (num //100) % 10 == (num//1000) % 10:
                        if num > Mayor:
                            Mayor = num
                            
print(Mayor)