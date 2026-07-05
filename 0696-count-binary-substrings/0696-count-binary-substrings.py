class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count=1
        arr=[]
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                count+=1
            else:
                arr.append(count)
                count=1
        arr.append(count)
        ans=0
        for i in range(len(arr)-1):
            ans+=min(arr[i],arr[i+1])
        return ans