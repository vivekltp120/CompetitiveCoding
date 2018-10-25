from itertools import permutations

a=str(432)
print(a)
per=permutations(a)
for x in per:
    x=''.join(x)
    if x<a:
       break


