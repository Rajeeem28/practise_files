txt = "python is easy and python powerful"
s_text = txt.split(" ")
print(s_text)
count= {}

for s in s_text:
    if s in count:
        count[s] += 1
    else:
        count[s] = 1
print(count)