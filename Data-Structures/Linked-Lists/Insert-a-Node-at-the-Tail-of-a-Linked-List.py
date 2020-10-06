

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    newNode = SinglyLinkedListNode(data)
    newNode.next = None
    if head is None:
        head = newNode
        return head
    curr = head
    while curr:
        if curr.next is None:
            curr.next = newNode
            return head
        else:
            curr = curr.next

