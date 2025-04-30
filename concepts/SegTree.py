import math


# segtree for minimum range queries
class SegTree(object):

    def __init__(self, arr):
        self.segroot = self.create_segtree(arr)

    def create_segtree(self, arr):
        size = len(arr)
        # for height of the tree
        height = math.ceil(math.log2(size))
        # Allocate the memory for segment tree
        nodeInSegTree = int((math.pow(2, height + 1)) - 1)
        # print(nodeInSegTree)
        segroot = [None] * nodeInSegTree
        self.seg_util(arr, 0, size - 1, segroot, 0)
        return segroot

    def seg_util(self, arr, sa, ea, segroot, ss):
        mid = int(sa + ((ea - sa) / 2))
        if sa == ea:
            segroot[ss] = arr[sa]
            return arr[sa]
        else:
            # put the logic here for any type of problem like for range query or minimum element of right and left
            segroot[ss] = self.seg_util(arr, sa, mid, segroot, ss * 2 + 1) + self.seg_util(arr, mid + 1, ea, segroot,
                                                                                         ss * 2 + 2)
            return segroot[ss]

    def getSegRoot(self):
        return self.segroot

    def rangeQuery(self, arr, qs, qe):
        if qs < 0 or qe > (len(arr) - 1) or qs > qe:
            return -1
        segroot = self.getSegRoot()
        return self.rangeQueryUtil(segroot, 0, len(arr) - 1, qs, qe, 0)

    def rangeQueryUtil(self, segroot, ss, se, qs, qe, si):
        if (qs <= ss and qe >= se):
            return segroot[si]

        if (se < qs or ss > qe):
            return 0

        mid = int(ss + (se - ss) / 2)
        return self.rangeQueryUtil(segroot, ss, mid, qs, qe, si * 2 + 1) + self.rangeQueryUtil(segroot, mid + 1, se, qs,
                                                                                               qe, si * 2 + 2)

def seg_tree_v1(arr):
    global st
    n=len(arr)

    size_ss=math.pow(2, math.ceil(math.log2(n))+1)
    print(size_ss)
    st=[None for _ in range(int(size_ss))]
    print(st)
    create_ss(0,0,4)
    print(st)


def create_ss(node, l,r):
    if l==r:
        st[node]=arr[l]
        return

    mid=(l+r)//2
    print(mid)
    create_ss(node*2+1,l,mid)
    create_ss(node*2+2,mid+1,r)
    st[node]=st[node*2+1]+st[node*2+2]

def query(node,al,ar,l,r):
    # global arr,st
    if r<al or ar<l:
        return 0
    if l<=al and ar<=r:
        return st[node]
    mid=(al+ar)//2
    return query(node*2+1,al,mid,l,r)+ query(node*2+2,mid+1,ar,l,r)

def update(node,al,ar,ul,ur,value):
    if ur<al or ar<ul:
        return 0
    if al==ar:
        arr[al] += value
        st[node] += value
        return
    mid=(al+ar)//2
    update(node*2+1,al,mid,ul,ur,value)
    update(node*2+2,mid+1,ar,ul,ur,value)
    print(st)
    print(arr)
    st[node]=st[node*2+1]+st[node*2+2]













# driver program
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    # root = SegTree(arr)
    # sum = root.rangeQuery(arr, 0, 3)
    # print(sum)
    seg_tree_v1(arr)
    print(query(0,0,4,3,4))
    update(0,0,4,2,4,10)
    print(query(0,0,4,3,4))


