n = int(input())
ans = ""

alphabet = [chr(i) for i in range(97, 97+26)]

while n > 0:
    k = n - 1
    rem = k % 26
    ans = alphabet[rem] + ans
    n = k // 26



print(ans)