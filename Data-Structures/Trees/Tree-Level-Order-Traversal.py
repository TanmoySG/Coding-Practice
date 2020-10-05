

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def levelOrder(root):
    #Write your code here
    queueOfNodes = [root]
    while len(queueOfNodes) > 0:
        node = queueOfNodes.pop(0)
        print(node.info, end=" ")
        if node.left:
            queueOfNodes.append(node.left)
        if node.right:
            queueOfNodes.append(node.right)

