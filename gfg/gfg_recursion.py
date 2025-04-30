# code for input


def floodfill(m,visited, r, c, x, y, k):
    if x < 0 or x > r - 1 or y < 0 or y > c - 1:
        return
    sc = m[x][y]
    visited[x][y]=True
    if x - 1 >= 0:
        if m[x - 1][y] == sc and visited[x-1][y]!=True:
            floodfill(m,visited, r, c, x - 1, y, k)
    if x + 1 < r :
        if m[x + 1][y] == sc and visited[x+1][y]!=True:
            floodfill(m,visited, r, c, x + 1, y, k)
    if y - 1 >= 0:
        if m[x][y - 1] == sc and visited[x][y-1]!=True:
            floodfill(m,visited, r, c, x, y - 1, k)
    if y + 1 < c:
        if m[x][y + 1] == sc and visited[x][y+1]!=True:
            floodfill(m,visited, r, c, x, y + 1, k)
    m[x][y] = k


def print_matrix(m, r, c):
    mstr = ''
    for i in range(r):
        for j in range(c):
            mstr = mstr + ' ' + str(m[i][j])
    print(mstr.strip())


def floodfill_input():
    N = int(input())
    for i in range(N):
        r, c = [int(x) for x in input().split()]
        arr = [int(x) for x in input().split()]
        x, y, k = [int(x) for x in input().split()]
        mat = [[-1 for x in range(c)] for y in range(r)]
        visited = [[False for x in range(c)] for y in range(r)]
        p = 0
        for i in range(r):
            for j in range(c):
                mat[i][j] = arr[p]
                p += 1
        floodfill(mat,visited,r,c,x,y,k)
        print_matrix(mat, r, c)


if __name__=='__main__':
    floodfill_input()

