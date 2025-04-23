# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # since the numbers are given backwards we don't need to
        # reverse them (addition is done from LSD)

        curr1 = l1
        curr2 = l2
        len1 = 0
        len2 = 0

        dummy = ListNode() # dummy for edge cases
        prevAns = currAns = dummy

        while curr1:
            curr1 = curr1.next
            len1 += 1
        while curr2:
            curr2 = curr2.next
            len2 += 1

        carry = 0
        curr1 = l1
        curr2 = l2

        while curr1 and curr2:
            newAdd = curr1.val + curr2.val
            currAns = ListNode((newAdd + carry) % 10, None)
            prevAns.next = currAns
            prevAns = currAns

            carry = (newAdd + carry) // 10

            curr1 = curr1.next
            curr2 = curr2.next

        # account for different length numbers
        while curr1:
            currAns = ListNode((curr1.val + carry) % 10, None)
            prevAns.next = currAns
            prevAns = currAns

            carry = (curr1.val + carry) // 10
            curr1 = curr1.next

        while curr2:
            currAns = ListNode((curr2.val + carry) % 10, None)
            prevAns.next = currAns
            prevAns = currAns

            carry = (curr2.val + carry) // 10
            curr2 = curr2.next

        # once the numbers are done, there may still be a carry digit
        if carry:
            currAns = ListNode(carry, None)
            prevAns.next = currAns
        
        return dummy.next