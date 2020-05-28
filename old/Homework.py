n, m = map(int, input().split())
a = list(map(int, input().split()))

day = 0
for i in a:
    day += i

if n >= day:
    print(n - day)
else:
    print(-1)