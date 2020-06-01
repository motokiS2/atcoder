from decimal import Decimal
import math
a, b = map(Decimal, input().split())

ans = math.floor(a * b)

print(ans)