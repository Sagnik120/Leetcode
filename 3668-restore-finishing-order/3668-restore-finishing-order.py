class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        s=set(friends)
        ans=[]
        for x in order:
            if x in s:
                ans.append(x)
        return ans