class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        #find sum of current and next index
        #store new value in current index
        for i in range(1,len(nums)):
            nums[i] = nums[i] + nums[i-1]

        return nums #return sum
