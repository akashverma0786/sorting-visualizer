import time

def merge_sort(arr, drawData, timeTick):
    if len(arr) <= 1:
        return arr
    
    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort both halves
    left_half = merge_sort(left_half, drawData, timeTick)
    right_half = merge_sort(right_half, drawData, timeTick)
    
    # Merge the sorted halves
    merge(arr, left_half, mid, right_half, drawData, timeTick)

def merge(arr, left, middle, right, drawData, timeTick):
    # drawData(arr, colorArray(len(arr), left, middle, right))
    # time.sleep(timeTick)

    result = []
    left_idx, right_idx = 0, 0
    
    while left_idx < len(left) and right_idx < len(right):
        drawData(arr, colorArray(len(arr), left_idx, middle, right_idx))
        time.sleep(timeTick)
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
        drawData(arr, colorArray(len(arr), left_idx, middle, right_idx))
        time.sleep(timeTick)
    
    # Append the remaining elements
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    drawData(arr, ["green" if x >= left_idx and x <= right_idx else "white" for x in range(len(arr))])
    time.sleep(timeTick)
    
    # return result

def colorArray(length, left, middle, right):
    colorArray = []

    for i in range(length):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colorArray.append("yellow")
            else:
                colorArray.append("orange")
        else:
            colorArray.append("white")
    return colorArray