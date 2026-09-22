class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        total_count = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
                if count != 0 and total_count < count:
                    total_count = count
                # print(f"i: " + str(i))
                print(f"count: " + str(count))
                print(f"total_count: " + str(total_count))
            else:
                count = 0
        return total_count