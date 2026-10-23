# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        last_tail = dummy
        future_head = head
        while True:
            # find new head for this section
            curr_head = future_head
            new_head = curr_head
            for i in range(k - 1):
                new_head = new_head.next
                if new_head is None:
                    return dummy.next
            
            # last section points to the new head
            last_tail.next = new_head

            # save the next section
            future_head = new_head.next

            # reverse this section
            last_tail = curr_head
            node = curr_head
            prev = new_head.next
            while node is not future_head:
                future = node.next
                node.next = prev
                prev = node
                node = future

            if future_head is None:
                return dummy.next
