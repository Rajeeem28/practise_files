# 1. Remove first and last character — Remove the first and last character from a string. Input:
# "Python" → Output: "ytho".

#
# A = "Python"
# Sl = A[1:5]
# print(Sl)

# 2. Convert snake case to camel case — Convert "hello_world"`` to"helloWorld"`.

# A= "hello_world"
# B = A.split("_")
# camel_Case = B[0]+B[1].capitalize()
# print(camel_Case)
#
# 3.Extract letters and convert to uppercase — From "Ferilionlabs2026", create a new string containing
# only letters and convert them to uppercase without built-in methods.
#
# A = "Ferilionlabs2026"
# st = " "
# for ch in A:
#     if ch.isalpha():
#         st += ch.upper()
# print(st)

#
# A ="Ferilionlabs2026"
# res =" "
# for ch in A:
#     if 'a' <=ch <= 'z':
#         res += chr(ord(ch)-32)
#     elif 'A' <=ch <='Z':
#         res += ch
# print(res)
#
# 4. Longest word in a sentence — Find the longest word in "Python programming language". Expected
# output: "Programming".
A ="Python programming language"
sp_re =A.split(" ")
result = sp_re[0]
for ch in sp_re:
    if len(ch)>len(result):
        result = ch
print(result)



