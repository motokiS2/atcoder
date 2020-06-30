s = input()
t = input()

ans = 0

st_len = len(s)

for i in range(st_len):
    if s[i] != t[i]:
        ans += 1

print(ans)