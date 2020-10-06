

# Complete the deleteNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def deleteNode(head, position):
    if position == 0:
        head = head.next
        return head
    curr = head
    pos = 1
    while curr:
        if pos == position:
            curr.next= curr.next.next
            return head
        else:
            curr = curr.next
            pos += 1
    return head

