def ascending(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i + 1]:
            return False
    return True

def descending(lst):
    for i in range(len(lst)-1):
        if lst[i] < lst[i + 1]:
            return False
    return True

def duplicate(lst):
    return len(set(lst)) != len(lst)

def allSame(lst):
    return len(set(lst)) == 1

inp = [int(i) for i in input("Enter Input : ")]


up = ascending(inp)
down = descending(inp)
dup = duplicate(inp)
same = allSame(inp)

if same:
    print("Repdrome")

elif up and not dup:
    print("Metadrome")

elif up and dup:
    print("Plaindrome")

elif down and not dup:
    print("Katadrome")

elif down and dup:
    print("Nialpdrome")

else:
    print("Nondrome")


