# Problem 4: sum_evens(nums)
# Add up only the even numbers in a list.
#sum_evens(nums): add up only the even numbers.
#[1, 2, 3, 4, 6] → 12

def even_sum(nums):
    total=0
    for n in nums:
        if n % 2 == 0:
            total += n
    return total

assert even_sum([1,2,3,4,6]) == 12
assert even_sum([1,3,5]) == 0
assert even_sum([]) == 0
assert even_sum([-4,2]) == -2
print("passed all tests")
