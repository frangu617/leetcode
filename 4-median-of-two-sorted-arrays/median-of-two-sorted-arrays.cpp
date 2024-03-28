class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        std::vector<int> mergedVec = nums1;
        mergedVec.insert(mergedVec.end(), nums2.begin(), nums2.end());

        std::sort(mergedVec.begin(), mergedVec.end());
        int n = mergedVec.size();
        if(n % 2 == 0)
            return (mergedVec[n/2-1] + mergedVec[n/2]) / 2.0;
        else
            return mergedVec[n / 2];
       
    }
};