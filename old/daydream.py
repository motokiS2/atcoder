s = input()

while True:
    if s[-5:] == 'dream':
        s = s[:-5]
        continue
    elif s[-7:] == 'dreamer':
        s = s[:-7]
        continue
    elif s[-5:] == 'erase':
        s = s[:-5]
        continue
    elif s[-6:] == 'eraser':
        s = s[:-6]
        continue
    elif len(s) == 0:
        print('YES')
        break
    else:
        print('NO')
        break