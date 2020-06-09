d, g = map(int, input().split())

p, c = [], []

for i in range(d):
    p_tmp, c_tmp = map(int, input().split())
    p.append(p_tmp)
    c.append(c_tmp)

ans = 10 ** 18

for bit in range(1 << d):
    solve = 0
    score = 0
    for i in range(d):
        if bit & (1 << i):
            score += 100 * (i + 1) * p[i]
            score += c[i]
            solve += p[i]
        if score >= g:
            ans = min(ans, solve)
    else:
        if score < g:
            tmp = (1 << d) - 1
            not_bit = bit ^ tmp
            digit = 0
            while not_bit != 0:
                digit += 1
                not_bit = not_bit >> 1
            for j in range(p[digit - 1]):
                score += digit * 100
                solve += 1
                if score >= g:
                    ans = min(ans, solve)
                    break

print(ans)
