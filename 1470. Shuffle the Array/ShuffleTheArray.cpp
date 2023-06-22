class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        int size = nums.length;
        int middle = (size / 2)

        if(size % 2 == 0){
            for(int i = 1; i <= middle; i++){
                for(int j = middle; j < size; j++){
                    int next = nums[i+1];
                    
                    temp = nums[i];
                    nums[i] = nums[j];


                }
            }
        }
    }
};
