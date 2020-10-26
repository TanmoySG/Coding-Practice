# Find the Top view of a Tree
'''

  1 (0) <
   \
     2 (+1) <
      \
       5 (+2) <
      /  \ 
(+1) 3    6 (+3) <
      \
       4 (+2)
       
Top View (from left to right) : [ 1 2 5 6 ]

* The Number within brackets represent the Horizontal Distance of that Node.
* For any Parent node:
  - The Left Node has horizontal distance 1 less than that of its Parent Node ( HD_of_Parent - 1)
  - The Right Node has horizontal distance 1 less than that of its Parent Node ( HD_of_Parent + 1)

'''

def topView(root):
    top_view = {} # map the first node corresponding to a particular Horizontal Distance, like ( 1 : Node_1 )
    level_queue = [] # Used for level order traversal 
    level_queue.append((root, 0))
    while level_queue:
        for _ in range(len(level_queue)):
            # pop left most element of the level queue
            node , distance = level_queue.pop(0)
            
            if node is None:
                continue
            
            # if the particular distance is encountered for the first time, map the distance to the node, 
            # i.e. if the particular HD is not present, no node with that HD is encountered
            if distance not in top_view.keys():  
                top_view[distance] = node.info
            
            level_queue.append((node.left, distance-1))  # append the left node of the parent to the level que with its HD (Horizontal Distance)
            level_queue.append((node.right, distance+1)) # apeend the right node of the parent to the level que with its HD
            
    for _ , value in sorted(list(top_view.items())):
        print(value, end=' ')
