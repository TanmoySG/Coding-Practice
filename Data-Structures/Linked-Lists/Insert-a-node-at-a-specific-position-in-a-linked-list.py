

# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    positer = 0
    temp = head
    while temp:
        if positer == position-1:
            newNode = SinglyLinkedListNode(data)
            newNode.next = temp.next
            temp.next = newNode
            break
        else:
            positer+=1
            temp = temp.next
    return head

