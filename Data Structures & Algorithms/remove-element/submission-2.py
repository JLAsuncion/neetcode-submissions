class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #k is the elements that is not equal to val 
        #scan nums[] then get the ones that is equal to val
        #then return the number of elements that is not equal to k 
        #and also the nums[]

        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = nums[k]
                continue
            else:
                nums[k] = nums[i]
                k+=1
        return k

                
            
        