L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

odd_L = []

even_L = []

for n in L :

if n % 2 == 0 :

even_L.append(n)

else :

odd_L.append(n)

L = odd_L + even_L

print(L) # [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
