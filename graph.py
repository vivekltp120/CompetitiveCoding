from collections import defaultdict

#graph class to represent a graph

class graph:
    #constructor for the graph
    def __init__(self,adjacencylist):
        self.adlist=defaultdict(list)
    #create a adjacency list for the given graph
    def add_edge(self,u,v):
        self.adlist[u].append(v)

    #implement the BFS for the graph
    def BFS(self,adjlist):
        self.initialize_vertex(adjlist)
        start=adjlist[0]
        self.initialize_start_vertex(start)
        q=[]
        q.append(start)
        vertex=q.pop()
        while vertex:
            for x in adjlist[vertex]:
                if x.color=='white':
                    q.append(x)
            vertex.color='grey'
            vertex=q.pop()


    def initialize_vertex(self, adjlist):
        for x in adjlist:
            adjlist[x].color = 'white'

    def initialize_start_vertex(self,adjlist,start):
        adjlist[start].color='grey'




