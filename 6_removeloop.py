class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def detectAndRemoveLoop(head):
    slow = head
    fast = head

    # Move slow and fast pointers to find the meeting point
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    # If the fast pointer reached the end, there is no loop
    if fast is None or fast.next is None:
        return

    # Reset slow pointer to the head
    slow = head

    # Move slow and fast pointers one step at a time until they meet again
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next

    # Remove the loop by setting the next pointer of the node where the slow pointer is pointing to null
    fast.next = None



# Create linked list: 1 -> 3 -> 4 -> 3 (loop)
head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(4)
head.next.next.next = head.next  # Create a loop

detectAndRemoveLoop(head)

# Check if the loop is removed
curr = head
while curr is not None:
    print(curr.val, end=" ")
    curr = curr.next
