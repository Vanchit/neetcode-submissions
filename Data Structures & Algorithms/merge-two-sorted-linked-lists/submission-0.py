# Definition for singly-linked list
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # Dummy node marks the beginning of the merged list
        dummy = ListNode(-1)

        # Used to construct the merged list
        current = dummy

        # Continue until one list reaches its end
        while list1 and list2:

            # Add the smaller node to the merged list
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            # Move forward in the merged list
            current = current.next

        # Attach whichever list still has nodes remaining
        if list1:
            current.next = list1
        else:
            current.next = list2

        # Skip the dummy node and return the actual list
        return dummy.next