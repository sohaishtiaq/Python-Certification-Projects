def selection_sort(my_list):
    length = len(my_list)
 
    for i in range(length - 1):
        min_index = i

        for j in range(i+1,length):
            if my_list[j] < my_list[min_index]:
                min_index = j

        if min_index != i:
            my_list[i], my_list[min_index] = my_list[min_index], my_list[i]

    return my_list
