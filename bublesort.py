def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


array = [int(x) for x in input("Enter the elements of the array, separated by spaces: ").split()]
bubble_sort(array)
print("Sorted array:", array)
