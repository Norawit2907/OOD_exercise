inp = list(map(int,input("Enter Input : ").split()))
#print(inp)

def findmin(numlist, min, index):
    if index == 0:
        return min
    if min == None:
        min = numlist[index-1]
    elif min > numlist[index-1]:
        min = numlist[index-1]
    
    return findmin(numlist, min, index-1)

print(f"Min : {findmin(inp, None, len(inp))}")
    