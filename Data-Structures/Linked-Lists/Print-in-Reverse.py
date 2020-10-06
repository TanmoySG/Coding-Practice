

# Complete the reversePrint function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reversePrint(head):
    curr = head
    arrayOfLL = []
    while curr is not None:
        arrayOfLL.insert(0, str(curr.data))
        curr = curr.next
    print("\n".join(arrayOfLL))
    

