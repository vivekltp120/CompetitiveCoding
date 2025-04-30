# rotten oranges
def rotten(mat, n, m):
    rotq = []
    top = 0
    bottom = n - 1
    left = 0
    right = m - 1
    visited = set()
    for i in range(n):
        for j in range(m):
            if mat[i][j]==2:
                rotq.append((i, j))

    step = -1
    while rotq:
        step += 1
        rotsize = len(rotq)
        print(rotq)
        while rotsize > 0:

            temp = rotq.pop(0)
            if temp not in visited and mat[temp[0]][temp[1]]==2:
                if  temp[0] - 1 >= top and temp[0] - 1 <= bottom:
                    if mat[temp[0] - 1][temp[1]] == 1:
                        mat[temp[0] - 1][temp[1]] = 2
                        rotq.append((temp[0] - 1, temp[1]))
                if temp[0] + 1 >= top and temp[0] + 1 <= bottom:
                    if mat[temp[0] + 1][temp[1]] == 1:
                        mat[temp[0] + 1][temp[1]] = 2
                        rotq.append((temp[0] + 1, temp[1]))

                if temp[1] - 1 >= left and temp[1] - 1 <= right:
                    if mat[temp[0]][temp[1] - 1] == 1:
                        mat[temp[0]][temp[1] - 1] = 2
                        rotq.append((temp[0], temp[1] - 1))

                if temp[1] + 1 >= left and temp[1] + 1 <= right:
                    if mat[temp[0]][temp[1] + 1] == 1:
                        mat[temp[0]][temp[1] + 1] = 2
                        rotq.append((temp[0], temp[1] + 1))

            visited.add(temp)
            rotsize -= 1
    # print(mat)
    rflag=0
    for i in range(n):
        for j in range(m):
            if mat[i][j]==0  or mat[i][j]==2:
                continue
            else:
                rflag=1
                break

    if rflag==0:
        print(step)
    else:
        print(-1)



N = int(input())
for i in range(N):
    n, m = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    k=0
    mat=[[0 for x in range(m)] for y in range(n)]
    for i in range(n):
        for j in range(m):
            mat[i][j]=arr[k]
            k+=1
    rotten(mat, n, m)