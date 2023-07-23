print("*** Fun with countdown ***")
list = input("Enter List : ").split()
num = []
for i in list:
    num.append(int(i))
ans = []
stack = []
count = 0
for i in range(len(num)-1):

    if num[i] - num[i+1] == 1:
        stack.append(num[i])
        #print("append!!", stack)

    if num[i] == 1:
        stack.append(num[i])
        ans.append([x for x in stack])
        #print("answer!", stack, ans)
        count += 1

    if num[i]-num[i+1] != 1:
        #print("clear!", stack)
        stack.clear()

if num[len(num)-1] == 1:
    stack.append(num[len(num)-1])
    ans.append([x for x in stack])
    #print("answer!", stack, ans)
    count += 1

else:
    #print("clear!!!", stack)
    stack.clear()

final = []
final.append(count)
final.append(ans)
print(final)