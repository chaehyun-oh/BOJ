import sys

# 7785 회사에 있는 사람

# T = int(sys.stdin.readline())
# # T = int(input())
# enlog = {}
# for _ in range(T):
#     k, v = sys.stdin.readline().rstrip().split()
#     # k, v = map(str, input().split())
#     enlog[k] = v

# lst = []
# for key in enlog:
#     if enlog[key] == 'enter':
#         lst.append(key)

# lst.sort(reverse=True)
# for name in lst:
#     print(name)

#----------------------------
# 1302 베스트셀러

T = int(sys.stdin.readline())
bs = {}

for _ in range(T):
    n = sys.stdin.readline().rsplit()
    bs[n] = bs[n] + 1

bs = sorted(bs.items())
print(sorted(bs, key = lambda x : x[1], reverse=True))


# bstsell = []

# for b, num in bst.items():
#     if num == bstmax:
#         bstsell.append(b)

# print(sorted(bstsell))