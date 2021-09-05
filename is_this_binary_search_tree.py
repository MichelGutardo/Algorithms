""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

# >>> My Answer
def checkBST(root):

    return check(root)

def check(root,min = None,max = None):

    if root == None:
        return True    

    if min != None: 
        if root.data <= min.data:
            return False
        
    if max != None: 
        if root.data >= max.data:
            return False
      
    return check(root.left,min,root) and check(root.right,root,max) 
    
    