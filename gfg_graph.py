
# Driver Program


def creategraph(n, arr, graph):
    i = 0
    while i < 2 * n:
        graph[arr[i]].append(arr[i + 1])
        graph[arr[i + 1]].append(arr[i])
        i += 2
    # print(graph)


def dfs_visit(n, visit, graph, v):
    print(v,end=' ')
    visit[v] = True
    for i in graph[v]:
        if visit[i] == False:
            dfs_visit(n, visit, graph, i)
    # visit[v] = True
def dfs(n, visit, graph, s):
    # Code
    for x in graph.keys():
      if visit[x]==False:
        dfs_visit(n, visit, graph, x)





from collections import defaultdict

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(n, arr, graph)
        visit = [False] * (max(arr) + 1)
        dfs(n, visit, graph, 1)
        print('')
# Contributed By: Harshit Sidhwa



''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

# Your task is to complete this function
# Function should print DFS Traversal
# Graph(graph) is a defaultict of type List
# Starting vertex (s) is 1
# Need not print new Line
# n is no of edges
# visit is a boolean array initialized to False



