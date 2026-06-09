input ="pwwkew"
result = 0
pre_char = ""

for cur_char in input:
    if cur_char not in pre_char:
        pre_char += cur_char
        print("pre_char",pre_char)
    else:
        if len(pre_char)>result:
            result += len(pre_char)

        index_pre_char =pre_char.index(cur_char)
        # print("index_pre_char",index_pre_char)
        sliced_pre_char = pre_char[index_pre_char+1:]+cur_char
        # pre_char = sliced_pre_char
print(pre_char)
