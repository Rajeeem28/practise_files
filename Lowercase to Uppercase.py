s = "data"
result = ""
for ch in s:
    if ch.islower():
        result += chr(ord(ch)-32)
print(result)
