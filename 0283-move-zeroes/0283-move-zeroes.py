class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        j = 0 # Pointer to place the next non-zero element
        for i in range(len(nums)):
            if nums[i] != 0:
                # Swap current element with the element at index j 
                nums[i], nums[j] = nums[j], nums[i]
                j += 1 # Move j to the next index for placing non-zero
        # first_zero, first_free = 0, 0

        # # initialise first zero
        # for i, n in enumerate(nums):
        #     if n == 0:
        #         first_zero = i
        #         break

        # # initialised first_free
        # for j, n in enumerate(nums[i + 1:]):
        #     if n != 0:
        #         first_free = first_zero + j + 1
        #         break
        
        # if first_zero > first_free:
        #     return


        # while first_free < len(nums):
        #     nums[first_zero], nums[first_free] = nums[first_free], nums[first_zero]

        #     # progress the first zero to the next zero
        #     while nums[first_zero] != 0:
        #         first_zero += 1

        #         if first_zero >= len(nums) - 1:
        #             return

        #     # progress the first_free to the next first free
        #     first_free = first_zero
        #     while nums[first_free] == 0:
        #         first_free += 1

        #         if first_free > len(nums) - 1:
        #             return