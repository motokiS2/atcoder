T = int(input())

for t in range(T):
    N, A, B, C, D = map(int, input().split())
    memo = {}

    def dist(n):
        if n == 0:
            return 0
        if n == 1:
            return D
        if n in memo:
            return memo[n]

        ret = min(
            D * n,
            D * abs(n - n//5 * 5) + C + dist(n//5),
            D * abs(n - (n + 4)//5 * 5) + C + dist((n+4)//5),
            D * abs(n - n//3*3) + B + dist(n//3),
            D * abs(n - (n+2)//3*3) + B + dist((n+2)//3),
            D * abs(n - n//2*2) + A + dist(n//2),
            D * abs(n - (n+1)//2*2) + A + dist((n+1)//2)
        )

        memo[n] = ret
        return ret
    print(dist(N))