def quick_sort(arr):

    if len(arr) <= 1:
        return arr[:]

    pivot = arr[0]

    left_part = []
    middle_part = []
    right_part = []
    
    for num in arr:
        if num < pivot:
            left_part.append(num)
        elif num > pivot:
            right_part.append(num)
        else:
            middle_part.append(num)

    return quick_sort(left_par
