input= "aabcccbcaaa"
compress_output={}
str_output = ""

for i in input:
    if i in compress_output:
        compress_output[i] += 1
    else:
        compress_output[i] = 1
for key,value in compress_output.items():
    str_output += key+ str(value)
print(str_output)