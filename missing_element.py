'''By Brute Force Linear Search'''
def missing_number(arr, N):
    for i in range(1,N+1):
        found = False
        for j in arr:
            if j == i:
                found = True
                break
            if not found:
                return i

'''Better aproach Hashing'''
def missing_no(arr, N):
    hash_arr = [0] * (N + 1)
    for num in arr:
        hash_arr[num] = 1

    for i in range(1, N+1):
        if hash_arr[i] == 0:
            return i
        
'''Optimal aproach Summation method'''
def missing_no_summation(arr,N):
    total = N * (N + 1) // 2
    arr_sum = sum(arr)
    return total - arr_sum