'''
AtCoder Beginner Contest 246
B問題
URL: https://atcoder.jp/contests/abc246/tasks/abc246_b
'''

# 入力
A, B = map(int, input().split())


# 出力
import math

if A == 0 and B != 0:
    x = 0
    y = 1

elif A != 0 and B == 0:
    x = 1
    y = 0

else:
    import math
    y = math.sqrt(B**2 / (A**2 + B**2))
    x = (A * y) / B

print('{:.12f} {:.12f}'.format(x, y))