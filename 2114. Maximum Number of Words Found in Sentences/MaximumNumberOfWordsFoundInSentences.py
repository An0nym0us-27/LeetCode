class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
                #count the number of spaces and add 1, return highest number of spaces plus 1
        return max(spaces.count(" ") for spaces in sentences) + 1
