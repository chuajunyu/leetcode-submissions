class Solution:
    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])
        result = [['.'] * m for _ in range(n)]
        
        # Loop through each row in original box
        # count number of objects before the next obstacle
        # backfill the number
        for i in range(m):
            new_col = m - i - 1
            count = 0
            for j in range(n + 1):  # Loop an extra time to account for floor
                if j >= n or boxGrid[i][j] == '*':
                    if j < n:
                        result[j][new_col] = '*'
                    for c in range(count):
                        result[j - c - 1][new_col] = '#'
                    count = 0
                elif boxGrid[i][j] == '#':
                    count += 1
        
        return result


        