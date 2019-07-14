class Solution(object):
    def rob(self, root):
        def postorder(root):
            if root == None:
                return (0,0)
            l = postorder(root.left)
            r = postorder(root.right)
            return  (root.val+l[1]+r[1]  ,  max(l[0], l[1])+ max( r[0], r[1]))
        r = postorder(root)
        return max(r[0],r[1])
