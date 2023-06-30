class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int most = 0; //value of kid with most candies
        int cpe = 0; //cpe = candies plus extra

        vector<bool> result; //output vector instantiation

        //determine most candies value
        for(int i = 0; i < candies.size(); i++){
            if(candies[i] > most){ //if current index is greater than previous most value, then update val
                most = candies[i];
            }
        }
        //compare cpe of every index with most candies
        for(int i = 0; i < candies.size(); i++){
            cpe = candies[i] + extraCandies;
            if(cpe >= most){ //if cpe is greater than equal to most, then push back true
                result.push_back(true);
            }
            else{ //else push back false
                result.push_back(false);
            }
        }
    return result; //returns result
    }
};
