x, y = map(int, input().split())

for kame in range(x + 1):
    tsuru = x - kame
    ashi = tsuru * 2 + kame * 4
    if y == ashi:
        print('Yes')
        exit()
else:
    print('No')