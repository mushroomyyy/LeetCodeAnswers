class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        unique_list = list(dict.fromkeys(nums))
        print(unique_list)
        if len(unique_list) == len(nums):
            return False
        else:
            return True



       