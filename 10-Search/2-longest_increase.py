data = [int(x) for x in input("Data : ").split()]
n = 1
ans = [99999999999]
cur = None
longest = -1
for i in data:
    while ans != [] and i <= ans[-1]:
        ans.pop(-1)

    ans.append(i)
    if len(ans) >= longest:
        longest = len(ans)
    print(f'{n} : {ans}')
    n += 1

print(f'longest increasing subsequence : {longest}')