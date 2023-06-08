class Solution {
public:
    int xorOperation(int n, int start) {
        int temp = start;

        int* nums= new int[n];
        for(int i = 0; i < n; i++){
            nums[i] = (start + 2 * i);
            temp ^= nums[i];
        }
        delete[] nums;

        return temp;
    }
};
