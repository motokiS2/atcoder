n, m, k = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = [0] * (n + 1)
b = [0] * (m + 1)

for i in range(1, n + 1):
    a[i] = A[i - 1] + a[i - 1]

for j in range(1, m + 1):
    b[j] = B[j - 1] + b[j - 1]

ans = 0
num_b = m

for i in range(n + 1):
    if a[i] > k:
        break
    for j in range(num_b, -1, -1):
        if b[j] <= k - a[i]:
            break
        num_b -= 1
    ans = max(ans, i + j)

print(ans)