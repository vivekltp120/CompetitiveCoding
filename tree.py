from collections import deque
import math

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
        # return self.root



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
        print('Recursive Inorder Traversal:',end=' ')
        temp=self.getRoot()
        self.inorderUtil(temp)



    def inorderUtil(self,root):
        if root==None:
            return
        self.inorderUtil(root.left)
        print(root.data,end='-->')
        self.inorderUtil(root.right)

    def inorderIterative(self):
        print("Iterative For Inorder",end=' ')
        stack=deque()
        temp=self.getRoot()
        while True:

            while temp!=None:
                stack.append(temp)
                temp=temp.left

            if len(stack)==0:
                break

            x = stack.pop()
            print(x.data)
            if x.right!=None:
                temp=x.right
            else:
                temp=None





    #Preorder iteative
    def preorder(self):
        print('Iterative Preorder:',end=' ')
        temp=self.getRoot()
        stack=deque()
        while True:
            while temp:
                print(temp.data,end='-->')
                stack.append(temp)
                temp=temp.left

            if stack.__len__()==0:
                return
            x=stack.pop()

            if x.right is not None:
                temp=x.right

    #postorder


    def iterative_postorder(self):
        temp=self.getRoot()
        print(temp)
        stack=[]
        # stack.append(temp)
        print("Iterative postorder traversal:")
        while True:

            while temp!=None:
                stack.append(temp)
                temp=temp.left

            print([x.data for x in stack])
            if len(stack)==0:
                break

            x=stack.pop()
            print(x.data)
            if x.right!=None and stack[-1].data!=x.data:
                stack.append(x)
                temp=x.right

            else:
                print(x.data)
                temp=None

#difference of odd even level sum in tree
    def odd_even_level_diff(self):
        Q=[]
        temp=self.getRoot()
        Q.append(temp)
        level=0
        diff=0
        odd_sum=0
        even_sum=0
        while len(Q)!=0:
            size=len(Q)
            level+=1
            while size>0:
                t=Q.pop(0)
                if level%2==0:
                    even_sum+=t.data
                else:
                    odd_sum+=t.data
                if t.left!=None:
                    Q.append(t.left)
                if t.right!=None:
                    Q.append(t.right)

                size-=1
        print(int(math.fabs(even_sum-odd_sum)))
        return math.fabs(even_sum-odd_sum)
    def recursive_odd_even_diff(self,root):

        if root==None:
            return 0

        return root.data -(self.recursive_odd_even(root.left)+self.recursive_odd_even(root.right))


    #find the maximum sum in level
    def max_of_level(self):
        print('Maximum sum in all the level is-',end=' ')
        queue=[]
        max_sum_level=-1
        temp=self.getRoot()
        queue.append(temp)
        odd_sum=0
        even_sum=0
        level=0
        max_sum=0
        while len(queue)!=0:
            size=len(queue)
            level_sum=0
            while size>0:
                qnode=queue.pop(0)
                level_sum+=qnode.data
                if qnode.left!=None:
                    queue.append(qnode.left)
                if qnode.right!=None:
                    queue.append(qnode.right)
                size-=1
            print('level sum '+str(level_sum))
            if level_sum>=max_sum:
                max_sum=level_sum
                max_sum_level=level
            level+=1
        print('max_sum %d for the level %d'%(max_sum,max_sum_level))
        return max_sum

    #Zigzag Order
    def zigzag_order(self):
        print('\nZigzag order--')
        q=deque()
        temp=self.getRoot()
        q.append(temp)
        level=0
        while len(q)>0:
            size=len(q)
            while size>0:

                if level%2!=0:
                    qnode = q.popleft()

                    if qnode.left != None:
                        q.append(qnode.left)
                    if qnode.right != None:
                        q.append(qnode.right)
                else:
                    qnode=q.pop()
                    if qnode.right != None:
                        q.appendleft(qnode.right)
                    if qnode.left != None:
                        q.appendleft(qnode.left)

                print(qnode.data,end='-->')
                size-=1
            level+=1

    # give or print the vertical order
    def vertical_hd(self):
          print('\nVertical Order:',end=' ')
          root=self.getRoot()
          self.hdmap = {}
          self.VerticalOrder(root,hddistancefromroot=0)
          # print(self.hdmap)
          sortedhd=sorted(self.hdmap.items(),key=lambda v:v[1])
          # print(sortedhd)
          print('\n')
          prev_kval=None
          subarr=[]
          for key,value in sortedhd:
              if prev_kval==value:
                 subarr.append(key.data)
              else:
                 if len(subarr)>0:
                  print(' '.join([str(x) for x in subarr]))
                 subarr.clear()
                 subarr.append(key.data)
              prev_kval=value

    def VerticalOrder(self,root,hddistancefromroot):
        if root==None:
            return
        self.hdmap[root]=hddistancefromroot
        self.VerticalOrder(root.left,hddistancefromroot-1)
        print(root.data,end='-->')
        self.VerticalOrder(root.right,hddistancefromroot+1)

    #top view
    def topview(self,root,hddistancefromroot):
        self.VerticalOrder(root,hddistancefromroot)







if __name__=='__main__':
    arr=[1,2,3,4,5,6,7]
    root=Tree()
    for x in arr:
        root.insert_into_tree(x)
    # root.inorder()
    # root.preorder()
    # root.inorderIterative()
    root.iterative_postorder()
    # root.odd_even_level_diff()
    # root.max_of_level()
    # root.zigzag_order()
    # root.vertical_hd()