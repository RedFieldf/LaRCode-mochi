'''
AtCoder Beginner Contest 246
A問題
URL：https://atcoder.jp/contests/abc246/tasks/abc246_a
'''

# 入力
nums = [list(map(int, input().split())) for _ in range(3)]


# 出力
# x座標について検討
if nums[0][0] == nums[1][0]:
    ans_x = nums[2][0]
 
elif nums[1][0] == nums[2][0]:
    ans_x = nums[0][0]

else:
    ans_x = nums[1][0]

# y座標について検討
if nums[0][1] == nums[1][1]:
    ans_y = nums[2][1]

elif nums[1][1] == nums[2][1]:
    ans_y = nums[0][1]

else:
    ans_y = nums[1][1]

print(ans_x, ans_y)

