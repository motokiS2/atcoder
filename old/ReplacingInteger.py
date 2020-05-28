n, k = map(int, input().split())

n_k = n % k

ans = min(n_k, k - n_k)

print(ans)