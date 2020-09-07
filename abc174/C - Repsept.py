k = int(input())

x = 7 % k

s = [0] * k
i = 1

while s[x] == 0:
    if x == 0:
        print(i)
        exit()
    s[x] = 1
    x = (x * 10 + 7) % k
    i += 1

print('-1')