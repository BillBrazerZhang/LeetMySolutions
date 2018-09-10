class Solution {
    #include <vector>
public:
    vector<int> twoSum(vector<int>& nums, int target) {
       vector<int> twoSum = {0,0};
       int length = nums.size();
       for (int i = 0 ; i < length; i++)
          for (int j = 0; j < i; j++)
               if (nums[i] + nums[j] == target)
                  {
                      twoSum[0] = j;
                      twoSum[1] = i;
                      return twoSum;
                  }


    }
};
