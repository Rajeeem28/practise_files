s1 = "abcde"
s2 = "cdeab"
output = s1 + s1

if len(s1) == len(s2) and s2 in output:
    print("true",output)
else:
    print("false")

