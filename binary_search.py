def binary_search(arr,key):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] < key:
            low = mid+1
        elif arr[mid] > key:
            high = mid-1
        else:
            return mid
    return False
    

arr = [1,2,3,4,5,6,7,8,9]
key = 2
pos = binary_search(arr,key)
if pos:
    print(f'The searched key {key} is at location: {pos}')
else:
    print('key not found')