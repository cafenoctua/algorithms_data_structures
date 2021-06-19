def MergeSort(data: list, left: int, right: int):
    if right - left == 1: return
    mid: int = int(left + (right - left) / 2)

    # left side sort
    MergeSort(data, left, mid)
    # right side sort
    MergeSort(data, mid, right)

    # Copy left and right sorted results.
    buf = []
    for i in range(left, mid): buf.append(data[i])
    for i in range(right-1, mid-1, -1): buf.append(data[i])

    # merge
    index_left = 0
    index_right = len(buf) - 1

    for i in range(left, right):
        # adopt left
        if buf[index_left] <= buf[index_right]:
            data[i] = buf[index_left]
            index_left += 1
        # adopt right
        else:
            data[i] = buf[index_right]
            index_right -= 1

    return data
        
if __name__ == "__main__":
    a = [12, 9, 15, 3, 8, 17, 6, 1]
    print(MergeSort(a, 0, len(a)))


