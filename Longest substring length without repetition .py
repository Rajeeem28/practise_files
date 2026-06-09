input = "pwwkew"

# to store previous value from the input string on loop
prev_char = ""

# to store the result (as length)
result = 0

# looping all the character from input one by one
for cur_char in input:
    # print(cur_char)

    # storing a current char when it is not duplicate
    if cur_char not in prev_char:
        prev_char += cur_char

    # incase duplicate character found
    else: #abc -> [a]bc -> bc + a

        if len(prev_char) > result:
            result = len(prev_char)

        dup_char_index = prev_char.index(cur_char)
        # print('duplicate>>>>>')

        sliced_char = prev_char[dup_char_index+1:] + cur_char
        prev_char = sliced_char

        # print('sliced char>>>>',dup_char_index, sliced_char, prev_char)

        # print(prev_char)

if len(prev_char) > result:
    result = len(prev_char)

print('Result', result)
