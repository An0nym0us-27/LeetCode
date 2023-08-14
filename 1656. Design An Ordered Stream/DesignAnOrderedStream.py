#This is not my own original code, the following is a solution found on github which I reviewed and commented on for learning purposes

class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 1 #initialize pointer to index 1 instead of 0
        self.stream = [""] * (n+1) #creates a list of empty strings of size (n + 1), n determines how many empty strings will be instantiated

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value #inserts the string into the specified idkey
        res = [] #instantiates list res
        
        if idKey == self.ptr: #This checks to make sure we are good to insert at the current index, if idKey is equal to the pointer
            while self.ptr < len(self.stream) and self.stream[self.ptr]: #as long as pointer is within stream length and isnt empty
                res.append(self.stream[self.ptr]) #insert string into empty index
                self.ptr += 1 #increment pointer to next index

            return res #update list
