s = input()

count = 0

for j in range(len(s) - 3):
    for i in range(j, len(s) - 3):
        if int(s[j:4 + i]) % 2019 == 0:
            count += 1

print(count)