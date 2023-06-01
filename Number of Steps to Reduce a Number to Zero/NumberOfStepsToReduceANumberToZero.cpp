class Solution {
public:
    int numberOfSteps(int num) {
        int i = 0;
        //repeat steps until num is zero
        while(num > 0){
            if(num % 2 == 0){
                num /= 2;
                i++;
            }
            else{
                num -= 1;
                i++;
            }
        }
        return i;
    }
};
