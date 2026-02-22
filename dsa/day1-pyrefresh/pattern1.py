# *****
# *****
# *****
# *****
# *****
def p1(n):
    for i  in range(n):
        for j in range(n):
            print("*",end="")
        print()
p1(5)        


# *
# **
# ***
# ****
# *****

def p2(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        print()    
p2(5)


# *****
# ****
# ***
# **
# *


def p3(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end="")
        print()
p3(5)


# 1
# 12
# 123
# 1234
# 12345

def p4(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        print()
p4(5)
    
    
    
