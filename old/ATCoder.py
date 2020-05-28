s = input()

acgt_len = 0
max_len = 0

ACGT = ['A', 'C', 'G', 'T']

for i in range(len(s)):
    if s[i] in ACGT:
        acgt_len += 1
    else:
        max_len = max(acgt_len, max_len)
        acgt_len = 0

print(max(acgt_len, max_len))