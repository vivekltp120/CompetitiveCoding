#leetcode submission(Already Submitted)
def sum_of_two_list():
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None

    class Solution:
        def addTwoNumbers(self, l1, l2):
            sumlist = []
            carry = 0
            while l1 and l2:
                z = l1.val + l2.val
                digitsum = (z + carry) % 10
                carry = (z + carry) // 10
                sumlist.append(digitsum)
                l1 = l1.next
                l2 = l2.next

            while l1:
                z = l1.val
                digitsum = (z + carry) % 10
                carry = (z + carry) // 10
                sumlist.append(digitsum)
                l1 = l1.next

            while l2:
                z = l2.val
                digitsum = (z + carry) % 10
                carry = (z + carry) // 10
                sumlist.append(digitsum)
                l2 = l2.next

            if l1 == None and l2 == None and carry != 0:
                sumlist.append(carry)

            return sumlist