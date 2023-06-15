class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteMiddleNode(head):
    if head is None or head.next is None:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    slow = dummy
    fast = dummy
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    
    slow.next = slow.next.next
    
    return dummy.next


# Create linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

new_head = deleteMiddleNode(head)

# Traverse the modified linked list and print the values
while new_head is not None:
    print(new_head.val, end=" ")
    new_head = new_head.next

# Output: 1 2 4 5
