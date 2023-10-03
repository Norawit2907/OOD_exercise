def bi_search(l, r, arr, x):
    if arr == [] or r <= l:
        return False
    
    mid = l + ((r - l) // 2)
    
    if arr[mid] == x:
        return True
    
    elif arr[mid] < x:
         arr = arr[mid+1:r+1]
         return bi_search(0, len(arr) - 1, arr, x)
    
    elif arr[mid] > x:
        arr = arr[l:mid]
        return bi_search(0, len(arr) - 1, arr,x)


inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))
