class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int X = 0; //counter
        int l = operations.size(); //var for code scalability

        for(int i = 0; i < l; i++){ //increment if string is ++X or X++
            if((operations[i] == "X++") ||  (operations[i] == "++X")){
                X++;
            }
            else{ //decrement if string is --X or X--
                X--;
            }
        }

        return X; //return counter
    }
};
