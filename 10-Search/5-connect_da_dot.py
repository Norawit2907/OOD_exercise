inp = input("Enter a list of points: ").split('/')
points = inp[0].split(',')
p = []
for i in points:
    p.append([int(i.split()[0]) ,int(i.split()[1])])
startp = [int(inp[1].split()[0]), int(inp[1].split()[0])]

p.remove(startp)
for i in p:

    pass