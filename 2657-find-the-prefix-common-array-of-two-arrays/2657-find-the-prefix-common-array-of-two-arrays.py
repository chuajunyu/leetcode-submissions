class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        result = []
        count = 0
        seen = [0] * len(A)
        for i in range(len(A)):
            a = A[i]
            b = B[i]
            seen[a - 1] += 1
            seen[b - 1] += 1
            if a == b:
                count += 1
            else:
                if seen[a - 1] == 2:
                    count += 1
                if seen[b - 1] == 2:
                    count += 1
            result.append(count)
        return result
        