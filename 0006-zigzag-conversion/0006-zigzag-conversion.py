class Solution:
    def convert(self, s: str, numRows: int) -> str:
        final = [""] * numRows
        down = True
        num = 0
        for letter in s:
            if down:
                final[num] += letter
                num = (num + 1) % numRows
            else:
                final[num] += letter
                num = (num - 1) % numRows


            if (num == 0 and down):
                down = False
                num = numRows - 2
            elif (num == 0 and not down):
                down = True
        
        return "".join(final)
        