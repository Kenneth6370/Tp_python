def mult_egyptienne(n,m):
    result = 0
    while n!=0:
        if (n % 2 )==1:
            result = result + m
        n >>= 1
        m <<= 1
    return result
test = mult_egyptienne(40,3)
print(test)