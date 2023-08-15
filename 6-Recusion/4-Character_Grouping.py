inp = input("input number : ").split(',')
number = inp[0]
index = inp[1]
#print(number, index, number[int(index)-1])
if number == "":
    print("Output : List is entry")
    exit()
elif int(index) > len(number):
    print("Output : Pin number out of range")
    exit()
elif int(index) < 1:
    print("Output : Pin number less than 1")
    exit()

count = 0
ind = int(index)
def countforward(list, index, char):
    global count

    if len(list) <= index:
        return count

    elif list[index] != char:
        #print(f"base:{count}")
        return count

    else:
        count += 1 
        #print(f"recuse:{count}")
        return countforward(list, index+1, char)

count = countforward(number, ind, number[int(index)-1])
#print(count)

countback = 0
def countbackward(list, index, char):
    global countback
    #print(f"listindex: {list[index]}, char: {char}, index: {index}")
    if index < 0:
        return countback
    
    elif list[index] != char:
        #print(f"backbase:{countback}")
        return countback
    
    elif list[index] == char:
        countback += 1
        #print(f"backrecuse:{countback}")
        return countbackward(list, index-1, char)

countback = countbackward(number, ind-1, number[int(index)-1])
#print(f"countback: {countback}")
print(f"Character : {number[int(index)-1]}")
print(f"Count : {count+countback}")

