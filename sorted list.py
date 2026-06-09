# 20. Merge two sorted lists — Merge [1,3,5] and [2,4,6] into one sorted list without using sort.
ls = [1,3,5]
ls1 = [2,4,6]

res = tuple(ls)
res1 = tuple(ls1)
print(sorted(list(res+res1)))