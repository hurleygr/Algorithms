def mergesort():
    """ Sorts array of numbers in descending order using merge sort"""
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

    infile = 'data.txt'
    outfile = open('merge.out', 'w')

    with open(infile, 'r') as file:
        line = file.readline()
        while line:
            inputs = line.split()
            nums = inputs[1:]
            merge_sort(nums)
            sorted_line = ' '.join(nums) + '\n'
            outfile.write(sorted_line)
            line = file.readline()