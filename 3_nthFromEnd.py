class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def nthFromEnd(head, n):
    if head is None:
        return -1
    
    slow = head
    fast = head
    
    # Move the fast pointer N nodes ahead of the slow pointer
    for _ in range(n):
        if fast is None:
            return -1
        fast = fast.next
    
    # Move both pointers together until fast reaches the end
    while fast.next is not None:
        slow = slow.next
        fast = fast.next
    
    return slow.val



# Create linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)
head.next.next.next.next.next.next.next.next = ListNode(9)

n = 2
result = nthFromEnd(head, n)

print(result)  # Output: 8
