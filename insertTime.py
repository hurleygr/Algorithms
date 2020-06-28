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
def insert_sort(nums):
    for i in range(1, len(nums)):
        cur = nums[i]
        j = i
        while j > 0 and int(nums[j - 1]) < int(cur):
            nums[j] = nums[j - 1]
            j -= 1
        nums[j] = cur


def compare_sort(algo=insert_sort):
    list_sizes = list(range(5000, 40000, 5000))
    times = []
    for list_size in list_sizes:
        rand_list = [random.randrange(1, 10001) for _ in range(list_size)]
        t = algo(list(rand_list))
        times.append(t)
        print(list_size, t)


compare_sort()
