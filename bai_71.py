def twoSum(nums, target):
    h = {}
    for i, num in enumerate(nums):
        n = target - num
        if n not in h:
            h[num] = i
        else:
            return [h[n], i]


nums = [1,2,5,4,6,1,4,6,4,1,4]
target = 9
print(twoSum(nums, target))


