# Check is a given Binary Tree is Binary Search Tree
""" 
Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def validate(root, max, min):
    if root is None:
        return True
    elif (max is not None and max <= root.data) or (min is not None and min >= root.data):
        return False
    else:
        return validate(root.left, root.data, min) and validate(root.right, max, root.data)

def check_binary_search_tree_(root):
    return validate(root, None, None)
