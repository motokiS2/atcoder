# a, b, c = map(int, input().split())
# if a == b != c or b == c != a or c == a != b :
#     print('Yes')
# else :
#     print('No')

nums = list(map(int, input().split()))
if len(set(nums)) == 2 :
    print('Yes')
else :
    print('No')