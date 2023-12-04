#!/usr/bin/python3

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # Check if either list is empty, return the other list
        if not list1:
            return list2
        elif not list2:
            return list1
        
        # Initialize a dummy node as the start of the merged list
        dummy = ListNode(0)
        # Current node to keep track of the last node in the merged list
        current = dummy
        
        # Iterate until one of the lists is exhausted
        while list1 and list2:
            # Compare the values of the current nodes in list1 and list2
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            # Move the current pointer to the last node in the merged list
            current = current.next
        
        # If one of the lists is not exhausted, append the remaining nodes
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        # The merged list starts from the next node of the dummy node
        return dummy.next

