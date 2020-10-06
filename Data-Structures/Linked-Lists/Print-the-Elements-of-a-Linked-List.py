

# Complete the printLinkedList function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def printLinkedList(head):
    curr = head
    while curr is not None:
        print(curr.data)
        curr = curr.next

