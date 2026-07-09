class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0 #1
        currentnum = 0 #0
        
        for num in nums:
            if num == 1:
                currentnum+=1
                res = max(res, currentnum)
            else:
                currentnum-=currentnum
            
        return res
