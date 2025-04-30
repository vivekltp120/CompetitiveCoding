
#Min_Heap
class heap(object):

     def __init__(self,arr,type):
         self.arr=arr
         self.type=type
         self.heap_size=len(arr)
     def  build_heap(self):
         n =len(self.arr)
         type=self.type
         i = int((n-1)/2)
         if type=='min_heap':
            while i >=0:
                self.minheapify(self.arr,i)
                i-=1

         else:
            while i >= 0:
                self.maxheapify(self.arr, i)
                i-=1
         return arr

     def swap(self,arr,i,j):
         temp=arr[i]
         arr[i]=arr[j]
         arr[j]=temp

     def maxheapify(self,arr,i):
         left=2*i+1
         right=2*i+2
         largest=i

         if left<=self.heap_size-1 and arr[left]>=arr[i]:
             largest=left
         if right <= self.heap_size-1 and arr[right] > arr[largest]:
             largest = right
         if largest!=i:
             self.swap(arr,i,largest)
             self.maxheapify(arr,largest)

     def extract_max(self):
         if self.heap_size==0:
             return
         arr=self.arr
         max_value=arr[0]
         self.swap(arr,0,self.heap_size-1)
         self.heap_size-=1
         self.maxheapify(arr,0)
         return max_value

     def minheapify(self, arr, i):
         left = 2 * i + 1
         right = 2 * i + 2
         smallest = i

         if left <= self.heap_size - 1 and arr[left] <= arr[i]:
             smallest = left
         if right <= self.heap_size - 1 and arr[right] < arr[smallest]:
             smallest = right
         if smallest != i:
             self.swap(arr, i, smallest)
             self.minheapify(arr, smallest)

     def extract_min(self):
         if self.heap_size == 0:
             return
         arr = self.arr
         min_value = arr[0]
         self.swap(arr, 0, self.heap_size - 1)
         self.heap_size -= 1
         self.minheapify(arr, 0)
         return min_value


#driver function

if __name__=="__main__":
    arr=[8,5,7,1,4,2,5,9]
    myheap=heap(arr,'maxheap')
    arr=myheap.build_heap()
    for i in range(len (arr)):
      print(myheap.extract_max(),end=' ')
    print('\n')
    myminheap = heap(arr, 'min_heap')
    arr = myminheap.build_heap()
    for i in range(len(arr)):
        print(myminheap.extract_min(), end=' ')




