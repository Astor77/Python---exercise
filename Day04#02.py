L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

L.insert(0,L[len(L)-1])

L.pop(len(L)-1)

print(L) # [9, 1, 2, 3, 4, 5, 6, 7, 8]
