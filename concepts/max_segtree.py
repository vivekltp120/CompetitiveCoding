import math
global sroot
def  createSegTreetree(a,n):
    """
    Function to create a segment tree for range maximum query.
    The segment tree is built in a way that each node contains the maximum value
    in the segment of the array it represents.  
    The tree is built recursively, and the size of the tree is determined by the
    height of the tree, which is calculated based on the number of elements in the array.   
    The segment tree is stored in a global list `sroot`, where each index corresponds
    to a node in the tree. The root of the tree is at index 0, and the left and right children of a node at index `i` are at indices `2*i + 1` and `2*i + 2`, respectively.
    

    Parameters:
    a (list): The input array for which the segment tree is to be created.
    n (int): The number of elements in the input array.     

    Returns:
    None: The function modifies the global variable `sroot` to store the segment tree.
    The segment tree can then be used to efficiently answer range maximum queries on the array.
    The time complexity for building the segment tree is O(n), and the space complexity is O(n).
    The segment tree allows for efficient range maximum queries in O(log n) time.
    The segment tree can be used to find the maximum value in any subarray of the input array.
    The segment tree can also be used to update the value of an element in the array,
    which can be done in O(log n) time, although this function does not include that
    """    
    h=int(math.ceil(math.log2(n)))
    # print(h)
    global sroot
    sroot=[None for _ in range(int(math.pow(2,h+1)-1))]
    arrstart=0
    arrend=n-1
    segind=0
    segtreeUtil(a,arrstart,arrend,sroot,segind)
    # print(sroot)

def segtreeUtil(arr:list,arrstart:int,arrend:int,sroot:int,segind:int)-> int:
    """Function to build the segment tree recursively.
    This function is a utility function that builds the segment tree    
    Parameters:
    arr (list): The input array for which the segment tree is to be created.
    arrstart (int): The starting index of the segment of the array being processed.
    arrend (int): The ending index of the segment of the array being processed.
    sroot (list): The segment tree being built, stored as a list.
    segind (int): The index of the current node in the segment tree being built.

    Returns:
    int: The maximum value in the segment of the array represented by the current node.
    This function modifies the global variable `sroot` to store the maximum values in the segment tree.
    The time complexity for this function is O(n), where n is the number of elements in the input array.
    The space complexity is O(n) for storing the segment tree.
    The segment tree allows for efficient range maximum queries in O(log n) time.
    The segment tree can be used to find the maximum value in any subarray of the input
    array.
    The segment tree can also be used to update the value of an element in the array,
    which can be done in O(log n) time, although this function does not include that
    functionality.
    """
    if arrstart>arrend:
        return 0            
    mid=int(arrstart+arrend)/2

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


