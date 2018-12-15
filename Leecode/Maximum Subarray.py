class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
     
  
        max = -99999999999999
        count = 0
        for j in range(len(nums)):
            for i in range(j,len(nums)):
                count += nums[i]
                if count > max:
                    max = count
            count = 0        
        return max
        """
        result = [0 for i in range(len(nums))]
        result[0] = nums[0]
    
        for j in range(1,len(nums)):
            if result[j-1] < 0:
                result[j] = nums[j]
            else:
                result[j] = result[j-1] + nums[j]
        return max(result)
        
        
        
