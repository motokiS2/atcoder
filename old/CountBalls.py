N, A, B = map(int, input().split())

set_num = N // (A + B)
mod_num = N % (A + B)
if mod_num >= A :
    mod_num = A

ans = set_num * A + mod_num
print(ans)