class Solution(object):
    def findLengthOfLCIS(self,nums):
        max_count = 1
        count = 1

        for i in range(o,len(nums)):
            if i == len(nums)-1:
                break
            if nums[i]<nums[i+1]:
                count+=1
                max_count = max(max_count,count)
            else:
                count =1
        return max_count