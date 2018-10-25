

class node(object):
  def __init__(self,data):
      self.data=data
      self.next=None

class SLL(object):
      def __init__(self):
          self.head=None


      def insertfront(self,data):
          if self.head==None:
              self.head=node(data)

          elif self.head!=None:
              temp=node(data)
              temp.next=self.head
              self.head=temp

      def gethead(self):
          return self.head

      def printlist(self):
          temp=self.gethead()
          while temp!=None:
              print(str(temp.data),end ='-->')
              temp=temp.next
          print('Null')

      def inserttail(self,data):
          if self.gethead()==None:
              self.head=node(data)
          else:
              temp=self.gethead()
              while temp.next!=None:
                  temp=temp.next
              newnode=node(data)
              temp.next=newnode

      def reverselist(self):
          prev=None
          curr=self.gethead()
          while curr != None:
              new=curr.next
              curr.next=prev
              prev=curr
              curr=new
          self.head=prev



if __name__=='__main__':
    a=[1,3,4,5]
    slf=SLL()
    slt=SLL()
    for x in a:
        print(x)
        slf.insertfront(x)
        slt.inserttail(x)
    slf.reverselist()
    slf.printlist()
    slt.printlist()
