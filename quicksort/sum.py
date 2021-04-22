def arr_sum(arr):
    l = len(arr)
    if l <= 1:
        return arr[0]
    else:
        new_arr = arr
        new_arr.append(new_arr[0]+new_arr[1])
        new_arr.pop(0)
        new_arr.pop(0)
        return arr_sum(new_arr)

print(arr_sum([2,4,6]))