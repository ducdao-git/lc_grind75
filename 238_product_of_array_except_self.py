def product_except_self(nums):
    return_num = [1]

    for i in range(1, len(nums)):
        return_num.append(return_num[i - 1] * nums[i - 1])

    reverse = 1
    for i in range(len(nums) - 2, -1, -1):
        reverse *= nums[i + 1]
        return_num[i] *= reverse

    return return_num


print(product_except_self([2, 3, 4, 5]))
