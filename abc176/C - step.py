n = int(input())
a = list(map(int, input().split()))

hight_now = a[0]
ans = 0

for i in range(n):
    if hight_now > a[i]:
        ans += hight_now - a[i]
    else:
        hight_now = a[i]

print(ans)