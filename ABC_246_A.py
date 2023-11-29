"""
AtCoder Beginner Contest 246
A問題
URL：https://atcoder.jp/contests/abc246/tasks/abc246_a
"""
nums = [list(map(int, input().split())) for _ in range(3)]

# x座標だけのリストとy座標だけのリストに分ける
x = [num[0] for num in nums]
y = [num[1] for num in nums]

# 各座標でユニークな数値が答えの座標になる
ans = [0, 0]
for i in range(3):
    if x.count(x[i]) == 1:
        ans[0] = x[i]
    if y.count(y[i]) == 1:
        ans[1] = y[i]
print(*ans)
