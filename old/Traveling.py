n = int(input())

prev_t = 0
prev_x = 0
prev_y = 0

for i in range(n):
    t, x, y = map(int, input().split())
    if t % 2 != (x + y) % 2:
        print('No')
        break
    if t - prev_t < abs(x + y - (prev_x + prev_y)):
        print('No')
        break
    prev_t, prev_x, prev_y = t, x, y
else:
    print('Yes')