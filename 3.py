nums = []

while True:
    num = input(f"Enter {int(len(nums)) + 1} for nums: ")
    if num == "done":
        break
    nums.append(int(num))

print(max(nums))
print(min(nums))
print(sum(nums) / len(nums))
