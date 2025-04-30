from collections import deque
import math
import random

memoryQ=deque()

referArr={}
print(referArr)

for x in [random.randrange(1,10) for _ in range(10)]:
   print('x-%d'%(x))
   if x in referArr:
       ind=referArr.get(x)
       print('ind %d x %d'%(ind,x))
       memoryQ.remove(x)
       memoryQ.appendleft(x)
   else:
       # print(len(memoryQ))
       if len(memoryQ)>=3:
           referArr.pop(memoryQ.pop())
       memoryQ.appendleft(x)

   for i in range(len(memoryQ)):
     referArr.__setitem__(memoryQ[i],i)
   print(referArr)
   print(memoryQ)

