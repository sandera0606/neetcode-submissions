class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        nxt = defaultdict(list)
        tickets= sorted(tickets)[::-1]
        for a, b in tickets:
            nxt[a].append(b)
        
        path = []
        def dfs(fro):
            while nxt[fro]:
                to = nxt[fro].pop()
                dfs(to)
            path.append(fro)
            
        dfs("JFK")
        path.reverse()
        return path