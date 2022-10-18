import sys

sys.stdin = open("input01.txt")

# 1920 수 찾기
n = int(sys.stdin.readline())
nums = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
chk = list(map(int, sys.stdin.readline().split()))


def bnr(i, nums, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if i == nums[mid]:
        return 1
    elif i < nums[mid]:
        return bnr(i, nums, start, mid - 1)
    else:
        return bnr(i, nums, mid + 1, end)


for i in chk:
    start = 0
    end = len(nums) - 1
    print(bnr(i, nums, start, end))
