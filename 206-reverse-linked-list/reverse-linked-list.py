# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
   
        prev = None 
        curr = head  
        # Set prev and curr

        while curr is not None:  
            curr.next, curr, prev = prev, curr.next, curr 

            # Set the next node to prevous (flip the arrow) 
            # Increment curr to curr.next 
            # Increment prev to curr 
            # We need to do all this at once so we use a parelell assignment

        # Return prev since curr points to None at the end
        return prev
        

# Time taken 13:22
# Time Complexity O(n)
# Space Complexity O(n) 
