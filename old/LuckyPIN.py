n = int(input())
s = input()

ans = 0

first = []
second = []
third = []

for i in range(n - 2):
    if len(first) == 10:
        break
    if s[i] in first:
        continue
    else:
        first.append(s[i])
    for j in range(i + 1, n - 1):
        if len(second) == 10:
            second = []
            break
        if s[j] in second:
            continue
        else:
            second.append(s[j])

        for k in range(j + 1, n):
            if len(third) == 10:
                ans += 10
                third = []
                break
            if s[k] in third:
                continue
            else:
                third.append(s[k])
        else:
            ans += len(third)
            third = []


print(ans)
