class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Tree(object):
    def __init__(self):
        self.root=None
        return self.root

    def insert_into_tree(self,data):
        if self.root==None:
            newNode=Node(data)
            self.root=newNode

        else:


