if not x.isdigit() :
    print(f'{x} 是一個不合法的輸入，無法運算')

f = 1
for number in range(1,  int(x) + 1) :
    f *= number

print(f) # 24
