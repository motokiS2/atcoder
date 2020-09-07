x, k, d = map(int, input().split())

x = abs(x)

# 0をまたがないなら0の方向にk回移動下座標が答え
if x - k * d > 0:
    print(x - k * d)
    exit()

# 0をまたぐ瞬間の移動回数
step_num = x // d + 1

remain_steps = k - step_num

if remain_steps % 2 == 0:
    ans = abs(x - step_num * d)
else:
    ans = x - (step_num - 1) * d

print(ans)