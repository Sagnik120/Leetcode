class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index = {}

        # Store restaurant -> index
        for i, restaurant in enumerate(list1):
            index[restaurant] = i

        ans = []
        min_sum = float('inf')

        # Check common restaurants
        for j, restaurant in enumerate(list2):
            if restaurant in index:
                total = index[restaurant] + j

                if total < min_sum:
                    min_sum = total
                    ans = [restaurant]
                elif total == min_sum:
                    ans.append(restaurant)

        return ans