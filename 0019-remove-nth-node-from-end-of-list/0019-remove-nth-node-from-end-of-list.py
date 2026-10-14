# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        pre=head
        temp=head
        for i in range(n):
            pre=pre.next
        if not pre:
            return head.next
        while pre.next:
            pre=pre.next
            temp=temp.next
        temp.next=temp.next.next
        return head
