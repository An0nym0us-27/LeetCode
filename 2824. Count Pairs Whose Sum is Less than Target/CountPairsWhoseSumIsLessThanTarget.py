class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        condition = 0
        cntr = 0
        check = []
        for indx, num in enumerate(nums):
            if (indx < (len(nums)-1)):
                for i in nums:
                    j = nums[indx+1]
                    condition = nums[indx] + nums[j]
                    if nums[indx] < nums[j] and condition < target:
                        cntr += 1
                        j += 1
                        check.append(nums[indx])
                        check.append(nums[j])
                    else:
                        j += 1
        return check
