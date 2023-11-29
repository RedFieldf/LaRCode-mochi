"""
AtCoder Beginner Contest 246
B問題
URL: https://atcoder.jp/contests/abc246/tasks/abc246_b
"""
import math

A, B = map(int, input().split())

# ベクトルの大きさを計算
length = math.sqrt((A**2 + B**2))

# 位置ベクトルを計算して出力
print(A / length, B / length)
