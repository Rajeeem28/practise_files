# ls = [2,500,7,8,90]
# result = sorted(ls)
# print(result)
ls = [2,500,7,8,90]
#
# n = len(ls)
#
# for i in range(n):
#     for j in range(n - i - 1):
#         if ls[j] > ls[j + 1]:
#             ls[j], ls[j + 1] = ls[j + 1], ls[j]
#
# print(ls)

n = len(ls)
for i in range(n):
    for j in range(n-i-1):
        if ls[j] > ls[j+1]:
            ls[j],ls[j+1] = ls[j+1],ls[j]
print(ls)

