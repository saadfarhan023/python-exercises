def get_input():
    nums = []
    while True:
        num = input(f"Enter {int(len(nums)) + 1} for nums: ")
        if num == "done":
            break
        nums.append(int(num))
    return nums


def print_data(nums):
    print(max(nums))
    print(min(nums))
    print(sum(nums) / len(nums))


nums = get_input()
print_data(nums)
