'''By Iteration'''
# Step 1: Input array
arr = [2, 5, 1, 3, 0]

# Step 2: Assume first element is the largest
max_element = arr[0]   # ✅ this line defines the variable

# Step 3: Compare each remaining element with max_element
for num in arr[1:]:
    if num > max_element:
        max_element = num    # ✅ update if bigger

# Step 4: Display result
print("Largest element in the array:", max_element)




arr = [10,20,30,5]
largest_element = arr[0]
for num in arr[1:]:
    if num > largest_element:
        largest_element = num

print("Largest element of array is",largest_element)


'''By Recursion'''
def find_largest(arr, n):
    if n == 1:
        return arr[0]
    
    return max(arr[n-1], find_largest(arr, n - 1))

arr = [10,50,80,5]
n = len(arr)
print("Largest element in an array:",find_largest(arr, n))