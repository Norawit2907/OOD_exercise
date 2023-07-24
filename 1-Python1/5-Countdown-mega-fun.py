print("*** Fun with countdown ***")
inputint = [int(x) for x in input("Enter List : ").split()]
list = [1]
temp = []
for i in range(len(inputint) - 1):


    if inputint[i] - inputint[i+1] == 1:
        print(f"{inputint[i]} {inputint[i+1]}")
        temp.append(inputint[i])
        print(f"append:{temp}")
        if inputint[i+1] == 1:
            temp.append(1)
            list.append([x for x in temp])
    elif inputint[i] == 1:
        list.append([1])
    
    else:
        temp.clear()



if len(list) == 1:
    print("no countdown")
else:
    list[0] = len(list) - 1

print(list)


