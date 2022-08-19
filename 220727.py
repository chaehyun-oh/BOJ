#10809 알파벳 찾기

# word = input()

# for i in range(97, 123):
#     print(word.find(chr(i)))


# 17249 태보태보 총난타

# n = input()

# ns = n.split('(^0^)')

# print(ns[0].count('@'), ns[1].count('@'))


#10988 팰린드롬 확인

# word = input()

# if word == word[::-1]:
#     print(1)
# else:
#     print(0)


# 10818 최소, 최대

# T = int(input())
# nums = list(map(int, input().split()))
# print(min(nums), max(nums))

#이렇게 하면 좀 더 간단함! 순서대로 정렬하고 맨 앞, 맨 뒤 값 프린트
# nums.sort()
# print(nums[0], nums[T-1])


# 1065 한수

# n = int(input())
# han = 0

# for i in range(1, n+1):
#     if i < 100:
#         han += 1
#     else:
#         ns = list(map(int, str(i)))
#         if ns[0] - ns[1] == ns[1] - ns[2]:
#             han += 1

# print(han)    

# 1110 더하기 사이클

# n = int(input())
# key = n
# cnt = 0

# while True:
#     cnt += 1

#     total = n // 10 + n % 10
#     n = n %10 * 10 + total % 10
#     if key == n:
#         print(cnt)
#         break


# 2789 유학금지
word = input()
non = 'CAMBRIDGE'

for i in word:
    if i in non:
        word = word.replace(i, '')
print(word)