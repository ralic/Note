class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        for index1, value1 in enumerate(num):
            for index2, value2 in enumerate(num[index1:]):
                if (value1+value2) == target:
                    return index1+1, index2+1

if __name__ == '__main__':
    sol = Solution()
    print sol.twoSum([2, 7, 11, 15], 15)