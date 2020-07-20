'''
Given an array content n + 1 numbers
Each elenment of array start form 0 to n
Find the only duplicate number

'''

def floyd_algorithm(nums):
    tortoise , hare = num[0], nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
    return ptr1

def find_duplicate(arr):
    for i in range(len(arr)):
        if (arr[abs(arr[i]) - 1] < 0):
            return abs(arr[i])
        else:
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]