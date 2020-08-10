def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        arr = []
        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                arr.append(left[0])
                left.pop(0)
            else:
                arr.append(right[0])
                right.pop(0)

        for i in left:
            arr.append(i)

        for i in right:
            arr.append(i)

    return arr


arr = [1,4,2,7,4,8,9,5]
print(merge_sort(arr))