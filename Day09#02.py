x = input('請輸入一個正整數') # 20
x = int(x)

def is_prime(x):
    for i in range(2, x):
        if x % i == 0 :
            return False
    return True
    
def primes(x):
    for i in range(2, x+1):
        if is_prime(i):
            print(i,end = ", ")
    

# print(is_prime(x))
primes(x)
