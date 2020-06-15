x, n = map(int, input().split())

if n == 0:
    print(x)
    exit()

p = list(map(int, input().split()))

left = 0
right = 101

i = 1
while i <= x:
    if i not in p:
        left = i
    i += 1
while right == 101:
    if i not in p:
        right = i
        break
    i += 1

if x - left <= right - x:
    print(left)
else:
    print(right)
