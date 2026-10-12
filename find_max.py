#problem 2: find max in a list
# nums[0, 5, 9, 10,1]
# output= 10


def find_max(nums):            # declare a function named find_max with (nums) as a parameter
    biggest = nums[0]          # "remember the biggest so far"
    for n in nums:             # "look at each number"
        if n > biggest:        # "if current is bigger"
            biggest = n        # "that's the new biggest"
    return biggest