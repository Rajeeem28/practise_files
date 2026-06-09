s = "data engineer"
sp_re= s.split(" ")
rev_result =" "
for ch in sp_re:
    # print(ch[::-1])
    rev_result += ch[::-1]+" "
print(rev_result)