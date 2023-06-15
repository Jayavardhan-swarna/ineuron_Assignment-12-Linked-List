class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isCircular(head):
    if head is None:
        return False

    slow = head
    fast = head.next

    while fast is not None and fast.next is not None:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next

    return False



# Create a circular linked list: 10 -> 12 -> 14 -> 16
head = ListNode(10)
head.next = ListNode(12)
head.next.next = ListNode(14)
head.next.next.next = ListNode(16)
head.next.next.next.next = head

# Check if the linked list is circular
circular = isCircular(head)

# Print the result
if circular:
    print("The linked list is circular")
else:
    print("The linked list is not circular")
