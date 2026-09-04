class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr=[]
        for i in nums1:
            arr.append(i)
        for i in nums2:
            arr.append(i)
        arr.sort()
        if len(arr)%2==0:
            a=int(len(arr)/2)
            m=(arr[a-1]+arr[a])/2
            return m
        else:
            m=int(len(arr)/2)
            return arr[m]