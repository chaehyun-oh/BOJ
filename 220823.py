import sys

sys.stdin = open('input01.txt')

# 균형잡힌 세상 4949
# while True:
#     word = input()
#     if word == '.':
#         break
#     stk = []
#     chk = True
#     for w in word:
#         if w == '(' or w == '[':
#             stk.append(w)
#         elif w == ')':
#             if not stk or stk[-1] == '[':
#                 chk = False
#                 break
#             elif stk[-1] == '(':
#                 stk.pop()
#         elif w == ']':
#             if not stk or stk[-1] == '(':
#                 chk = False
#                 break
#             elif stk[-1] == '[':
#                 stk.pop()
#     if chk == True and not stk:
#         print('yes')
#     else:
#         print('no')


# ----
# 암기왕 2776

# T = int(input())
# for _ in range(T):
#     n = int(input())
#     nlist = set(map(int, input().split()))
#     m = int(input())
#     mlist = list(map(int, input().split()))
#     for mm in mlist:
#         print(1 if mm in nlist else 0)

# 곰곰이 25192

T = int(input())
cnt = 0
loglist = []
xlist = set(loglist)
for _ in range(T):
    loglist.append(input())
for log in loglist:
    if log == 'ENTER':
        xlist.clear()
    else:
        if log not in xlist:
            xlist.add(log)
            cnt += 1
print(cnt)
