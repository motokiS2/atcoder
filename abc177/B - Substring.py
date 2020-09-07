s = input()
t = input()

ans = 0
max_match = 0
match = 0
for i in range(len(s) - len(t) + 1):
    for j in range(len(t)):
        if s[i+j] == t[j]:
            match += 1
    else:
        max_match = max(max_match, match)
        match = 0

ans = len(t) - max_match

print(ans)

