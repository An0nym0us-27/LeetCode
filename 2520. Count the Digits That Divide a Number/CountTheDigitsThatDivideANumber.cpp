class Solution {
public:
    int countDigits(int num) {
        int counter = 0;
        int element;
        int val;
        int nums = num;

        vector<int> myvec; //declare vector

        //individually store each integer of num in myvec
        while(num > 0){
            element = num % 10;
            myvec.push_back(element);
            num /= 10;
        }

        //count how many elements can divide nums
        for(int i = 0; i < myvec.size(); i++){
            val = myvec[i];
            if(nums % val == 0){
                counter++;
            }
        }
        
        return counter;
    }
};
