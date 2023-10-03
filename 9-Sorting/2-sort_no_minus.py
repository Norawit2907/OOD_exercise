inp = [int(x) for x in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    insertE = inp[i]
    current = i

    if insertE < 0:
        continue

    for j in range(i, -1, -1):
        if inp[j-1] < 0 and j != 0:
            continue


        if inp[j-1] > insertE and j > 0:
            inp[current] = inp[j-1]
            current = j-1
        else:
            inp[current] = insertE
            break

print(*inp)