s = "Apache Spark Data Engineering"
sp_re = s.split(" ")
print(sp_re)
result =sp_re[0]

for ch in sp_re:
    if len(ch)>len(result):
        result = ch
print(result)