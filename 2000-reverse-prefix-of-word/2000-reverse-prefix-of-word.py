class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i=0
        while i<len(word):
            if word[i]!=ch:
                i+=1
            else:
                break
        if i==len(word):
            return word
        right=i+1
        low=i
        ans=""
        while low>=0:
            ans+=word[low]
            low-=1
        while right<len(word):
            ans+=word[right]
            right+=1
        return ans


            