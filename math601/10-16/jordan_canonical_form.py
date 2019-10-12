def tostr(ls):
    return ''.join(map(str, ls))

def nestedtostr(ls):
    ans = ''
    for x in ls:
        ans += '.' + ''.join(map(str, x))
    while len(ans) <= 20:
        ans += ' '
    return ans

def dfs(block, left, cur, res):
    if block == 0 and left == 0:
        res += [cur.copy()]
    total = 0
    for sz in range(1, left + 1):
        for ev in range(2):
            if ev == 0 and sz > 2: continue
            if ev == 1 and sz > 3: continue
            nxt = []
            for ss in range(sz):
                nxt += [ev]
            if len(cur) == 0 or tostr(cur[-1]) <= tostr(nxt):
                cur += [nxt]
                total += dfs(block - 1, left - sz, cur, res)
                del(cur[-1])
    return total

total = 0
res = []
for numblocks in range(1, 5):
    cur = []
    total += dfs(numblocks, 4, cur, res)

res = sorted(res, key = nestedtostr)
for r in res:
    print(r)

print(total)

