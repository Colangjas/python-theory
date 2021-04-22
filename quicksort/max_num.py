def highest(arr):
    l = len(arr)
    if not arr:
        return 'Not an array'
    if l <= 1:
        return arr[0]
    else:
        new_arr = arr
        if arr[0] < arr[1]:
            new_arr.pop(0)
            return highest(new_arr)
        else:
            new_arr.pop(1)
            return highest(new_arr)



print(highest([2,4,6]))