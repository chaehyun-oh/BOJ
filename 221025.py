import sys

sys.stdin = open("input01.txt")
# 1541 잃어버린 괄호

a = input().split("-")
nums = []
for i in a:
    cnt = 0
    s = i.split("+")
    for j in s:
        cnt += int(j)
    nums.append(cnt)
n = nums[0]
for k in range(1, len(nums)):
    n -= nums[k]
print(n)
