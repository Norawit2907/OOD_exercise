inp = list(map(int, input("Enter Input a b : ").split()))
base = inp[0]
pw = inp[1]

# a is base b is pw
def power(a,b):
    if b == 0:
        return 1
    else:
        return a * power(a, b-1)

print(power(base, pw))