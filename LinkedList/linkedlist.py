
#self created class
class node(object):
  def __init__(self,data):
      self.data=data
      self.next=None

class SLL(object):
      def __init__(self):
          self.head=None


      def appendfront(self,data):
          if self.head==None:
              self.head=node(data)

          elif self.head!=None:
              temp=node(data)
              temp.next=self.head
              self.head=temp

      def gethead(self):
          return self.head

      def display(self):
          temp=self.gethead()
          while temp!=None:
              print(str(temp.data),end ='-->')
              temp=temp.next
          print('Null')

      def append(self, data):
          if self.gethead()==None:
              self.head=node(data)
          else:
              temp=self.gethead()
              while temp.next!=None:
                  temp=temp.next
              newnode=node(data)
              temp.next=newnode

      def reverse(self):
          prev=None
          curr=self.gethead()
          while curr != None:
              new=curr.next
              curr.next=prev
              prev=curr
              curr=new
          self.head=prev

#reverse in a group of k
def reverse(head, k):
    # Code here
    curr = head
    prev = None
    next = None
    count = 0
    while count < k and curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        count += 1
    if next is not None:
        head.next = reverse(next, k)
    return prev


#Loop in a linked list from geeksforgeeks
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None
    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    # Utility function to prit the linked LinkedList
    def printList(self, node):
        temp = node
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
    def getHead(self):
        return self.head
    def createLoop(self, n):
        if n == 0:
            return None
        temp = self.head
        ptr = self.head
        cnt = 1
        while (cnt != n):
            ptr = ptr.next
            cnt += 1
        # print ptr.data
        while (temp.next):
            temp = temp.next
        temp.next = ptr

    def detectLoop(self):
        # code here
        visitDict = {}
        curr = self.getHead()
        while curr:
            if visitDict.get(curr) != None and visitDict[curr] == 'T':
                return True
            else:
                visitDict[id(curr)] = 'T'
            curr = curr.next

        return False


def input_detect_loop():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        lst = LinkedList()
        for i in arr:
            lst.push(i)
        ele = int(input())
        lst.createLoop(ele)
        if lst.detectLoop():
            print(True)
        else:
            print(False)


if __name__ == '__main__':
      input_detect_loop()

#     a=[1,3,4,5]
#     slf=SLL()
#     slt=SLL()
#     for x in a:
#         print(x)
#         slf.appendfront(x)
#         slt.append(x)
#     slf.reverse()
#     slf.display()
#     slt.display()
