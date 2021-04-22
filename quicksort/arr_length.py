def arr_length(arr):
    if not arr:
        return 0
    else:
        new_arr = arr
        new_arr.pop(0)
        return arr_length(new_arr) + 1


print(arr_length([2,4,6]))