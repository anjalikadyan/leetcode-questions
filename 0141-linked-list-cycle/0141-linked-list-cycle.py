# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sl, fa = head, head
        while fa and fa.next:
            sl = sl.next          
            fa = fa.next.next      
            if sl == fa:           
                return True
        
        return False 