# 17. Missing number in first n natural numbers — Input: [3,7,1,2,8,4,5], n=8 → Output: 6.
Input =[3,7,1,2,8,4,5]
n= 8
aactual_sum = sum(Input)
print(aactual_sum)
expected_sum = n*(n+1)//2
print(expected_sum)

result =expected_sum-aactual_sum
print(result)