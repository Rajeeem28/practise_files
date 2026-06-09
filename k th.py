#  Q6 / Q20 / Q24. List rotation — Rotate a list right by k positions. Example: [1,2,3,4,5], k=2 →
# [4,5,1,2,3].

input = [4,5,1,2,3]
k= 5
k=k%len(input)
re = input[-k:]+input[:-k]
print(re)