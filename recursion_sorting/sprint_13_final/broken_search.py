# 83352056
def broken_search(nums: list, target: int) -> int:
    left: int = 0
    right: int = len(nums) - 1
    while left <= right:
        mid: int = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


if __name__ == '__main__':
    count_array = int(input())
    target_number = int(input())
    numbers_array = [int(num) for num in input().split()]
    print(broken_search(numbers_array, target_number))
