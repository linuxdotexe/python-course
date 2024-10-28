"""
Day - 7

Linear and Binary Search
"""

#* Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  #* Index of target
    return -1  #* Target not found





# arr = [10, 24, 35, 42, 57, 66]
# target = 35
# result = linear_search(arr, target)
# if result != -1:
#     print(f"Element found at index: {result}")
# else:
#     print("Element not found")

# exit()












#* Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  #* Target found at index
        elif arr[mid] < target:
            low = mid + 1  #* Search the right half
        else:
            high = mid - 1  #* Search the left half

    return -1  #* Target not found

#* Example usage of Binary Search
arr = [5, 12, 19, 26, 34, 40, 50]
target = 34
result = binary_search(arr, target)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found")
