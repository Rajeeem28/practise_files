s = "Raj123Lakshmi456"
result = " "
for ch in s:
    if ch.isalpha():
        if 'a'<= ch <='z':
            result += chr(ord(ch)-32)
        elif 'A'<= ch <='Z':
            result += ch
print(result)