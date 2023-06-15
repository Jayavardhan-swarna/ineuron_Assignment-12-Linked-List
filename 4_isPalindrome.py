class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head):
    stack = []

    # Traverse the linked list and store each character in the stack
    curr = head
    while curr is not None:
        stack.append(curr.val)
        curr = curr.next

    # Traverse the linked list again and compare characters with the stack
    curr = head
    while curr is not None:
        if curr.val != stack.pop():
            return False
        curr = curr.next

    # If the stack is empty, the linked list is a palindrome
    return True



# Create linked list: R -> A -> D -> A -> R -> None
head = ListNode('R')
head.next = ListNode('A')
head.next.next = ListNode('D')
head.next.next.next = ListNode('A')
head.next.next.next.next = ListNode('R')

result = isPalindrome(head)
print(result)  # Output: True
