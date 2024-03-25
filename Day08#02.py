x = input() # Hello World

dict = {}

for i in range(len(x)):
    dict[x[i]] = x.count(x[i])

print(dict) # {‘H’: 1, ‘e’: 1, ‘l’: 3, ‘o’: 2, ‘ ’:1, ‘W’: 1, ‘r’: 1, ‘d’: 1}
