print("*** Fun with Drawing ***")
n = input("Enter input : ")
n = int(n)
for j in range(n):
    for i in range(2*n + ((2*(n-1)))-1):
        #left side
        if i+j == n-1 : print('*', end = '')
        elif i-j == n-1 : print('*', end = '')
        elif i+j > n-1 and i-j < n-1: print('+', end = '')

        #right side
        elif i+j == (n-1) + (2*(n-1)): print('*', end = '')
        elif i-j == (n-1) + (2*(n-1)): print('*', end = '')
        elif i+j > (n-1) + (2*(n-1)) and i-j < (n-1) + (2*(n-1)): print('+', end = '')
        else:print(".", end = '')
    print('')

for j in range((2*n) - 2):
    for i in range(2*n + ((2*(n-1)))-1):
        if i == j+1 : print('*', end = '')
        elif i == (2*n + ((2*(n-1)))-1)-2-j : print('*', end = '')
        elif i > j+1 and i < (2*n + ((2*(n-1)))-1)-2-j : print('+', end = '')
        else:print(".",end = '')
    print('')