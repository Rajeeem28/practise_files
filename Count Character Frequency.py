s = "banana"
result = " "
for ch in s:
    if ch not in result:
        result += ch
        print(ch,s.count(ch))
