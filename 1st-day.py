# DAY 1

# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

# Since the result may be very large, so you need to return a string instead of an integer.

 

# Example 1:

# Input: nums = [10,2]
# Output: "210"


from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        # Custom comparator function
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0

        # Convert all numbers to strings for comparison
        nums = list(map(str, nums))

        # Sort with the custom comparator
        nums.sort(key=cmp_to_key(compare))

        # Join the sorted numbers
        largest_num = ''.join(nums)

        # Handle the case where the numbers are all zeros
        if largest_num[0] == '0':
            return '0'
        
        return largest_num

# Example usage
if __name__ == "__main__":
    solution = Solution()  # Create an instance of the Solution class
    nums = [3, 30, 34, 5, 9]  # Input list of numbers
    print(solution.largestNumber(nums))  # Output: "9534330"
