class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr=[]
        for i in nums1:
            if i in nums2:
                e=-1
                s=-1
                for j in range(len(nums2)):
                    if nums2[j]==i:
                        s=j
                    if (s>-1 and j>s):
                            if nums2[j]>i:
                                e=nums2[j]
                                break
                arr.append(e)
        return arr
