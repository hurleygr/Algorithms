def insertsort():
    """ Sorts array of numbers in descending order using insertion sort"""
    def insert_sort(nums):
        for i in range(1, len(nums)):
            cur = nums[i]
            j = i
            while j > 0 and int(nums[j-1]) < int(cur):
                nums[j] = nums[j-1]
                j -= 1
            nums[j] = cur

    infile = 'data.txt'
    outfile = open('insert.out', 'w')

    with open(infile, 'r') as file:
        line = file.readline()
        while line:
            inputs = line.split()
            nums = inputs[1:]
            insert_sort(nums)
            sorted_line = ' '.join(nums) + '\n'
            outfile.write(sorted_line)
            line = file.readline()