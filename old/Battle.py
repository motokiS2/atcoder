import math

a, b, c, d = map(int, input().split())

takahashi_attack = math.ceil(c / b)
aoki_attack = math.ceil(a / d)

if takahashi_attack <= aoki_attack:
    print('Yes')
else:
    print('No')
