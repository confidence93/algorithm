class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0
        total = 0 
        left = 0
        right = max(height)
        
        for i in range(len(height)):
            
            left = max(left,height[i])
            if height[i] == right and i != len(height)-1: 
                right = max(height[i+1:])
          
            if height[i] < min(left, right):
                total += min(left, right) - height[i]
                #print total,i
        return total
