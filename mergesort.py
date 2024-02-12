

def merge_sort(data, drawData, timeTick):
    merge_sort_algo(data, 0, len(data) - 1, drawData, timeTick)

def merge_sort_algo(data, left, right, drawData, timeTick):
    if left < right:
        middle = (left + right) // 2
        merge_sort_algo(data, left, middle, drawData, timeTick)
        merge_sort_algo(data, middle + 1, right, drawData, timeTick)
        merge(data, left, middle, right, drawData, timeTick)

def merge(data, left, middle, right, drawData, timeTick):
    leftPart = data[left : middle + 1]
    rightPart = data[middle + 1 : right + 1]

    leftIdx = rightIdx = 0

    for dataIdx in range(left, right):
        if leftIdx < len(leftPart) and rightIdx < len(rightPart):
            if leftPart[leftIdx] < rightPart[rightIdx]:
                data[dataIdx] = leftPart[leftIdx]
                leftIdx += 1
            else:
                data[dataIdx] = rightPart[rightIdx]
                rightIdx += 1

        elif leftIdx < len(leftPart):
            data[dataIdx] = leftPart[leftIdx]
            leftIdx += 1

        else:
            data[dataIdx] = rightPart[rightIdx]
            rightIdx += 1

data = [1, 4, 6, 4, 56, 76, 56, 899, 88, 99, 45, 567, 7, 9, 2, 5, 6, 5]
merge_sort(data, 0, 0)
print(data)