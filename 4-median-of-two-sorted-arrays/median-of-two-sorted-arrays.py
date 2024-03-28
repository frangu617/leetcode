class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newArray = nums1 + nums2
        newArray = sorted(newArray)
        print(newArray)
        if newArray == []:
            return null
        else:
            if len(newArray) % 2 == 0:
                left_left = 0
                right_right = len(newArray)
                left_mid = newArray[len(newArray)//2-1]
                right_mid = newArray[len(newArray)//2]
                print(left_mid, right_mid)
                return ((left_mid + right_mid) / 2)
            else:
                mid = newArray[len(newArray)//2]
                print(mid)
                return mid
        