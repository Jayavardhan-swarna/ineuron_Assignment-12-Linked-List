class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insertAtAlternatePositions(first, second):
    if second is None:
        return first

    # Store the heads of the first and second lists
    head1 = first
    head2 = second

    while first is not None and second is not None:
        # Save the next pointers of both first and second nodes
        next1 = first.next
        next2 = second.next

        # Insert the second node into the first list
        first.next = second
        second.next = next1

        # Move the first and second pointers to their respective next nodes
        first = next1
        second = next2

    # Set the next pointer of the last node of the first list to None
    if first is not None:
        first.next = None

    # Return the modified first list
    return head1


# Create first list: 5 -> 7 -> 17 -> 13 -> 11
first = ListNode(5)
first.next = ListNode(7)
first.next.next = ListNode(17)
first.next.next.next = ListNode(13)
first.next.next.next.next = ListNode(11)

# Create second list: 12 -> 10 -> 2 -> 4 -> 6
second = ListNode(12)
second.next = ListNode(10)
second.next.next = ListNode(2)
second.next.next.next = ListNode(4)
second.next.next.next.next = ListNode(6)

# Insert nodes of second list into first list at alternate positions
modified_first = insertAtAlternatePositions(first, second)

# Print the modified first list
curr = modified_first
while curr is not None:
    print(curr.val, end=" ")
    curr = curr.next

# Print the second list (should be empty)
curr = second
while curr is not None:
    print(curr.val, end=" ")
    curr = curr.next
