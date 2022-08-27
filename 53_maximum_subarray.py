def max_subarray(nums):
    curr_subarr = max_subarr = nums[0]

    for num in nums[1:]:
        curr_subarr = max(num, curr_subarr + num)
        max_subarr = max(max_subarr, curr_subarr)

    return max_subarr
