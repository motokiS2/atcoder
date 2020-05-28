N, K = map(int, input().split())
ans = 1
while K ** ans <= N :
    ans += 1

print(ans)