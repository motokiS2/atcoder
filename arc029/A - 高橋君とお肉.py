n = int(input())

t = []
for i in range(n):
    t.append(int(input()))

ans = 10 ** 18

for bit in range(1 << n):
    t_1 = 0
    t_2 = 0
    for i in range(n):
        if bit & (1 << i):
            t_1 += t[i]
        else:
            t_2 += t[i]
    else:
        this_time = max(t_1, t_2)
        ans = min(ans, this_time)


print(ans)