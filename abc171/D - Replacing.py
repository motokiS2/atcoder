import sys

sys.setrecursionlimit(10**7)

n = int(input())

a = list(map(int, input().split()))
a_num = [0] * 100000
for a_i in a:
    a_num[a_i] += 1

q = int(input())

ans = sum(a)


for _ in range(q):
    b, c = map(int, input().split())
    value_diff = c - b
    b_num = a_num[b]
    c_num = a_num[c]
    a_num[c] += a_num[b]
    a_num[b] = 0
    ans = ans + (a_num[c] - c_num) * c - b_num * b
    print(ans)

