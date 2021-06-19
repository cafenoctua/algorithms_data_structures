def QuickSort(data: list, left: int, right: int):
    if right - left <= 1: return

    # set pivot
    pivot_index = int((left + right) / 2)
    pivot = data[pivot_index]
    # swap pivot number to last index
    data[pivot_index], data[right - 1] = data[right - 1], data[pivot_index]

    i = left
    for j in range(left, right):
        if data[j] < pivot:
            data[i], data[j] = data[j], data[i]
            i += 1

    data[i], data[right - 1] = data[right - 1], data[i]

    QuickSort(data, left, i)
    QuickSort(data, i + 1, right)

    return data

if __name__ == "__main__":
    a = [10, 12, 15, 3, 8, 17, 4, 1]
    print(QuickSort(a, 0, len(a)))