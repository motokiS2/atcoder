n = int(input())
c = input()

a, b = 0, 0

for i in range(n):
    if c[i] == 'R':
        a += 1

ans = max(a, b)

for i in range(n):
    if c[i] == 'R':
        a -= 1
    else:
        b += 1
    now = max(a, b)
    ans = min(now, ans)

print(ans)