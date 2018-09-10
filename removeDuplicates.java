//my Solution
class Solution {
    public int removeDuplicates(int[] nums) {
        int m = nums.length;
        int n = 1;
        for (int i=0; i<m-1; i++){
            if (nums[i] != nums[i+1]){
                n++;
                nums[n-1] = nums[i+1];
            }
        }
        return n;
    }
};

//standard solution
public int removeDuplicates(int[] nums) {
    if (nums.length == 0) return 0;
    int i = 0;
    for (int j = 1; j < nums.length; j++) {
        if (nums[j] != nums[i]) {
            i++;
            nums[i] = nums[j];
        }
    }
    return i + 1;
}
