n = int(input())
a = list(map(int, input().split()))

sum_a = sum(a)

ans = 0

for i in range(n - 1):
    sum_a -= a[i]
    ans += a[i] * sum_a

ans = ans % (10 ** 9 + 7)

print(ans)