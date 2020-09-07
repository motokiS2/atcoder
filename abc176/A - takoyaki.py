import math

n, x, t = map(int, input().split())

make_times = math.ceil(n / x)

ans = make_times * t

print(ans)