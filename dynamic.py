#LCS by dynamic programming
def getlcs(a,x):
    lcs=''
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j]=='diagonal':
                lcs+=x[i]
    print('Longest Common Subsequence -'+ lcs)

def longest_common_subsequence(x,y):
    len_x=len(x)
    len_y=len(y)
    s=[[0 for i in range(len_y+1)] for j in range(len_x+1)]
    a=[[0 for i in range(len_y+1)] for j in range(len_x+1)]
    x=' '+x
    y=' '+y

    for i in range(1,len_x+1):
        for j in range(1,len_y+1):
            if x[i]==y[j]:
                s[i][j]=s[i-1][j-1]+1
                a[i][j]='diagonal'

            elif s[i-1][j]>s[i][j-1]:
                s[i][j]=s[i-1][j]
                a[i][j]='horizontal'
            else:
                s[i][j] = s[i][j-1]
                a[i][j] ='vertical'

    getlcs(a,x)
#find the maximum profit for given weight
def createDictAndMaximumWeight():
    wdict=[]
    infile=open('knapsack.txt','r')
    for line in infile.readlines():
     p,w=[int(x) for x in line.split()]
     wdict.append((p,w))
    wdict.append((0,0))
    wdict.sort()
    print(wdict)
    for i in range(len(wdict)):
        print(wdict[i][1])
    print('Give the max weight for which object will be selected')
    m=int(input())
    return wdict,m

def knapsack_problem():
    wdict,m=createDictAndMaximumWeight()
    n=len(wdict)
    profitmatrix=[[0 for x in range(m+1)] for y in range(n)]
    for i in range(1,n):
        for w in range(1,m+1):
            if i-1 >= 0:
                p=profitmatrix[i-1][w]
            else :
                p=0

            if w-wdict[i][1]>=0 and i-1 >= 0:
                q=profitmatrix[i-1][w-wdict[i][1]]
            else:
                q=0

            profitmatrix[i][w]=max(p,q+wdict[i][0])

    print(profitmatrix)







if __name__=='__main__' :
    # longest_common_subsequence('abcde','bd')
    knapsack_problem()