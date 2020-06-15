n = int(input())
a = list(map(int, input().split()))

m = max(a) + 1
a = sorted(a)

count = [0] * m

for x in a:
    if count[x] != 0:
        count[x] = 2
        continue

    for i in range(x, m, x):
        count[i] += 1

ans = 0
for x in a:
    if count[x] == 1:
        ans += 1

print(ans)