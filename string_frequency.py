Input= "aabbccda"
result_key={}#i am taking result in dictinary
output_str=""# after my dict output i modify into string output

#i am using loops for storing value into result

for ch in Input:
    if ch in result_key:
        result_key[ch] += 1
    else:
        result_key[ch] = 1
#this loop is used to display the dict format to string
for key,value in result_key.items():
    output_str += key +str(value)#changing  value into string format
print(output_str)



