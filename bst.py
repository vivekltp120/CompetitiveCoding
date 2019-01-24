#This is class for Tree Node
import random
class TNode(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def insert_in_bst(curr, data):
    if curr == None:
        new = TNode(data)
        curr=new
    elif data < curr.data:
        curr.left = insert_in_bst(curr.left,data)
    else:
        curr.right = insert_in_bst(curr.right,data)
    return curr
def getBST(n):
    root = None
    for x in range(n):
        data = random.randint(1, 10)
        print('%d---'%(data),end='---')
        root = insert_in_bst(root, data)
    return root

def displayBST(curr):
    if curr==None:
        return
    if curr.left!=None:
        displayBST(curr.left)
    print(curr.data,end='--')
    if curr.right!=None:
        displayBST(curr.right)

#modify the bst with the some of greater then element
nsum=0
def modify_bst(curr):
    global nsum
    if curr==None:
        return
    modify_bst(curr.right)
    nsum=curr.data+nsum
    curr.data=nsum
    modify_bst(curr.left)




if __name__=='__main__':
    bst=getBST(10)
    print('\n')
    displayBST(bst)
    print('\n-----Modified Binary Search Tree-----')
    modify_bst(bst)
    displayBST(bst)

