from audioop import avg
import sys

sys.stdin = open('input01.txt')

# 설탕배달 2839

# cnt = 0
# n = int(input())

# while n >= 0:
#     if n % 5 == 0:
#         cnt += (n//5)
#         print(cnt)
#         break
#     n -= 3
#     cnt += 1
# else:
#     print(-1)


# 공 1547
# ball = [1, 0, 0]

# m = int(input())
# for _ in range(m):
#     a, b = map(int, input().split())
#     a -= 1
#     b -= 1
#     if ball[a] == 1:
#         ball[a] = 0
#         ball[b] = 1
#     elif ball[b] == 1:
#         ball[b] = 0
#         ball[a] = 1
# print(ball.index(1)+1)


# 대표값 2592

# nums = []
# n = 10
# for _ in range(n):
#     nums.append(int(input()))
# print(sum(nums)//n)
# print(max(nums, key=nums.count))


# N번째 큰 수 2693

# T = int(input())
# for _ in range(T):
#     nums = list(map(int, input().split()))
#     nums.sort()
#     print(nums[-3])


# 단어뒤집기 9093

T = int(input())
for _ in range(T):
    sts = list(map(str, input().split()))
    rev = []
    for w in sts:
        rev.append(w[::-1])
    ans = ' '.join(rev)
    print(ans)
