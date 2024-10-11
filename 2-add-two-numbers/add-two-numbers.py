# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []

        while l1:
            num1.insert(0, l1.val)
            l1 = l1.next
        while l2:
            num2.insert(0, l2.val)
            l2 = l2.next

        i, j = len(num1) - 1, len(num2) - 1

        remainder = 0

        root = None
        curr = None

        while i >= 0 and j >= 0:
            ans = num1[i] + num2[j] + remainder
            remainder = ans // 10
            ans = ans % 10

            if not curr:
                root = ListNode(ans)
                curr = root
            else:
                curr.next = ListNode(ans)
                curr = curr.next

            i -= 1
            j -= 1

        while i >= 0:
            ans = num1[i] + remainder
            remainder = ans // 10
            ans = ans % 10
            curr.next = ListNode(ans)
            curr = curr.next
            i -= 1

        while j >= 0:
            ans = num2[j] + remainder
            remainder = ans // 10
            ans = ans % 10
            curr.next = ListNode(ans)
            curr = curr.next
            j -= 1
        
        if remainder:
            curr.next = ListNode(remainder)

        return root

        

        
