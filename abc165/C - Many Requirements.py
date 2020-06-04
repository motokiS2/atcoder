from itertools import *
n, m, q = map(int, input().split())

a, b, c, d = [], [], [], []

for i in range(q):
    a_temp, b_temp, c_temp, d_temp = map(int, input().split())
    a.append(a_temp)
    b.append(b_temp)
    c.append(c_temp)
    d.append(d_temp)

A = list(combinations_with_replacement(range(1,m + 1),n))

ans = 0
ans_i = 0

for A_i in A:
    for i in range(q):
        if A_i[b[i] - 1] - A_i[a[i] - 1] == c[i]:
            ans_i += d[i]

    ans = max(ans, ans_i)
    ans_i = 0

print(ans)