class Solution:
    def isValid(self, s: str) -> bool:

        st = []

        for ch in s:

            if ch == '(':
                st.append(ch)

            elif ch == '{':
                st.append(ch)

            elif ch == '[':
                st.append(ch)

            elif ch == ')':
                if not st or st[-1] != '(':
                    return False
                st.pop()

            elif ch == '}':
                if not st or st[-1] != '{':
                    return False
                st.pop()

            elif ch == ']':
                if not st or st[-1] != '[':
                    return False
                st.pop()

        return len(st) == 0
