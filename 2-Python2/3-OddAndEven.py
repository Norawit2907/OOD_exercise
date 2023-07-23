def odd_even(type, data, mode):
    if type == 'S':
        if mode == 'Odd':
            st = data[::2]
            print(st)
        elif mode == 'Even':
            st = data[1::2]
            print(st)
    if type == 'L':
        str = data.split()
        if mode == 'Odd':
            ans = str[::2]
            print(ans)
        elif mode == 'Even':
            ans = str[1::2]
            print(ans)
print("*** Odd Even ***")
t, d, m = input("Enter Input : ").split(',')
odd_even(t,d,m)