class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        valid = {"electronics", "grocery", "pharmacy", "restaurant"}
        order = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }

        ans = []

        for c, b, active in zip(code, businessLine, isActive):
            if not active:
                continue
            if b not in valid:
                continue
            if not c:
                continue

            ok = True
            for ch in c:
                if not (ch.isalnum() or ch == "_"):
                    ok = False
                    break

            if ok:
                ans.append((b, c))

        ans.sort(key=lambda x: (order[x[0]], x[1]))
        return [c for _, c in ans]