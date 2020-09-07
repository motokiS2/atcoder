n = int(input())

result = sum(list(map(int, str(n))))

if result % 9 == 0:
    print('Yes')
else:
    print('No')