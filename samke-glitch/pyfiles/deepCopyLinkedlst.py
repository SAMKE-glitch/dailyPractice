
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Step 1: Create a mapping of original nodes to copied nodes
        mapping = {}
        current = head
        while current:
            mapping[current] = Node(current.val)
            current = current.next
        # Step 2: Update the next pointers of copied nodes
        current = head
        while current:
            if current.next:
                mapping[current].next = mapping[current.next]
            current = current.next
        # Step 3: Update the random pointers of copied nodes
        current = head
        while current:
            if current.random:
                mapping[current].random = mapping[current.random]
            current = current.next
        
        return mapping[head]

        
