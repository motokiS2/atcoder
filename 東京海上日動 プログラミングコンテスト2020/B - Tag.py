a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())

if a == b:
    print('YES')
    exit()

if a < b:
    after_a = a + v*t
    after_b = b + w*t
    if after_b - after_a <= 0:
        print('YES')
    else:
        print('NO')

if b < a:
    after_a = a - v*t
    after_b = b - w*t
    if after_b - after_a >= 0:
        print('YES')
    else:
        print('NO')