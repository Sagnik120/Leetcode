class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        if s == goal:
            return len(set(s)) < len(s)

        s=list(s)
        goal=list(goal)
        index1=-1
        index2=-1

        for i in range(len(s)):
            if s[i]!=goal[i]:
                if index1==-1:
                    index1=i
                elif index2==-1:
                    index2=i
                else:
                    return False
        if index1==-1 or index==-1:
            return False
        s[index1],s[index2]=s[index2],s[index1]

        return True if s==goal else False