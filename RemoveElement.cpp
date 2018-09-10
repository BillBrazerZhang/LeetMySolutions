//my solution
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        for (unsigned i=0; i<nums.size(); i++){
            if (nums[i]==val){
                nums.erase(nums.begin()+i);
                i--;
            }
        }
        return nums.size();
    }
};


//standard solution
int removeElement(vector<int>& nums, int val) {
    int cnt = 0;
    for(int i = 0 ; i < nums.size() ; ++i) {
        if(nums[i] == val)
            cnt++;
        else
            nums[i-cnt] = nums[i];
    }
    return nums.size()-cnt;
}
