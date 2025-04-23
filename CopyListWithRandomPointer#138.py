"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # start by making the nodes and setting their next and random
        # to NULL (None).

        curr = head

        # common technique to avoid edge cases when making new list
        dummy = Node(0)
        
        prevNew = currNew = dummy

        # old ptr -> new ptr (got hint for this part)
        hashmap = {}

        # set up copied linked list structure (with next ptr +
        # populate the hashmap for random ptr functionality)
        while curr:
            currNew = Node(
                curr.val,
                None,
                None
            )

            hashmap[curr] = currNew

            prevNew.next = currNew
            prevNew = currNew
            curr = curr.next

        # Revisit each of the new nodes and populate their random ptr
        currNew = dummy.next
        curr = head
        
        while curr:
            # common case
            if curr.random:
                currNew.random = hashmap[curr.random]
            # edge case
            else:
                currNew.random = None
                
            curr = curr.next
            currNew = currNew.next

        return dummy.next