# maximum consecutive repetition — Find the character with the maximum consecutive
# repetitions in "aaabbccccdde". Expected output: "c".

s = "aaabbccccdde"
result =""
max_count = 0
for i in s:
    count = s.count(i)
    if count > max_count:
        max_count = count
        result = i
print(result)



