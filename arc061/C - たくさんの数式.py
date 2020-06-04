from itertools import *
s = input()

n = len(s) - 1 # 隙間の数
plus_list = list(product(["+", ""], repeat=n))

ans = 0

for bit in range(1 << n):
    formula = s[0]
    for j, k in zip(plus_list[bit], s[1:]):
        formula += (j + k)
    ans += eval(formula)

print(ans)
