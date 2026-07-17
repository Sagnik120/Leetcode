class Solution:
    def dayOfYear(self, date: str) -> int:
        # Standard non-leap year days list
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        parts = date.split("-")
        
        def is_leap_year(year: int) -> bool:
            return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

        extra = is_leap_year(int(parts[0]))
        n = int(parts[1])
        ans = int(parts[2])
        
        for i in range(n - 1):
            if i == 1:
                ans += extra
            ans += days[i]
            
        return ans
