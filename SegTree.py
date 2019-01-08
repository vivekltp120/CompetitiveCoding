import math
#segtree for minimum range queries
class SegTree(object):

    def __init__(self,arr):
        self.segroot=self.createSegTree(arr)

    def createSegTree(self,arr):
        size=len(arr)
        #for height of the tree
        height=math.ceil(math.log2(size))
        #Allocate the memory for segment tree
        nodeInSegTree=int((math.pow(2,height+1))-1)
        # print(nodeInSegTree)
        segroot=[None]*nodeInSegTree
        self.segUtil(arr,0,size-1,segroot,0)
        return segroot
    def segUtil(self,arr,sa,ea,segroot,ss):
        mid =int(sa+((ea-sa)/2))
        if sa==ea:
            segroot[ss]=arr[sa]
            return arr[sa]
        else:
            #put the logic here for any type of problem like for range query or minimum element of right and left
            segroot[ss]=self.segUtil(arr,sa,mid,segroot,ss*2+1)+self.segUtil(arr,mid+1,ea,segroot,ss*2+2)
            return segroot[ss]
    def getSegRoot(self):
        return self.segroot


    def rangeQuery(self,arr,qs,qe):
        if qs<0 or qe>(len(arr)-1) or qs>qe:
            return -1
        segroot=self.getSegRoot()
        return self.rangeQueryUtil(segroot,0,len(arr)-1,qs,qe,0)

    def rangeQueryUtil(self,segroot,ss,se,qs,qe,si):
        if (qs <= ss and qe >= se):
            return segroot[si]


        if (se < qs or ss > qe):
            return 0

        mid=int(ss+(se-ss)/2)
        return self.rangeQueryUtil(segroot,ss,mid,qs,qe,si*2+1)+self.rangeQueryUtil(segroot,mid+1,se,qs,qe,si*2+2)


#driver program
if __name__=='__main__':
    arr=[1,2,3,4,5]
    root=SegTree(arr)
    sum=root.rangeQuery(arr,0,3)
    print(sum)
