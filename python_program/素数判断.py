# 素数是只能被 1 和自身整除的大于 1 的整数。

def panduan(a):
    if a<2:
        return False #素数是大于 1 的整数
    for i in range(2,a):
        if a%i==0:
            return False
        else:
            return True


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print(is_prime(5))



   
 
    
 

