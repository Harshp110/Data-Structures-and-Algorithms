def mergeSort(arr,low,high):
    if low >= high:
        return
    
    mid = (low + high)//2
    mergeSort(arr,low,mid)
    mergeSort(arr,mid+1,high)
    merge(arr,low,mid,high)

def merge(arr,low,mid,high):
    temp = []
    left = low
    right = mid +1

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left +=1
        else:
            temp.append(arr[right])
            right +=1
    while left <= mid:
        temp.append(arr[left])
        left += 1

    # Step 3: Copy remaining elements from right half
    while right <= high:
        temp.append(arr[right])
        right += 1

    # Step 4: Put sorted values back into original array
    for i in range(len(temp)):
        arr[low + i] = temp[i]


# Driver Code
arr = [4, 2, 1, 6, 7]
print("Original Array:", arr)

mergeSort(arr, 0, len(arr) - 1)

print("Sorted Array:", arr)   


'''RECURSIVE BUBBLE SORT'''
def bubbleSortRecursive(arr, n):
    if n == 1:
        return

    swapped = False
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swapped = True

    # If no swaps → array already sorted
    if not swapped:
        return

    bubbleSortRecursive(arr, n - 1)


'''RECURSIVE INSERTION SORT'''
def insertionSortRecursive(arr, n, i=0):
    # Base case: when i reaches n, stop
    if i == n:
        return

    # Take the current element
    key = arr[i]
    j = i - 1

    # Shift elements greater than key to the right
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    # Place key at its correct position
    arr[j + 1] = key

    # Recursive call for next element
    insertionSortRecursive(arr, n, i + 1)


# Driver code
arr = [13, 46, 24, 52, 20, 9]
print("Original Array:", arr)

insertionSortRecursive(arr, len(arr))

print("Sorted Array:", arr)


'''QUICK SORT'''
def partition(arr, low, high):
    # Choosing the first element as pivot
    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        # Move i forward until finding an element greater than pivot
        while i <= j and arr[i] <= pivot:
            i += 1
        # Move j backward until finding an element smaller than pivot
        while i <= j and arr[j] > pivot:
            j -= 1
        # If pointers cross, stop
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]  # swap
        else:
            break

    # Place pivot in its correct position
    arr[low], arr[j] = arr[j], arr[low]
    return j  # return pivot’s final index


def quickSort(arr, low, high):
    if low < high:
        # Partition the array and get pivot index
        pi = partition(arr, low, high)

        # Sort left part
        quickSort(arr, low, pi - 1)
        # Sort right part
        quickSort(arr, pi + 1, high)


# Driver code
arr = [4, 6, 2, 5, 7, 9, 1, 3]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array:", arr)
