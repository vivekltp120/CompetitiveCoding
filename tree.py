from collections import deque

#This is class for Tree Node
class TNode(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
#Tree
class Tree(object):
    def __init__(self):
        self.root=None
        return self.root

    def insert_into_tree(self,data):
        if self.root==None:
            newNode=TNode(data)
            self.root=newNode
        else:
            q=deque()
            q.append(self.root)
            x=q.popleft()
            child=TNode(data)
            while x!=None:
                if x.left:
                    q.append(x.left)
                else:
                    x.left=child
                    return
                if x.right:
                    q.append(x.right)
                else:
                    x.right=child
                    return
                x=q.popleft()
    def getRoot(self):
        return self.root

    def inorder(self):
        print('Recursive Inorder Traversal')
        temp=self.getRoot()
        self.inorderUtil(temp)

    def inorderUtil(self,root):
        if root==None:
            return
        self.inorderUtil(root.left)
        print(root.data)
        self.inorderUtil(root.right)

    #Preorder iteative
    def preorder(self):
        print('Iterative Preorder:')
        temp=self.getRoot()
        stack=deque()
        while True:
            while temp:
                print(temp.data)
                stack.appendleft(temp)
                temp=temp.left

            if stack.__len__()==0:
                return
            x=stack.popleft()

            if x.right is not None:
                temp=x.right







if __name__=='__main__':
    arr=[1,2,3,4,5,8,9,10]
    root=Tree()
    for x in arr:
        root.insert_into_tree(x)

    root.inorder()
    root.preorder()