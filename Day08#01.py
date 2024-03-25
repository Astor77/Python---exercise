x = input() # 4
x = int (x)
sum = 0

for i in range(1, x+1) :
    start = 1
    for num in range(1,  i+1) :
        start *= num
    sum += start
        
print(sum) # 33
