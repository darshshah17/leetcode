# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # soln 1:
        # two pointer;
        # 1 at head and 1 at tail where both move toward each other
        # DOESNT WORK BC WE DONT HAVE A PREV POINTER

        # soln 2:
        # add a prev attribute in the ListNode class?
        # SHOULDNT DO THAT (SHOULD NOT ADD FIELDS TO THE NODES)

        # soln 3 (got hint):
        # divide linked list in halves
        # reverse the second half
        # then just join both and iterate until done
        dummy = head
        head2 = tail2 = head
        
        # bring head2 to middle of list
        while tail2 and tail2.next:
            head2 = head2.next
            tail2 = tail2.next.next

        # make head2 be where it should and make the previous one
        # point to NULL
        temp = head2
        head2 = head2.next
        temp.next = None

        # reverse second half
        prev = None
        curr = head2
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # head2 is at the end of the list, head is at the front
        head2 = prev

        while head2:
            temp1 = head.next
            temp2 = head2.next
            head.next = head2
            head2.next = temp1
            head = temp1
            head2 = temp2