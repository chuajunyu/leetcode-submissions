class Solution:
    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        result = [['.'] * len(boxGrid) for x in boxGrid[0]]
        
        # Loop through each row in original box
        # count number of objects before the next obstacle
        # backfill the number
        for i in range(len(boxGrid)):
            count = 0
            for j in range(len(boxGrid[0]) + 1):
                if j >= len(boxGrid[0]) or boxGrid[i][j] == '*':
                    if j < len(boxGrid[0]):
                        result[j][len(boxGrid) - i - 1] = '*'
                    for c in range(count):
                        result[j - c - 1][len(boxGrid) - i - 1] = '#'
                    count = 0
                elif boxGrid[i][j] == '#':
                    count += 1
        
        return result


        