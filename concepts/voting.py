__author__ = "Vivek"
__author_email__ = "vivekltp120@gmail.com"

from collections import defaultdict
import heapq
candidates=[]
fp=open("candidate_voting.txt", 'r')
num_candidate=int(fp.readline())
#name of the candidate
for i in range(num_candidate):
    candidates.append("candidate_"+str(i))

candidate_voting={}
for candidate in candidates:
    candidate_voting[candidate]=0


#taking the votes from the colleague
for line in fp.readlines():
    print(line)
    votes=[int(x) for x in line.split(" ")]
    for vote in range(len(votes)):
         candidate_voting["candidate_"+str(vote)]=candidate_voting["candidate_"+str(vote)]+votes[vote]

sort_list=list(candidate_voting.items())

# method to sort the array
result=sorted(sort_list,key=lambda x:x[1],reverse=True)
result_smallest=heapq.nsmallest(6,candidate_voting.items(),key=lambda x:x[1])
result_largest=heapq.nlargest(6,candidate_voting.items(),key=lambda x:x[1])
print(result_smallest)
print(result_largest)








