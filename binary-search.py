def binary_search(list, item):
<<<<<<< HEAD
  low = 0
  high = len(list)-1

  while low <= high:
    mid = (low + high)
    guess = list[mid]
    if guess == item:
      return mid
    if guess > item:
      high = mid-1
    else:
      low = mid+1
  return None
=======
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid-1
        else:
            low = mid+1
    return None

>>>>>>> 9d1e2176c4fea17553bfd28c4fe962ef00b1493c

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
<<<<<<< HEAD
print(binary_search(my_list, -1))
=======
print(binary_search(my_list, -1))
>>>>>>> 9d1e2176c4fea17553bfd28c4fe962ef00b1493c
