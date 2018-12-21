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



if __name__=='__main__' :
    longest_common_subsequence('abcde','bd')