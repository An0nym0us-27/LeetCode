class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = [int]
        for i in nums:
            target[index[i]] = nums[i]

        return target
