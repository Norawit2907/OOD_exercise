num = input("Enter Your List : ").split()
num = [int(x) for x in num]
ans = []
if len(num) <= 2:
    print ("Array Input Length Must More Than 2")
else:
    for x in range(len(num) - 2):
        for y in range(x+1, len(num) - 1):
            for z in range(y+1, len(num)):
                num1 = num[x]
                num2 = num[y]
                num3 = num[z]
                if num1 + num2 + num3 == 0:
                    str = []
                    str.append(num1)
                    str.append(num2)
                    str.append(num3)
                    if str not in ans:
                        ans.append([x for x in str])

    print(ans)