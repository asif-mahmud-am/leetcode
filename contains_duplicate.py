# Leetcode 75

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        arr = list(set(nums))
        if len(arr) != len(nums):
            return True
        else:
            return False
