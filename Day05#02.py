d1 = {1:10, 2:20}

d2 = {3:30, 4:40}

d3 = {5:50, 6:60}

d1 = list(d1.items())

d2 = list(d2.items())

d3 = list(d3.items())

d = dict(d1 + d2 + d3)

print(d)

# print(d) # {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
