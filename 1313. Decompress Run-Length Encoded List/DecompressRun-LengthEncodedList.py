class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        output = []

        for i in range(0, len(nums), 2):
            freq = nums[i]
            val = nums[i+1]
            for _ in range(freq):
                output.append(val)
                
            return output
