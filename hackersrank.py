#find the sum of submatrix

def createMatrix(file,n,m):
    matrix=[[None for x in range(m)] for y in range(n)]
    i=0
    for line in file.readlines():
        matrix[i]=list(map(int,line.split()))
        i+=1
    return matrix
def sum_of_sum_matrix(matrix,k):
    print('In sum of matrix'+str(len(matrix)))
    n=len(matrix)
    m=len(matrix[0])
    for i in range(n-k+1):
        for j in range(m-k+1):

            for p in range(i,i+k):
                for q in range(j,j+k):
                    sum=matrix[p][q]
            mid_i=i+int(k/2)
            sum-=(matrix[mid_i][j]+matrix[mid_i][j+k-1])
            print(sum)

if __name__=='__main__':
    infile=open('mat_input.txt','r')
    m=createMatrix(infile,6,6)
    sum_of_sum_matrix(m,3)
