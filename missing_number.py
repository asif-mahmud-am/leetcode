# Problem 268 

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        arr = []
        if length==1:
            if nums[0] ==0:
                return 1
            else:
                return 0
        for i in range(1,length+1):
            arr.append(i)
        for i in arr:
            if i not in nums:
                return i
        return 0
