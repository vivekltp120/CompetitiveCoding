__author__ = "Vivek"
__author_email__ = "vivekltp120@gmail.com"

"""
This script contains implementations for finding the Kth smallest element using a min-heap,
as well as sorting algorithms like Quick Sort and Merge Sort.
"""

class Solution:
    """
    A class to represent a solution for finding the Kth smallest element in an array.
    """

    def build_heap(self, arr):
        """
        Builds a min-heap from the given array.

        Args:
            arr (list): The input array to be converted into a min-heap.
        """
        self.heap_size = len(arr) - 1
        n = len(arr)
        for i in range(n // 2, -1, -1):
            self.min_heapify(arr, i)

    def swap(self, arr, i, j):
        """
        Swaps two elements in the array.

        Args:
            arr (list): The array in which elements are to be swapped.
            i (int): Index of the first element.
            j (int): Index of the second element.
        """
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def min_heapify(self, arr, i):
        """
        Maintains the min-heap property for the given array.

        Args:
            arr (list): The array representing the heap.
            i (int): The index of the current node.
        """
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
        """
        Finds the Kth smallest element in the array using a min-heap.

        Args:
            arr (list): The input array.
            k (int): The position of the smallest element to find.

        Returns:
            int: The Kth smallest element in the array.
        """
        self.build_heap(arr)
        for i in range(k):
            result = arr[0]
            self.swap(arr, 0, self.heap_size)
            self.heap_size -= 1
            self.min_heapify(arr, 0)
        return result


def quick(arr, p, r):
    """
    Implements the Quick Sort algorithm.

    Args:
        arr (list): The array to be sorted.
        p (int): The starting index of the array.
        r (int): The ending index of the array.
    """
    if p < r:
        q = partition(arr, p, r)
        quick(arr, p, q - 1)
        quick(arr, q + 1, r)


def partition(arr, p, r):
    """
    Partitions the array for Quick Sort.

    Args:
        arr (list): The array to be partitioned.
        p (int): The starting index.
        r (int): The ending index.

    Returns:
        int: The partition index.
    """
    pivot = arr[r]
    j = p
    i = j - 1
    while j < r:
        if arr[j] < pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
        j += 1
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def merge_sort(arr, strt_i, end_i):
    """
    Implements the Merge Sort algorithm.

    Args:
        arr (list): The array to be sorted.
        strt_i (int): The starting index of the array.
        end_i (int): The ending index of the array.
    """
    if strt_i < end_i:
        mid = (end_i + strt_i) // 2
        merge_sort(arr, strt_i, mid)
        merge_sort(arr, mid + 1, end_i)
        merge(arr, strt_i, mid, end_i)


def merge(arr, p, mid, q):
    """
    Merges two sorted subarrays into a single sorted array.

    Args:
        arr (list): The array containing the subarrays to merge.
        p (int): The starting index of the first subarray.
        mid (int): The ending index of the first subarray.
        q (int): The ending index of the second subarray.
    """
    i = 0
    j = 0
    k = p
    left_arr = arr[p:mid + 1]
    right_arr = arr[mid + 1:q + 1]
    print(left_arr)
    print(right_arr)

    while i < mid - p + 1 and j < q - mid:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    while i < mid - p + 1:
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < q - mid:
        arr[k] = right_arr[j]
        j += 1
        k += 1


if __name__ == "__main__":
    """
    Main function to test the implemented algorithms.
    """
    arr = [3, 4, 5, 1, 2, 8, 7, 9]

    # Uncomment to test Quick Sort
    # quick(arr, 0, len(arr) - 1)
    # print(arr)

    # Test Merge Sort
    merge_sort(arr, 0, len(arr) - 1)
    print(arr)

    # Test Kth Smallest Element
    t = int(input("Enter number of test cases: "))
    for tcs in range(t):
        arr = list(map(int, input("Enter array elements: ").strip().split()))
        k = int(input("Enter value of k: "))
        ob = Solution()
        print(ob.kthSmallest(arr, k))