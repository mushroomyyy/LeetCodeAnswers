class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        e = ""
        for i in range(len(strs[0])): # flower
            for word in strs: # flower flow flight
                if i == len(word) or word[i] != strs[0][i]:
                    return e
            e += strs[0][i]
        return e
