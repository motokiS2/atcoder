import math
A, B = map(int, input().split())

xa_min = math.ceil((A * 100) / 8)
xa_max = math.floor(((A + 1) * 100) / 8)

xb_min = math.ceil((B * 100) / 10)
xb_max = math.floor(((B + 1) * 100) / 10)

low_price = max(xa_min, xb_min)

if xb_max <= xa_min or xa_max <= xb_min:
    print(-1)
else :
    print(low_price)