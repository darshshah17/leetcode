# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # slower way is to count length of linked list and then count til len - n
        # nodes. instead, this soln does it in 1 pass:
        # move to the n-th node from the front, then move
        # from the start until that node reaches the end

        i = 1
        curr = head

        while i < n:
            curr = curr.next
            i += 1

        prev = None
        removeNode = head

        # instead of doing while curr, we do curr.next so that
        # removeNode is actually the node to remove (otherwise 
        # curr would be NULL, prev would be the node to remove
        # and removeNode would be 1 past it)
        while curr.next:
            prev = removeNode
            removeNode = removeNode.next
            curr = curr.next
        
        # edge case:
        if removeNode == head:
            head = removeNode.next
        # common case
        else:
            prev.next = removeNode.next

        return head