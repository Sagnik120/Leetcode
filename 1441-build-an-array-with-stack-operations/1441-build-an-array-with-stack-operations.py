class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        curr = 1

        for num in target:
            # For every missing number from the stream, push then immediately pop
            while curr < num:
                res.append("Push")
                res.append("Pop")
                curr += 1

            # Push the matching target number
            res.append("Push")
            curr += 1

        return res