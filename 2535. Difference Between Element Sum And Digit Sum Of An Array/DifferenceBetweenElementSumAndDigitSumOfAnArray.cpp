class Solution {
public:
    int differenceOfSum(vector<int>& nums) {
        int x = 0; //element sum
        int y = 0; //digit sum
        int eh; //element holder
        
        int tempInt;
        vector<int> temp;


        for(int i = 0; i < nums.size(); i++){
            x += nums[i]; //finds element sum
            eh = nums[i];

            //stores each element into temp vector
            while(eh > 0){
                tempInt = eh % 10;
                temp.push_back(tempInt);
                eh /= 10;
            }
        }
        for(int i = 0; i < temp.size(); i++){
            y += temp[i]; //finds digit sum
        }

        int difference = abs(x - y); //take absolute val of x - y

        return difference;
    }
};
