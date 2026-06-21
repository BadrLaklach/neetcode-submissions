class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int,int> countMap;

        for( int number:nums ){
            countMap[number]++;
            if (countMap[number] >= 2){
                return true;
            }
        }
        return false;

    }
};
