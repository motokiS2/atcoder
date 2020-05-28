n = int(input())
a = list(map(int, input().split()))
a_len = len(a)
a_unique = set(a)
a_unique_len = len(a_unique)

if a_len == a_unique_len :
    print('YES')
else :
    print('NO')