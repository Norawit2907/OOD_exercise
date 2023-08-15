
def identifyDemon(x, y):
    #print("running")

    if y > 0 and mapp[y-1][x] == '#':
        mapp[y-1][x] = 'x'
        identifyDemon(x, y-1)
    
    if y < mapy-1 and mapp[y+1][x] == '#':
        mapp[y+1][x] = 'x'
        identifyDemon(x, y+1)
    
    if x > 0 and mapp[y][x-1] == '#':
        mapp[y][x-1] = 'x'
        identifyDemon(x-1, y)
    
    if x < mapx-1 and mapp[y][x+1] == '#':
        mapp[y][x+1] = 'x'
        identifyDemon(x+1, y)
    
    

inp = input("Enter input: ").split()

mapx = int(inp[0])
mapy = int(inp[1])

mapp = [] # map[y][x]
for eachy in range(mapy):
    mapp.append(input('').split())

count = 0
for eachy in range(mapy):
    for eachx in range(mapx):
        #print(f"eachx, eachy: {eachx}, {eachy}")
        if mapp[eachy][eachx] == '#':
            #mapp[eachy][eachx] = 'x'
            #print(f"eachx, eachy: {eachx}, {eachy}")
            identifyDemon(eachx, eachy)
            count += 1

# print("")
# for eachy in mapp:
#     s = ''
#     for eachx in eachy:
#         s += eachx + " "
#     print(s)
print(count)