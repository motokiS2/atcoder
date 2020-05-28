import math
n = int(input())

ans = 0

for i in range(1, n+1):
    if i % 2 == 0:
        continue
    num = 0
    for j in range(1, math.floor(i / 3) + 1):
        if i % j == 0:
            num += 1
    else:
        if num == 7:
            ans += 1

print(ans)
