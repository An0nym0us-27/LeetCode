class Solution:
    def sortSentence(self, s: str) -> str:

        temp = []
        output = []
        tempword = ""
        s += " "
        place = 0

        for word in s:
            if word == " ":
                temp.append(tempword)
                tempword = ""
            else:
                tempword += word


        return temp
