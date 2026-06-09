s="abcabcbb"
result=""
max_count = 0
for ch in s:
    if ch not in result:
        result+=ch
        # print(ch)
print(len(result))
#     else:
#         if len(result)>max_count:
#             max_count=len(result)
#         print(max_count)
