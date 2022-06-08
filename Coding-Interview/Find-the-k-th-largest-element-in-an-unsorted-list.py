# [Google Interview Question] Find the k-th Largest Element in an Unsorted List
import bisect
import math

lst = [1, 2, 3, 4, 5]
k = 2


def find_k_largest_element_a(nums, k):
    sorted_nums = sorted(nums, reverse=True)
    # index starts from 0, index = position - 1
    return sorted_nums[k-1]


'''
RUNTIME
n --> O(n log n)
'''
# solution 2


def find_k_largest_element_b(nums, k):
    for _ in range(k-1):
        nums.remove(max(nums))
    return max(nums)


'''
RUNTIME
n --> O(k n)
'''


def find_k_largest_element(nums, k):
    n = len(nums)
    # print(math.log(n, 2))
    if k > math.log(n, 2):
        return find_k_largest_element_a(nums, k)
    else:
        return find_k_largest_element_b(nums, k)


'''
RUNTIME
n --> O(min(log(n),k) * n)
'''

print(find_k_largest_element(lst, k))


# Solution 3 - use bisect


def find(nums, k):
    window = nums[k:]
    for element in nums[k:]:
        if element > window[0]:
            # Remove minimum element from window
            window.pop(0)
            # Sorted insert of new element
            bisect.insort(window, element)
    return window[0]


print(find(lst, k))
'''
RUNTIME
n --> O((n-k) * log k)
'''
