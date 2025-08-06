#convert a string into array
def string_to_list(instr):
    mylist = [int(i) for i in instr.split()]
    return mylist


#input for geeksforgeeks
def inputgfg():
    N = int(input())
    for i in range(N):
        alen = int(input())
        arr = [int(x) for x in input().split()]
        yield arr

#input for geeksforgeeks
def input_subarray_max_gfg():
        alen, k = [int(x) for x in input().split()]
        arr = [int(x) for x in input().split()]
        return arr,k





#remove common in string and conatenate
def remove_common_concat():
    N = int(input())
    for i in range(N):
        s1 = input()
        s2 = input()

        # print(s2)
        hash=[]
        lists1=list(s1)
        lists2=list(s2)
        # for ch in lists2:
        #    hash.append(ch)
        for ch in lists1:
            if ch in lists2:
                c1=lists1.count(ch)
                c2=lists2.count(ch)
                while c1>0 or c2>0:
                    if c1>0:
                        lists1.remove(ch)
                        c1=c1-1
                    if c2>0:
                        lists2.remove(ch)
                        c2=c2-1

        if lists1 != None or lists2 != None :
            print(str(lists1+lists2))
        else:
            print('-1')


#leetcode-Find indices in a array to a given sum
def sum_of_two():
    k=int(input())
    arr=list(map(lambda x:int(x),[x for x in input().split()]))
    print(arr)
    hashmap={}
    for x in range(len(arr)):
        hashmap[arr[x]]=x

    for i in range(len(arr)):
        complement=k-arr[i]
        com_index=hashmap.get(complement)
        if com_index and com_index!=i:
            print( str(i)+" "+str(com_index))
            return
    return -1


#catalan number for the given number
def catalan_number(n):
    #first method by formula
    #C(n)=C(i)C(n-1-i)
    pass



#leaders in array
# code
def leader_array(arr):
    leader_group = []
    arr=usr_input()
    alen=len(arr)
    for i in range(len(arr)):
        leader = arr[i]
        for j in range(i, alen):
            if leader < arr[j]:
                leader = None
                break
        if leader:
            leader_group.append(leader)
    return ' '.join([str(x) for x in leader_group])

def usr_input():
  N = int(input())
  arr = [int(x) for x in input().split()]
  return arr


#stock buy and sell
def max_profit(stock):
    n=len(stock)
    stack=[]
    if n==1:
        return 'Stock price should be atleast for two days'
    pp=[]
    maxprof=0
    start=0
    end=None
    i=0
    while i<n:
        stack.append(stock[i])
        start=i
        end=None
        if stack[-1]>stock[i]:
            if maxprof>0 and end>0:
                pp.append((start,end))
            stack.pop()
            start=i
            end=-1
        else:
            if stock[i]-stack[-1]>maxprof:
                maxprof=stock[i]-stack[-1]
                end = i
                i += 1
                continue
        i+=1

    print(pp)




#find the longest subsequence for the given array
#Kadane Algorithm
def longest_subarray_of_sum(arr,k):
    si=0
    ei=0
    alen=len(arr)
    max_so_far=0
    subarr=[]
    maximum_sum=0
    while ei<alen:
        max_so_far+=arr[ei]
        if max_so_far>=maximum_sum:
            subarr.append(list(arr[si:ei+1]))
            maximum_sum=max_so_far
        ei+=1


#find the number of subarray of given multiplication
def subarry_for_mul(arr,k):
    subarr=[]
    mul=1
    for si in range(len(arr)):
        for ei in range(si,len(arr)):
            mul*=arr[ei]
            if mul==k:
                subarr.append(arr[si:ei+1])
        mul=1
    print(subarr)


# Most asked question in company interview from geeks for geeks
# stock by and sell
from collections import deque


def stock_buy_sell(arr):
    if len(arr)<=1:
        return 'Give at least two day stock price'
    n=len(arr)
    i=0
    buy=[]
    sell=[]
    stockstr=''
    while i<n-1:

        #find local minima
        while i<n-1 and arr[i]>=arr[i+1] :
            i+=1

        if i==n-1:
            break
        buy.append(i)
        i+=1

        #find local maxima
        while i<n and arr[i]>=arr[i-1]:
            i+=1
        sell.append(i-1)

    for i,j in zip(buy,sell):
        stockstr=stockstr+'('+str(i)+' '+str(j)+')'+' '
    print(stockstr.strip())


#tapping water
def tapping_water(arr):
    #create an array for finding the left max and right max including itself
    n=len(arr)
    left_max=[-1 for i in range(n)]
    right_max=[-1 for i in range(n)]
    right_max[n-1]=arr[n-1]
    left_max[0]=arr[0]
    for i in range(1,n):
        if arr[i]>=left_max[i-1]:
            left_max[i]=arr[i]
        else:
            left_max[i]=left_max[i-1]
    for i in range(n-2,-1,-1):
        if arr[i] >= right_max[i+1]:
            right_max[i]=arr[i]
        else:
            right_max[i]=right_max[i+1]

    collected_water=0
    for i in range(len(arr)):
        collected_water+=min(left_max[i],right_max[i])-arr[i]
    print(collected_water)


#pythagorian tirplet
def pythagorian(arr):
    n=len(arr)
    arr.sort()
    sqr=[x*x for x in arr]

    for i in range(n-1,-1,-1):
        a=sqr[i]
        for j in range(0,i):
            if (a-sqr[j]) in sqr:
                # print('Yes- (%d %d %d)'%(i,j,sqr.index(a-sqr[j])))
                print('Yes')
                return
    print('No')

#maximum increasing subsequence
def msis(arr):
    n = len(arr)
    mis = [arr[i] for i in range(n)]
    for i in range(1,n):
        for j in range(0, i):
            if arr[j] < arr[i] and mis[i] < mis[j] + arr[i]:
                mis[i] = mis[j] + arr[i]
    print(mis)
    print(arr)
    maxsum = max(mis)
    print(maxsum)

def equilibrium(arr):
    right_sum=sum(arr)
    left_sum=0
    for i in range(len(arr)):
        right_sum = right_sum - arr[i]
        if left_sum==right_sum:
            return i+1
        left_sum=left_sum+arr[i]
    return -1


#leaders in a array
def leaders(a):
    n=len(a)
    if n==1:
        return a[0]
    max_so_far=a[n-1]
    leaders=[]
    leaders.append(a[n-1])
    for i in reversed(range(n-1)):
        if a[i]>=max_so_far:
            leaders.append(a[i])
            max_so_far=a[i]
    return ' '.join([str(x)  for x in reversed(leaders)])


#tricky problem please look into logic
def subarray_maximum(a,k):
    n=len(a)
    if n<k:
        return -1
    curr_max=max(arr[0:k])
    i=1
    maxstr=str(curr_max)
    while i<=n-k:
        if arr[i-1]!=curr_max:
            if curr_max<=arr[i+k-1]:
                curr_max=arr[i+k-1]
            else:
                pass
        else:
            if arr[i-1]<=arr[i+k-1]:
                curr_max=arr[i+k-1]
            else:
                curr_max=max(arr[i:i+k])
        maxstr=maxstr+' '+str(curr_max)
        i+=1
    print(maxstr.strip())

#minplateform
# 1
# 65
# 1445 1709 124 1422 552 1413 1828 551 847 32 1347 1131 1320 553 1710 825 1658 623 244 643 740 2 233 1327 1408 1543 59 1023 525 323 628 921 1740 1317 1807 811 146 840 1216 931 1910 633 817 1506 1800 935 242 1615 1435 1711 1515 328 1837 301 1801 757 1337 1620 853 1917 1316 1325 1355 1908 1111
# 1519 1759 2000 1431 1522 1445 1847 558 2117 1600 1348 1315 2100 2100 1735 1700 2100 644 341 1048 1535 1335 1721 1442 1837 1734 2238 1048 1400 2346 1641 958 1829 2300 1826 1018 855 844 1224 1000 1958 645 826 1740 2151 955 527 1633 1453 1718 2212 810 1921 400 2000 2102 1345 1627 1200 1928 1355 1400 1357 1924 2100


#input for min plateform
def min_plateform():
    a=[int(x) for x in input().split()]
    d=[int(x) for x in input().split()]
    return a,d
#wrong implementation for repeated arrival and departure time.Do later for right logic
def minplateform(a,d):
    min_plateform=1
    plateform_need=1
    a.sort()
    d.sort()
    n=len(a)
    j=0
    i=1
    while i<n and j<n:
         if a[i]<=d[j]:
            plateform_need+=1
            if min_plateform<plateform_need:
                min_plateform=plateform_need
            i+=1
         else:
             plateform_need-=1
             j+=1

    print(min_plateform)



# kth largest element in the stream execution time more than expected
def input_kthlargest():
    N =int(input())
    for n in range(N):
        k,alen=[int(x) for x in input().split()]
        a=[int(x) for x in input().split()]
        kthlargest(a,k)
def kthlargest(arr,k):
    stream=[-1 for i in range(k)]
    streamstr=''
    for i in range(0,len(arr)):
        if arr[i]<=stream[-1]:
            pass
        else:
            stream.pop()
            stream.append(arr[i])
            stream.sort(reverse=True)
        streamstr = streamstr + ' ' + str(stream[-1])
        print(streamstr.strip())

#Spirally travesing of an array
def spiraltraverse(mat,m,n):
    left=0
    right=n-1
    top=0
    bottom=m-1
    spiral=''
    while left<right and top<bottom:
        #left to right
        for i in range(left,right):
            spiral=spiral+' '+str(mat[top][i])
        for i in range(top,bottom):
            spiral=spiral+' '+str(mat[i][right])
        for i in range(right,left,-1):
            spiral=spiral+' '+str(mat[bottom][i])
        for i in range(bottom,top,-1):
            spiral=spiral+' '+str(mat[i][left])
        top+=1
        bottom-=1
        left+=1
        right-=1
    if top==bottom and left<=right:
        for i in range(left,right+1):
            spiral=spiral+' '+str(mat[top][i])
    elif left==right and top<=right:
        for i in range(top,bottom+1):
            spiral=spiral+' '+str(mat[i][left])
    else:
        pass
    print(spiral.strip())

def spiral_input():
    N = int(input())
    for n in range(N):
        m, n = [int(x) for x in input().split()]
        arr = [int(x) for x in input().split()]
        mat = [[-1 for i in range(n)] for j in range(m)]
        k = 0
        for i in range(m):
            for j in range(n):
                mat[i][j] = arr[k]
                k += 1
        spiraltraverse(mat, m, n)

#find the element which is greater then it's left and smaller then it's right
def lsrg(arr):
    n = len(arr)
    left_max = [-1 for i in range(n)]
    left_max[0] = arr[0]
    right_min = [-1 for i in range(n)]
    right_min[n - 1] = arr[n - 1]
    for i in range(1, n):
        if arr[i - 1] >= left_max[i - 1]:
            left_max[i] = arr[i - 1]
        else:
            left_max[i] = left_max[i - 1]

    for i in range(n - 2, -1, -1):
        if arr[i + 1] <= right_min[i + 1]:
            right_min[i] = arr[i + 1]
        else:
            right_min[i] = right_min[i + 1]

    for i in range(n):
        if arr[i] >= left_max[i] and arr[i] <= right_min[i] and i != n - 1 and i != 0:
            print(arr[i])
            return
    print('-1')

#find a pivot element in a array
def find_pivot(arr,l,r):

    #return condition
    if l==r:
        return l
    if l>r:
        return -1
    mid=(l+r)//2

    if mid<r and arr[mid]>arr[mid+1]:
        return mid
    elif mid>l and arr[mid]<arr[mid-1]:
        return mid-1
    elif arr[l]<arr[mid]:
         return find_pivot(arr,mid+1,r)
    return find_pivot(arr,l,mid-1)

#Kth largest element of the stream
def swap(a, x, y):
    temp = a[x]
    a[x] = a[y]
    a[y] = temp


def minheapify(a, i):
    l = 2 * i + 1
    r = 2 * i + 2
    minimum = i
    if l < heapsize and a[l] < a[i]:
        minimum = l
    if r < heapsize and a[r] < a[minimum]:
        minimum = r
    if i != minimum:
        swap(a, i, minimum)
        minheapify(a, minimum)


def build_min_heap(a, k):
    global heapsize
    heapsize = k
    i = n // 2
    while i > 0:
        minheapify(a, i)
        i -= 1


def kthlargest(a, k):
    mystr = ''
    n = len(a)
    minha = [-1 for x in range(k)]

    # build a min heap on minha
    build_min_heap(minha, k)
    j = k
    while j < n:
        if a[j] < minha[0]:
            mystr = mystr + ' ' + str(minha[0])
            continue
        else:
            minha[0] = a[j]
            minheapify(minha, 0)
            mystr = mystr + ' ' + str(minha[0])
        j += 1
    print(mystr.strip())


def kthlargestinput():
    global n, arr
    N = int(input())
    for i in range(N):
        k, n = [int(x) for x in input().split()]
        arr = [int(x) for x in input().split()]
        kthlargest(arr, k)



def all_sub_array_of_given_sum(a,mysum):
    n=len(a)
    result=[]
    if n==0:
       print('Size 0')
       return
    currsum=a[0]
    start=0
    end=1
    while end<n or currsum>mysum:
        while currsum>mysum and start!=end:
            currsum-=a[start]
            start+=1
        if currsum==mysum:
            result.append((start,end-1))

        if end!=n:
            currsum+=a[end]
            end+=1
    print(result)


# User function template for Python 3

class Solution:
    def majorityElement(self, arr):
        # Your code here
        i = 1
        count = 1
        major = arr[0]
        while i < len(arr):
            if arr[i] == major:
                count += 1
            else:
                count -= 1
            if count == 0:
                major = arr[i]
                count += 1
            i += 1

        if count >= 1:
            tem = 0
            for i in range(len(arr)):
                if arr[i] == major:
                    tem += 1
            if tem > (len(arr) / 2):
                return major
            else:
                return -1
        else:
            return -1


# {
# Driver Code Starts
# Initial Template for Python 3

import math
from sys import stdin
def memain():
    with open("input_majority.txt") as fp:
        T=int(fp.readline())
        while (T > 0):
            input = fp.readline()
            A = [int(x) for x in input.strip().split()]
            obj = Solution()
            print(obj.majorityElement(A))
            T -= 1




# } Driver Code Ends



if __name__=='__main__':

    #subarray of given sum
    a=[1,1,1,1,2,1]
    # mysum=3
    # all_sub_array_of_given_sum(a,mysum)
    memain()



    # code for kth largest element input
    # kthlargestinput()

    #find pivot
    # for a in inputgfg():
    #     print(find_pivot(a,0,len(a)-1))

    #elment with minimum in left and maximum on right
    # for a in inputgfg():
    #     lsrg(a)

    #spiral
    # spiral_input()

    #kth largest element in stream
    # input_kthlargest()


    #min plateform
    # N=int(input())
    # for n in range(N):
    #     trains=int(input())
    #     a,d=min_plateform()
    #     minplateform(a,d)


    #maximum of all subarray
    # N=int(input())
    # for n in range(N):
    #     arr,k=input_subarray_max_gfg()
    #     subarray_maximum(arr,k)



    #leaders
    # for a in inputgfg():
    #     print(leaders(a)+'\n')


    #Equilibrium




    # maximum increasing subsequence
    # instr='468 335 501 170 725 479 359 963 465 706 146 282 828 962 492 996 943 828 437 392 605 903 154 293 383 422 717 719 896 448 727 772 539 870 913 668 300 36 895 704 812 323'
    # arr=string_to_list(instr)
    # msis(arr)



    # pythagorian
    # a=[3, 2, 4, 6, 5]
    # pythagorian(a)



    #rain tapping
    # a=[7, 4, 0, 9]
    # tapping_water(a)



    # stock buy and sell clear concept
    stock1 = [100, 180, 260, 310, 40, 535, 695]
    stock2 = [23, 13, 25, 29, 33, 19, 34, 45, 65, 67]
    stock3 = [886, 2777, 6915, 7793, 8335, 5386, 492, 6649, 1421, 2362, 27, 8690, 59, 7763, 3926, 540, 3426, 9172, 5736,
              5211, 5368, 2567, 6429, 5782, 1530, 2862, 5123, 4067, 3135, 3929, 9802, 4022, 3058, 3069, 8167, 1393,
              8456, 5011, 8042, 6229, 7373, 4421, 4919, 3784, 8537, 5198, 4324, 8315, 4370, 6413, 3526, 6091, 8980,
              9956, 1873, 6862, 9170, 6996, 7281, 2305, 925, 7084, 6327, 336, 6505, 846, 1729, 1313, 5857, 6124, 3895,
              9582, 545, 8814, 3367, 5434, 364, 4043, 3750, 1087, 6808, 7276, 7178, 5788]
    stock4 = [5403, 2651, 2754, 2399, 9932, 5060, 9676, 3368, 7739, 12, 6226, 8586, 8094, 7539, 795, 570, 1434, 378,
              7467, 6601, 97, 2902, 3317, 492, 6652, 756, 7301, 280, 4286, 9441, 3865, 9689, 8444, 6619, 8440, 4729,
              8031, 8117, 8097, 5771, 4481, 675, 709, 8927, 4567, 7856, 9497, 2353, 4586, 6965, 5306, 4683, 6219, 8624,
              1528, 2871, 5732, 8829, 9503, 19, 8270, 3368, 9708, 6715, 6340, 8149, 7796, 723, 2618, 2245, 2846, 3451,
              2921, 3555, 2379, 7488, 7764, 8228, 9841, 2350, 5193, 1500, 7034, 7764, 124]

    # stock_buy_sell(stock4)



    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    # longest_subsequence(arr)
    # subarry_for_mul(arr,8)
    # sum_of_two()
    # remove_common_concat()
    # arr = usr_input()
    # max_profit(arr)











