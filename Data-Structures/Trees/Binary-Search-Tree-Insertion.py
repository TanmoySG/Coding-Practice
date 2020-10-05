#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        if self.root.info == val:
            self.root = self.root
        #Enter you code here.
        curr = self.root
        while curr is not None:
            if curr.info < val:
                if curr.right is not None:
                    curr = curr.right
                else:
                    curr.right = Node(val)
                    break
            elif curr.info > val:
                if curr.left is not None:
                    curr = curr.left
                else:
                    curr.left = Node(val)
                    break
            else:
                break
        return self.root
