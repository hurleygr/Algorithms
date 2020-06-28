import time
import random


def time_decorator(func):
    def wrapper(*args):
        start = time.perf_counter()
        func(*args)
        end = time.perf_counter()
        return end - start

    return wrapper


@time_decorator
def merge_sort(nums):
    # base case is singleton array
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        # recurse on left and right subarrays
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        # merge left and right to rebuild in descending order
        while i < len(left) and j < len(right):
            if int(left[i]) > int(right[j]):
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1


def compare_sort(algo=merge_sort):
    list_sizes = list(range(5000, 40000, 5000))
    times = []
    for list_size in list_sizes:
        rand_list = [random.randrange(1, 10001) for _ in range(list_size)]
        t = algo(list(rand_list))
        times.append(t)
        print(list_size, t)


compare_sort()