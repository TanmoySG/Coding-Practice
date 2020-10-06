

# Complete the reverse function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reverse(head):
    curr = head
    prev = None
    next = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    head = prev
    return head



