# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
        def check(node, min_val, max_val):
            if node is None:
                return True
            
            # Check if current node's value violates BST property
            if min_val is not None and node.val <= min_val:
                return False
            if max_val is not None and node.val >= max_val:
                return False
            
            # Recursively check left and right subtrees
            # Left subtree: values must be < current node value
            # Right subtree: values must be > current node value
            return (check(node.left, min_val, node.val) and 
                    check(node.right, node.val, max_val))
        
        return check(root, None, None)
        
