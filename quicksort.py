def quicksort(arr, begin, end):
    if end - begin > 1:
        p = partition(arr, begin, end)
        quicksort(arr, begin, p)
        quicksort(arr, p + 1, end)


def partition(arr, begin, end):
    pivot = arr[begin]
    i = begin + 1
    j = end - 1

    while True:
        while i <= j and arr[i] <= pivot:
            i = i + 1
        while i <= j and arr[j] >= pivot:
            j = j - 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            arr[begin], arr[j] = arr[j], arr[begin]
            return j


arr = input('Enter1 the list of numbers to be Sorted: ').split()
arr = [int(x) for x in arr]
quicksort(arr, 0, len(arr))
print('Sorted list: ', end='')
print(arr)
