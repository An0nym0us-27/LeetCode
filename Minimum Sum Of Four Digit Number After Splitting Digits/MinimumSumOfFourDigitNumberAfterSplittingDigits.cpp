class Solution {
public:
    int minimumSum(int num) {
    //variable declaration
    int new1;
    int new2;
    int sum;
    int index0;
    int index1;
    int index2;
    int index3;

    index0 = num / 1000;
    index1 = (num / 100) % 10;
    index2 = (num / 10) % 10;
    index3 = num % 10;

    new1 = index0 + index1;
    new2 = index2 + index3;

    sum = new1 + new2;
    return sum;
    }
};
