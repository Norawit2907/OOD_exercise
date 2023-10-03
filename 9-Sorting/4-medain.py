def quickSort(lst):
    if len(lst) <= 1:
        return lst
    
    return quickSort([i for i in lst[1:] if i < lst[0]]) + [lst[0]] + quickSort([i for i in lst[1:] if i >= lst[0]])

def findMedian(lst):
    lst = quickSort(lst)
    left = (len(lst) - 1) // 2
    right = left + (len(lst) - 1) % 2

    return (lst[left] + lst[right]) / 2

inp = [int(i) for i in input("Enter Input : ").split()]
for i in range(len(inp)):
    print(f"list = {inp[:i+1]} : median = {findMedian(inp[:i+1])}")

# 1 2 3