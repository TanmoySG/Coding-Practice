"""
class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
    #Enter Your Code Here
    string = []
    curr = root
    for i in s:
        curr = curr.right if i == '1' else curr.left
        if curr.right is None and curr.left is None:
            string.append(curr.data)
            curr = root
    print("".join(string)) 
