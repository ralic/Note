class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        if num1 < 0 or num2 < 0:
            return None
        if num1 == 0 or num2 == 0:
            return "0"
        resultlist = []