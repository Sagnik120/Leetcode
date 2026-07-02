class Solution:
    def average(self, salary: List[int]) -> float:
        max1=max(salary)
        min1=min(salary)
        s=0
        for i in salary:
            s+=i
        s-=max1
        s-=min1
        return s/(len(salary)-2)