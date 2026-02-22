def sum_of_even_numbers(n):
    total=0
    for i in range(1,n+1):
        if i%2==0:
            total+=i
    return total
print(sum_of_even_numbers(20))