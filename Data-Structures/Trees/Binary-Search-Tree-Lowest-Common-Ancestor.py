'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
    curr = root
    while curr:
        if curr.info > v1 and curr.info > v2:
            curr = curr.left
        elif curr.info < v1 and curr.info < v2:
            curr = curr.right
        else:
            break
    return curr
