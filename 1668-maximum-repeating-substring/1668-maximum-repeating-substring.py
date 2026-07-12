class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n=len(sequence)
        m=len(word)

        dp=[0]*n

        ans=0

        for i  in range(m-1,n):
            if sequence[i-m+1:i+1]==word:
                dp[i]=1
                if i>=2*m-1:
                    dp[i]+=dp[i-m]
                ans=max(ans,dp[i])
        return ans