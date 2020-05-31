n, m, q = map(int, input().split())

a, b, c, d = [], [], [], []
ans = 0
A = [1]

for i in range(q):
    a_temp, b_temp, c_temp, d_temp = map(int, input().split())
    a.append(a_temp)
    b.append(b_temp)
    c.append(c_temp)
    d.append(d_temp)

def dfs(A):
    if len(A) == n + 1:
        now = 0
        for i in range(q):
            if A[b[i]] - A[a[i]] == c[i]:
                now += d[i]

        ans = max(ans, now)
        return ans

    A.append(A[-1])
    while A[-1] <= m:
        dfs(A)
        A[-1] += 1

print(ans)
