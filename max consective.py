# 16. Maximum consecutive ones — Find the longest streak of 1s in [1,1,0,1,1,1]. Expected output: 3.

ls= [1,1,0,1,1,1]
result = 0
count =0
for i in ls:
    if i == 1:
        count += 1
        result = max(result,count)
    else:
        count = 0


print(result)