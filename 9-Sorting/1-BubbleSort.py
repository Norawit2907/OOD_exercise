inp = [int(x) for x in input('Enter Input : ').split()] 

lastindex = len(inp) - 1
step = 1
for last in range(len(inp) - 1, 0, -1):
    move = None
    for j in range(lastindex):
        if inp[j] > inp[j + 1]:
            inp[j], inp[j + 1] = inp[j + 1], inp[j]
            move = inp[j+1]
    
    lastindex -= 1
    if last == 1:
        print(f"last step : {inp} move[{move}]")
    elif move != None:
        print(f"{step} step : {inp} move[{move}]")
        step += 1



