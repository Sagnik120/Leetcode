class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        graph = [[] for _ in range(n)]
        indegree = [0] * n

        max_cost = 0

        for u, v, w in edges:
            graph[u].append((v, w))
            indegree[v] += 1
            max_cost = max(max_cost, w)

        # Topological order
        q = deque()

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        topo = []

        while q:
            u = q.popleft()
            topo.append(u)

            for v, _ in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        def check(limit):
            dp = [inf] * n
            dp[0] = 0

            for u in topo:
                if dp[u] == inf:
                    continue

                for v, w in graph[u]:

                    if w < limit:
                        continue

                    if v != n - 1 and not online[v]:
                        continue

                    if dp[v] > dp[u] + w:
                        dp[v] = dp[u] + w

            return dp[n - 1] <= k

        lo, hi = 0, max_cost
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2

            if check(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans