

def power_set(nums):
    temp = []

    def backtrack(start, path):
        temp.append(path)

        for i in range(start, len(nums)):
            backtrack(i + 1, path + [nums[i]])

    backtrack(0, [])

    return temp


print(power_set([1, 2, 3]))
