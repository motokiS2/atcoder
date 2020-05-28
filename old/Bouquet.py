n, a, b = map(int, input().split())

combi_all = 2 ** n - 1

combi_a = 0
combi_b = 0

def calc_combi(n, k) :
    combi = 1
    for i in range(k) :
        combi *= (n - k)
    for i in range(k) :
        combi //= (k - i)
    return combi

combi_a = calc_combi(n, a)
combi_b = calc_combi(n, b)

ans = combi_all - (combi_a + combi_b)
ans //= (10 ** 9) + 7

print(ans)