__author__ = "Vivek"
__author_email__ = "vivekltp120@gmail.com"


# Kth Smallest Element


class Solution:

    def build_heap(self, arr):
        self.heap_size = len(arr) - 1
        n = len(arr)
        for i in range(n // 2, -1, -1):
            self.min_heapify(arr, i)

    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def min_heapify(self, arr, i):
        left = 2 * i + 1
        right = 2 * i + 2
        minimum = i
        if left <= self.heap_size and arr[i] >= arr[left]:
            minimum = left
        if right <= self.heap_size and arr[minimum] > arr[right]:
            minimum = right
        if minimum != i:
            self.swap(arr, i, minimum)
            self.min_heapify(arr, minimum)

    def kthSmallest(self, arr, k):
        self.build_heap(arr)
        for i in range(k):
            result = arr[0]
            self.swap(arr, 0, self.heap_size)
            self.heap_size -= 1
            self.min_heapify(arr, 0)
        return result

#Quick Sort
def quick(arr,p,r):
    if p<r:
        q=partition(arr,p,r)
        quick(arr,p,q-1)
        quick(arr,q+1,r)
def partition(arr,p,r):
    pivot=arr[r]
    j=p
    i=j-1
    while j<r:
        if arr[j]<pivot:
            i+=1
            arr[j],arr[i]=arr[i],arr[j]
        j+=1
    arr[i+1],arr[r]=arr[r],arr[i+1]
    return i+1     


def merge_sort(arr,strt_i,end_i):
    if strt_i<end_i:
        mid=(end_i+strt_i)//2
        merge_sort(arr,strt_i,mid)
        merge_sort(arr,mid+1,end_i)
        merge(arr,strt_i,mid,end_i)
        
        
        
def merge(arr,p,mid,q):
    i=0
    j=0
    k=p
    left_arr=arr[p:mid+1]
    right_arr=arr[mid+1:q+1]
    print(left_arr)
    print(right_arr)
    
    while i < mid-p+1  and j < q-mid:
        if left_arr[i]<= right_arr[j]:
            arr[k]=left_arr[i]
            i+=1
        else:
            arr[k]=right_arr[j]
            j+=1
        k+=1
    while i < mid-p+1:
        arr[k]=left_arr[i]
        i+=1
        k+=1
    while j < q-mid:
        arr[k]=right_arr[j]
        j+=1
        k+=1
    


if __name__=="__main__":
    arr=[3,4,5,1,2,8,7,9]
    
    # quick(arr,0,len(arr)-1)
    # print(arr)
    merge_sort(arr,0,len(arr)-1)
    print(arr)    

# contributed by RavinderSinghPB
if __name__ == '__main__':
    import random
    t = int(input())
    for tcs in range(t):
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.kthSmallest(arr, k))
    
    # quick(arr,0,len(arr)-1)
    # print(arr)
    merge_sort(arr,0,len(arr)-1)
    print(arr)       

