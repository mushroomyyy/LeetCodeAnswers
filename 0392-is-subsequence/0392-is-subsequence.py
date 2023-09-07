class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ind_s = 0
        for char in t:
            if ind_s< len(s) and char == s[ind_s]:
                ind_s += 1
        if ind_s == len(s):
            return True
        else:
            return False
                   
       
        

 