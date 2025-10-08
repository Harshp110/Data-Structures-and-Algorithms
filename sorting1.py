'''Selection Sort'''
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # swap
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [13, 46, 24, 52, 20, 9]
selection_sort(arr)
print("Sorted array:", arr)

'''BASIC BUBBLE SORT'''
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1] , arr[j]
arr = [20,30,40,10]
bubble_sort(arr)
print("Sorted array:",arr)


'''INSERTION SORT'''
def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
arr = [20,50,45,98]
insertion_sort(arr)
print("Sorted array is",arr)
            