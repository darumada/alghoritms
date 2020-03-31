class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def removeNthFromEnd(head, n):
    dummy = ListNode(None)
    dummy.next = head
    slow = dummy
    fast = dummy

    for i in range(n + 1):
        fast = fast.next

    while fast is not None:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return dummy.next
