import math
global sroot
def  createSegTreetree(a,n):
    h=int(math.ceil(math.log2(n)))
    # print(h)
    global sroot
    sroot=[None for _ in range(int(math.pow(2,h+1)-1))]
    arrstart=0
    arrend=n-1
    segind=0
    segtreeUtil(a,arrstart,arrend,sroot,segind)
    # print(sroot)

def segtreeUtil(arr,arrstart,arrend,sroot,segind):
    mid=int(arrstart+(arrend-arrstart)/2)

    if arrstart==arrend:
        sroot[segind]=arr[arrstart]

    else:
        sroot[segind]=max(segtreeUtil(arr,arrstart,mid,sroot,segind*2+1),
        segtreeUtil(arr,mid+1,arrend,sroot,segind*2+2))
    return sroot[segind]



def rangeQuery(arr,qs,qe):
    createSegTreetree(arr,len(arr))
    # print(sroot)
    result=rangeQueryUtils(arr,qs,qe,0,len(arr)-1,sroot,0)
    print(result)

def rangeQueryUtils(arr,qs,qe,startind,endind,sroot,segind):

    if startind>=qs and qe>=endind:
        return sroot[segind]


    if qe<startind or endind<qs:
        return 0

    mid=int(startind+(endind-startind)/2)

    return max(rangeQueryUtils(arr,qs,qe,startind,mid,sroot,segind*2+1),rangeQueryUtils(arr,qs,qe,mid+1,endind,sroot,segind*2+2))


if __name__=='__main__':
    a=[2,4,5,6,1,2,3,1,7,8,9]
    # createSegTreetree(a,len(a))max_segtree.py:40
    rangeQuery(a,2,8)


