class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        res = 999999
        l = inorder(root)
        for i in range(1, len(l)):
            res = min(res, l[i] - l[i - 1])
            
        return res
