class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newArray = nums1 + nums2
        newArray = sorted(newArray)
        if newArray == []:
            return null
        else:
            if len(newArray) % 2 == 0:
                return ((newArray[len(newArray)//2-1] + newArray[len(newArray)//2]) / 2)
            else:
                return newArray[len(newArray)//2]
        