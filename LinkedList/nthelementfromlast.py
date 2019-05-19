

# Node Class


class node:
    def __init__(self, val):
        self.data = val
        self.next = None


# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, val):
        if self.head == None:
            self.head = node(val)
        else:
            new_node = node(val)
            temp = self.head
            while (temp.next):
                temp = temp.next
            temp.next = new_node


def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head

def getNthFromLast(head, n):
    # Code here
    curr = head
    count = 0
    while curr:
        count += 1
        curr = curr.next
    if n > count:
        return -1
    k = count - n
    count = 1
    curr = head
    while count <= k and curr:
        curr = curr.next
        count += 1

    if curr:
        return curr.data
    else:
        return -1
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        head = createList(arr, n)
        print(getNthFromLast(head, k))
# Contributed by: Harshit Sidhwa



''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

# your task is to complete this function
# function should return index to the any valid peak element


