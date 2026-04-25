nums = []

while len(nums) != 10:
    num = input(f"Enter {int(len(nums)) + 1} for nums: ")
    nums.append(int(num))

average = sum(nums) / len(nums)

print(f"Total average: {average}")
