#LCS by dynamic programming
def getlcs(a,x):
    lcs=''
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j]=='diagonal':
                lcs+=x[i]
    print('Longest Common Subsequence -'+ lcs)

def longest_common_subsequence(x,y):
    print('Longest Common Subsequence:')
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
    print('Knapsack Problem:')
    wdict=[]
    infile=open('knapsack.txt','r')
    for line in infile.readlines():
        p,w=[int(x) for x in line.split()]
        wdict.append((p,w))
    wdict.append((0,0))
    wdict.sort()
    print(wdict)
    for i in range(len(wdict)):
        print(wdict[i][1],end=' ')
    print('Give the max weight for which object will be selected')
    m= 8#int(input())
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
                q=profitmatrix[i-1][w-wdict[i][1]]+wdict[i][0]
            else:
                q=0

            profitmatrix[i][w]=max(p,q)

    print(profitmatrix)
#Matrix chain multiplication
def matrix_chain_multiplication():
    print('Matrix Chain Multiplication:')
    mat=['5*4','4*6','6*2','2*7']
    d=[]
    mlen=len(mat)
    m=[[0 for x in range(mlen+1)] for y in range(mlen+1)]
    s=[[0 for x in range(mlen+1)] for y in range(mlen+1)]
    for x in mat:
        d.extend([int(y) for y in x.split('*') if int(y) not in d])
    print('dimension-'+str(d))

    for i in range(1,mlen+1):
        for j in range(1,mlen+1):
            temp={}
            for k in range(i,j):
                temp[m[i][k]+m[k+1][j]+d[i-1]*d[j]*d[k]]=k

            if temp:
                m[i][j]=min(temp)
                s[i][j]=temp[min(temp)]
    print('Order of matrix is:',end='')
    getMatrix(s,1,4)
def getMatrix(s,i,j):
    if i==j:
        return
    getMatrix(s, i, s[i][j])
    getMatrix(s, s[i][j] + 1, j)
    print('A%d*'%(s[i][j]),end='')


# coin sum dynamic

def coin_sum(a, s):
    t = [[-1 for x in range(s + 1)] for y in range(len(a))]

    for j in range(s + 1):
        t[0][j] = 1
    for i in range(len(a)):
        t[i][0] = 1
    for i in range(1, len(a)):
        for j in range(s + 1):
            if j < a[i]:
                t[i][j] = t[i - 1][j]

            else:
                if (j - a[i]) >= 0:
                    t[i][j] = t[i - 1][j] + t[i][j - a[i]]
                else:
                    t[i][j] = t[i - 1][j]
            print(t)

    return t[len(a) - 1][s]


def input_coin_sum():
    N = int(input())
    for i in range(N):
        alen = int(input())
        arr = [int(x) for x in input().split()]
        s = int(input())
        print(coin_sum(arr, s))



if __name__=='__main__' :
    # longest_common_subsequence('abcde','bd')
    # knapsack_problem()
    # matrix_chain_multiplication()
    input_coin_sum()
