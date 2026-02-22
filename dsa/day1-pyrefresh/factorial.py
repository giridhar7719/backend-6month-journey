def factor(n):
    fact=1
    for i in range(n, 0, -1):
        fact=fact*i
    return fact
factor(5)