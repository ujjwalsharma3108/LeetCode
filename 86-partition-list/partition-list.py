class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:

        if head is None:
            return None

        left = left_head = ListNode(0)
        right = right_head = ListNode(0)

        curr = head

        while curr:
            if curr.val < x:
                left.next = curr
                left = left.next
            else:
                right.next = curr
                right = right.next

            curr = curr.next

        right.next = None
        left.next = right_head.next

        return left_head.next