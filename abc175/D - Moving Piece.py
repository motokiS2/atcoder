n, k = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))
p = list(map(lambda x: x - 1, p))

ans = -1 * 10 ** 18

for i in range(n):
    x = i
    s = []
    tot = 0
    while True:
        x = p[x]
        s.append(c[x])
        tot += c[x]
        if (x == i):
            break
    l = len(s)
    t = 0
    for j in range(l):
        t += s[j]
        if j + 1 > k:
            break
        now = t
        if tot > 0:
            e = (k - (j + 1)) // l
            now += tot * e
        ans = max(ans, now)

print(ans)
