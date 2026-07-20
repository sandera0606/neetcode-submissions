class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        pre = defaultdict(list)
        tickets = sorted(tickets)[::-1]

        for f, t in tickets:
            pre[f].append(t)

        path = []

        def dfs(port):
            while pre[port]:
                fro = pre[port].pop()
                dfs(fro)
            path.append(port)

        dfs("JFK")  
        return path[::-1]