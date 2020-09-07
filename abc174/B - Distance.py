import math

def distance(p, q):
    return math.sqrt(p ** 2 + q ** 2)

ans = 0

n, d = map(int, input().split())

for _ in range(n):
    x, y = map(int, input().split())
    dist = distance(x, y)
    if dist <= d:
        ans += 1

print(ans)
