#It does not detect duplicates and the absolute value difference so i need to go back and fix this in my code
Class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        dict = {}
        pairs = 0

        for num in nums:
            dict[num] = len(nums)

        for num in dict:
            if num - k in dict:
                pairs = pairs + 1

        return pairs
