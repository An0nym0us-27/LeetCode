class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        alphabet = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
        output = []
        start = 0
        end = 0

        for location in s:
            if location > start:
                end = location
            else:
                for letter in alphabet:
                    if location == letter:
                        output.append(letter)
                        while location != letter:
                            output.append(letter)

        return output
