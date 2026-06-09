input ="abcabcbb"
result = 0 #for storing the length of substring
pre_char = "" #for store pre_char on input

for cur_char in input:
    if cur_char not in pre_char:#loop for only taking without duplicate substring
        pre_char += cur_char
        # print(pre_char)
    else:
        if len(pre_char)>result:
            result = len(pre_char)
        # print(result)

        index_pre_char=pre_char.index(cur_char)
        # print("duplicate>>>",index_pre_char)

        slice_char =pre_char[index_pre_char+1:]+cur_char
        pre_char =slice_char
        # print(pre_char)
if len(pre_char)>result:
    result = len(pre_char)
print("string length",result)
