class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        target =''
        count, i = 1, 1
        while i< len(S):
            count += 1 if S[i]=="(" else -1
            if count == 0:
                i += 2
                count += 1
                continue
            target += S[i]
            i += 1
        return target
