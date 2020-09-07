n = int(input())
l = list(map(int, input().split()))

ans = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        if l[i] == l[j]:
            continue
        for k in range(j + 1, n):
            if l[i] == l[k] or l[j] == l[k]:
                continue
            max_l = max(l[i], l[j], l[k])
            judge = (l[i] + l[j] + l[k] - max_l) - max_l
            if judge > 0:
                ans += 1

print(ans)

