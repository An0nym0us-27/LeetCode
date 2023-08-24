class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
      alpha = {} #dictionary
      output = False #initially assume its false
      alphabet = 'abcdefghijklmnopqrstuvwxyz' #to check if every letter is in hash map
      counter = 0 #to check if every letter is in hash map

      if(len(sentence) < 26): #I know its false if the length of the string is less than that of the alphabet
        output = False
      else: #else create a hash map from every letter in the sentence
        for char in sentence:
          alpha[char] = len(char)
        
      for chars in alphabet: #if the letter is found in the alphabet, increment counter
        if chars in alpha:
          counter = counter + 1
        else:
          counter = counter #if not counter stays the same

      if counter == 26: #if there are 26 letters found, then we know every letter in alphabet was found
        output = True

      return output
