
#Min_Heap Google Docstring
class heap(object):
    """
    A class to represent a heap data structure.
    It can be either a min-heap or a max-heap based on the type specified.
    Attributes:
        arr (list): The array representation of the heap.
        type (str): The type of heap ('min_heap' or 'max_heap').
        heap_size (int): The current size of the heap.
    """ 

    def __init__(self,arr,type):
         """
         Initializes the heap with the given array and type.
         Args:
             arr (list): The array to be used for the heap.
             type (str): The type of heap ('min_heap' or 'max_heap').
         Raises:
             ValueError: If the type is not 'min_heap' or 'max_heap'.
             TypeError: If the input is not a list or contains non-numeric elements.
             ValueError: If the input list is empty.        
         """
         if type not in ['min_heap', 'max_heap']:
             raise ValueError("Heap type must be 'min_heap' or 'max_heap'")
         if not isinstance(arr, list):
             raise TypeError("Input must be a list")
         if not all(isinstance(x, (int, float)) for x in arr):
             raise TypeError("All elements in the list must be numbers")
         if len(arr) == 0:
             raise ValueError("Input list cannot be empty")
         if type == 'min_heap':
             arr = arr[:]
         self.arr=arr
         self.type=type     
         self.heap_size=len(arr)
    def  build_heap(self):
            """ Builds the heap from the array.
            This method rearranges the elements in the array to satisfy the heap property.
            Returns:
                list: The array representing the heap after building it.
            """
            arr = self.arr
            if not arr:
                return arr
            if self.type not in ['min_heap', 'max_heap']:
                raise ValueError("Heap type must be 'min_heap' or 'max_heap'")
            if not isinstance(arr, list):
                raise TypeError("Input must be a list")
            if not all(isinstance(x, (int, float)) for x in arr):
                raise TypeError("All elements in the list must be numbers")
            if len(arr) == 0:
                raise ValueError("Input list cannot be empty")
            self.heap_size = len(arr)
            if self.type == 'min_heap':
                arr = arr[:]
            else:
                arr = arr[:]
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

    
    def maxheapify(self,arr,i):
         """"Maintains the max-heap property for the subtree rooted at index i.
         This method assumes that the left and right subtrees of the node at index i are already max-heaps.
         Args:
             arr (list): The array representation of the heap.
             i (int): The index of the node to be heapified.
         """
         if not arr:
             return
         if not isinstance(arr, list):
             raise TypeError("Input must be a list")
         if not all(isinstance(x, (int, float)) for x in arr):
             raise TypeError("All elements in the list must be numbers")

         left = 2 * i + 1
         right = 2 * i + 2
         largest = i

         if left <= self.heap_size - 1 and arr[left] >= arr[i]:
             largest = left
         if right <= self.heap_size - 1 and arr[right] > arr[largest]:
             largest = right
         if largest != i:
             arr[i], arr[largest] = arr[largest], arr[i]
             self.maxheapify(arr, largest)

    def extract_max(self):
         """Extracts the maximum element from the max-heap.
         This method removes the root element (maximum) from the heap and restores the max-heap property.
         Returns:
             The maximum element from the heap.
         Raises:
             IndexError: If the heap is empty.
         """
         if not self.arr:
             raise IndexError("Heap is empty")
         if not isinstance(self.arr, list):
             raise TypeError("Input must be a list")
         if not all(isinstance(x, (int, float)) for x in self.arr):
             raise TypeError("All elements in the list must be numbers")
         if self.heap_size==0:  
             return
         arr=self.arr
         max_value=arr[0]
         arr[0],arr[self.heap_size-1] = arr[self.heap_size-1], arr[0]
         self.heap_size-=1
         self.maxheapify(arr,0)
         return max_value

    def minheapify(self, arr, i):
         """Maintains the min-heap property for the subtree rooted at index i.
         This method assumes that the left and right subtrees of the node at index i are already min-heaps.
         Args:
             arr (list): The array representation of the heap.
             i (int): The index of the node to be heapified.
         """
         if not arr:
             return
         if not isinstance(arr, list):
             raise TypeError("Input must be a list")         
         left = 2 * i + 1
         right = 2 * i + 2
         smallest = i

         if left <= self.heap_size - 1 and arr[left] <= arr[i]:
             smallest = left
         if right <= self.heap_size - 1 and arr[right] < arr[smallest]:
             smallest = right
         if smallest != i:
             self.arr[i], self.arr[smallest]= arr[smallest], arr[i]
             arr = self.arr
             self.heap_size = len(arr)
             self.minheapify(arr, smallest)

    def extract_min(self):
         """ Extract the min and restore the min-heap properties
         args:
             arr (list): The array representation of the heap.
         Returns:
             The minimum element from the heap.
         Raises:
             IndexError: If the heap is empty.
         """
         if not self.arr:
             raise IndexError("Heap is empty")
         if not isinstance(self.arr, list):
             raise TypeError("Input must be a list")
         if self.heap_size == 0:
             return
         arr = self.arr
         min_value = arr[0]
         arr[0], arr[self.heap_size - 1] = arr[self.heap_size - 1], arr[0]
         self.heap_size -= 1
         self.minheapify(arr, 0)
         return min_value


#driver function

if __name__=="__main__":
    """Driver function to demonstrate the heap operations.
    It creates a max-heap and a min-heap from a given array, builds the heaps,
    and extracts elements from both heaps.
    """
    print("Max Heap:")
    # Example array for max-heap        
    arr=[8,5,7,1,4,2,5,9]
    myheap=heap(arr,'max_heap')
    arr=myheap.build_heap()
    for i in range(len (arr)):
      print(myheap.extract_max(),end=' ')
    print('\n')
    myminheap = heap(arr, 'min_heap')
    arr = myminheap.build_heap()
    for i in range(len(arr)):
        print(myminheap.extract_min(), end=' ')




