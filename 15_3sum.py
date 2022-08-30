def three_sum(nums):
    nums = sorted(nums)
    result = set()

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            curr_sum = nums[i] + nums[lo] + nums[hi]

            if curr_sum == 0:
                result.add((nums[i], nums[lo], nums[hi]))
                lo += 1
                hi -= 1

            elif curr_sum > 0:
                hi -= 1

            else:
                lo += 1

    return result
