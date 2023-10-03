def mergeSort(lst, left, right):
    center = (left + right) // 2
    
    if left < right:
        mergeSort(lst, left, center)
        mergeSort(lst, center+1, right)
        merge(lst, left, center+1, right)

def merge(lst, left, right, rightEnd):
    start = left
    leftEnd = right - 1
    result = []

    while left <= leftEnd and right <= rightEnd:
        if lst[left][0] < lst[right][0]:
            result.append(lst[left])
            left += 1

        else:
            result.append(lst[right])
            right += 1
    
    while left <= leftEnd:
        result.append(lst[left])
        left += 1
    
    while right <= rightEnd:
        result.append(lst[right])
        right += 1

    for i in result:
        lst[start] = i
        start += 1
        if start > rightEnd:
            break

inp = [int(x) for x in input("input : ").split()]
#print(inp)
lst = []
for i in range(0, len(inp)-1, 2):
    lst.append([inp[i], inp[i+1]])
    
#print(lst)
mergeSort(lst, 0, len(lst)-1)
#print(lst)

result = 0
for each in reversed(lst):
    for temp in lst:
        #print(each, temp)
        if temp == each:
            break
        
        if each[1] < temp[1]:
            #print(f"plus : {each[1]} + {temp[1]}")
            result += each[0] + temp[0]
    #print()

print(f"ans = {result}")
