class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []  # Stores function IDs
        prev_time = 0

        for log in logs:
            fn_id_str, type_, time_str = log.split(":")
            fn_id = int(fn_id_str)
            timestamp = int(time_str)

            if type_ == "start":
                if stack:
                    # Add execution time to the function currently at the top of stack
                    res[stack[-1]] += timestamp - prev_time
                stack.append(fn_id)
                prev_time = timestamp
            else:
                # Add execution time (inclusive of end timestamp) to the completing function
                res[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1

        return res