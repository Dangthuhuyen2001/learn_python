"""Max Consecutive Ones"""
def findMaxConsecutiveOnes(nums):
    maxLength = 0
    count = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
            maxLength = max(maxLength, count)
        else:
            count = 0
    return maxLength



if __name__ == '__main__':
    nums = [1, 1, 0, 1, 1, 1]
    print(findMaxConsecutiveOnes(nums))