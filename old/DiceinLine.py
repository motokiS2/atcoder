def cal_expected(x) :
    return (x + 1) / 2

def sum_dice(k, p) :
    sum = 0
    for i in range(k) :
        sum += p[i]
    return sum


n, k = map(int, input().split())
p = list(map(int, input().split()))

for i in range(n) :
    p[i] = cal_expected(p[i])

max_exp = 0
for i in range(n - k + 1) :
    tmp = sum_dice(i + k, p) - sum_dice(i, p)
    # print(tmp)
    if tmp > max_exp :
        max_exp = tmp

print(max_exp)