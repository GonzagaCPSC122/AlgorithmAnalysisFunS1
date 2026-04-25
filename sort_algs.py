def selection_sort(array: list[int]) -> None:
    n = len(array)
    i = 0
    while i < n - 1:
        min_index = i
        min_value = array[i]
        j = i + 1
        while j < n:
            if array[j] < min_value:
                min_value = array[j]
                min_index = j
            j += 1
        array[min_index] = array[i]
        array[i] = min_value
        i += 1

def bubble_sort(array: list[int]) -> None:
    # TODO: add early exit
    n = len(array)
    i = n - 1
    while i > 0:
        j = 0
        while j < i:
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
            j += 1
        i -= 1

def insertion_sort(array: list[int]) -> None:
    n = len(array)
    i = 1
    while i < n:
        curr_value = array[i]
        j = i - 1
        while j >= 0 and curr_value < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = curr_value
        i += 1

# added on 4/25/26
# based on Goodrich 12.2
def merge(s1: list[int], s2: list[int], s: list[int]) -> None:
    # merge two sorted lists s1 and s2 into list s
    i = j = 0
    while i + j < len(s):
        if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
            # copy ith element of s1 as next item of s
            s[i + j] = s1[i]
            i += 1
        else:
            # copy jth element of s2 as next item of s
            s[i + j] = s2[j]
            j += 1

def merge_sort(s: list[int]) -> None:
    n = len(s)
    if n < 2:
        return
    # divide
    mid = n // 2
    s1 = s[0: mid]
    s2 = s[mid: ]
    # conquer
    merge_sort(s1)
    merge_sort(s2)
    
    merge(s1, s2, s)

# based on Goodrich 12.3
def quick_sort(s: list[int]) -> None:
    n = len(s)
    if n < 2:
        return
    # divide
    p = s[-1]
    l = [] # for less than pivot
    e = []  # for equal to pivot
    g = [] # for greater than pivot
    for i in range(len(s)):
        if s[i] < p:
            l.append(s[i])
        elif s[i] > p:
            g.append(s[i])
        else:
            e.append(s[i])
    # conquer
    quick_sort(l)
    quick_sort(g)
    # concatenate results (copy sorted order over into s)
    i = 0
    for j in range(len(l)):
        s[i] = l[j]
        i += 1
    for j in range(len(e)):
        s[i] = e[j]
        i += 1
    for j in range(len(g)):
        s[i] = g[j]
        i += 1

# based on Goodrich 12.3
def inplace_quick_sort(s: list[int], a: int, b: int) -> None:
    if a >= b:
        # range is trivially sorted
        return 
    
    pivot = s[b] # last element of range is pivot
    left = a # will scan rightward
    right = b - 1 # will scan leftward
    while left <= right:
        # scan until reach value equal or larger than pivot (or right marker)
        while left <= right and s[left] < pivot:
            left += 1
        # scan until reach value equal or smaller than pivot (or left marker)
        while left <= right and pivot < s[right]:
            right -= 1
        if left <= right:
            # scans did not strictly cross
            s[left], s[right] = s[right], s[left] # swap values
            left, right = left + 1, right -1 # shrink range
        
        # put pivot in final place (currently marked by left index)
        s[left], s[b] = s[b], s[left]
        # make recursive calls
        inplace_quick_sort(s, a, left - 1)
        inplace_quick_sort(s, left + 1, b)

if __name__ == "__main__":
    nums = [7, 4, 6, 9, 10, 2, 5, 3, 8]
    nums2 = [7, 4, 6, 9, 10, 2, 5, 3, 8]
    nums3 = [7, 4, 6, 9, 10, 2, 5, 3, 8]
    nums4 = [7, 4, 6, 9, 10, 2, 5, 3, 8]
    nums5 = [7, 4, 6, 9, 10, 2, 5, 3, 8]

    print(nums)
    print("Selection Sort")
    selection_sort(nums)
    print(nums)

    print("Bubble Sort")
    bubble_sort(nums2)
    print(nums2)

    print("Insertion Sort")
    insertion_sort(nums3)
    print(nums3)

    print("Merge Sort")
    merge_sort(nums4)
    print(nums4)

    print("Quick Sort")
    # inplace_quick_sort(nums5, 0, len(nums5) - 1)
    quick_sort(nums5)
    print(nums5)
