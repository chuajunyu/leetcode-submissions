from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # Find all initial rotting oranges:
        rotted = set()
        q = deque()
        oranges = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                    rotted.add((i, j))
                    oranges += 1
                elif grid[i][j] == 1:
                    oranges += 1

        
        next_q = deque()
        count = 0
        while q:
            
            while q:
                i, j = q.popleft()

                for neighbour in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    ni, nj = neighbour
                    if ni >= 0 and ni < len(grid) and nj >= 0 and nj < len(grid[0]):
                        if grid[ni][nj] == 1 and not (ni, nj) in rotted:
                            next_q.append((ni, nj))
                            rotted.add((ni, nj))
            if next_q:
                count += 1
                q, next_q = next_q, q

        return count if len(rotted) == oranges else -1
