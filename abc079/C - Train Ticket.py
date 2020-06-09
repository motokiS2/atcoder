from itertools import *

ABCD = input()

n = len(ABCD) - 1 # opの入力数

plumi_list = list(product(["+", "-"], repeat=n))

for bit in range(1 << n):
    formula = ABCD[0]
    for num, op in zip(ABCD[1:], plumi_list[bit]):
        formula += op + num
        ans = eval(formula)

    if ans == 7:
        print(formula + "=7")
        break

