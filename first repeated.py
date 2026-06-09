s = "abccde"
result =""
for ch in s:
    if s.count(ch)>1:
        print(ch)
        break