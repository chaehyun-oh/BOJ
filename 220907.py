from pprint import pprint
import sys

sys.stdin = open('input01.txt')

# 2447 별찍기-10
# n = int(input())
# s = ['***', '* *', '***']
# cnt = 0


# def getS(S):
#     matrix = []
#     for i in range(3 * len(S)):
#         if i // len(S) == 1:
#             matrix.append(S[i % len(S)] + ' ' * len(S) + S[i % len(S)])
#         else:
#             matrix.append(S[i % len(S)] * 3)
#     return matrix


# while n > 3:
#     n /= 3
#     cnt += 1

# for j in range(cnt):
#     s = getS(s)

# for k in s:
#     print(k)

# swea 1983 조교의 성적 매기기

# T = int(input())
# grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

# for testcase in range(1, T + 1):
#     n, k = map(int, input().split())
#     students = []
#     for i in range(n):
#         mid, fin, asn = map(int, input().split())
#         total = (mid * 0.35) + (fin * 0.45) + (asn * 0.2)
#         students.append(total)

#     Ktotal = students[k-1]
#     students.sort(reverse=True)

#     per = int(n / 10)

#     Kgrd = students.index(Ktotal) // per
#     print(f'#{testcase} {grade[Kgrd]}')


# swea 1984 중간 평균값

# T = int(input())
# for tc in range(1, T+1):
#     nums = list(map(int, input().split()))
#     mxm = max(nums)
#     mnm = min(nums)
#     nums.remove(mxm)
#     nums.remove(mnm)
#     print(f'#{tc} {round(sum(nums)/len(nums))}')

# swea 1989 초심자의 회문검사

T = int(input())
for test_case in range(1, T + 1):
    n = input().strip('')
    if n == n[::-1]:
        print(f'#{test_case}', 1)
    else:
        print(f'#{test_case}', 0)
