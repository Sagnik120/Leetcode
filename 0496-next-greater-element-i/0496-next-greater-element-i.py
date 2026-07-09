class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for num in nums1:
            # Find where num is in nums2
            index = nums2.index(num)

            # Search only to the right
            for i in range(index + 1, len(nums2)):
                if nums2[i] > num:
                    ans.append(nums2[i])
                    break
            else:
                ans.append(-1)

        return ans