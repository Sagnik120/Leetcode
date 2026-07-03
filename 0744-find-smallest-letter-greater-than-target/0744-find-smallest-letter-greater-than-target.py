class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low=0
        high=len(letters)-1
        ans=letters[0]
        while high>=low:
            mid=low+((high-low)>>1)
            if letters[mid]>target:
                ans=letters[mid]
                high=mid-1
            else:
                low=mid+1
        return ans