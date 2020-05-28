N = int(input())
X = list(map(int, input().split()))

P = round(sum(X) / N)

ans = 0
for x in X :
    ans += (P - x) ** 2

print(ans)