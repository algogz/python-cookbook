def quick_sort(arr):
    if len(arr) < 2:
        return arr
    base = arr[0]
    left_arr = [x for x in arr[1:] if x <= base]
    right_arr = [x for x in arr[1:] if x > base]

    left_sorted = quick_sort(left_arr)
    right_sorted = quick_sort(right_arr)

    return left_sorted + [base] + right_sorted


test_arr = [3, 10, 5, 2, 3, 2, 1, 3]
print(quick_sort(test_arr))
