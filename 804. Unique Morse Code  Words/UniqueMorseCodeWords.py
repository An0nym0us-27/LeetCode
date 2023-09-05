class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morseDict = { #morse code dictionary
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
            "j": ".---",
            "k": "-.-",
            "l": ".-..",
            "m": "--",
            "n": "-.",
            "o": "---",
            "p": ".--.",
            "q": "--.-",
            "r": ".-.",
            "s": "...",
            "t": "-",
            "u": "..-",
            "v": "...-",
            "w": ".--",
            "x": "-..-",
            "y": "-.--",
            "z": "--.."
        }
        transformations = set()  #used to store unique vals only

        for word in words: #iterate through words string
            morse_val = "" #the morse code version of the letter
            for letter in word: #checks the each char in each word in the provided string
                if letter in morseDict: #if the letter is valid
                    morse_val += morseDict[letter] #add morse code val to the morse_val string

            transformations.add(morse_val) # appends morse_val to transformation set

        return len(transformations) #return length of transformations
