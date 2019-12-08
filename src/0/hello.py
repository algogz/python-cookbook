def find_the_num(width, length):
    print(f"width={width}, length={length}")
    if length > width:
        width, length = length, width
    if width % length == 0:
        return length
    else:
        width, length = length, width % length
        return find_the_num(width, length)

def recurse_sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        a, *b = arr
        return a + recurse_sum(b)

# print(find_the_num(1680, 640))
print(recurse_sum([1,2,3]))
