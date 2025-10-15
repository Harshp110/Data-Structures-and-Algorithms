def longest_subarray_with_sum_k(arr, k):
    n = len(arr)
    max_len = 0

    # Step 1: pick every starting index
    for i in range(n):
        # Step 2: for each start, pick every possible ending index
        for j in range(i, n):
            sum_ = 0  # new subarray sum

            # Step 3: calculate sum of current subarray arr[i..j]
            for m in range(i, j + 1):
                sum_ += arr[m]

            # Step 4: if sum == K → update max_len
            if sum_ == k:
                max_len = max(max_len, j - i + 1)

    return max_len


'''better approach double loop'''
def longest_subarray_with_sum_k(arr, k):
    n = len(arr)
    max_len = 0

    for i in range(n):
        sum_ = 0
        for j in range(i, n):
            sum_ += arr[j]  # keep adding

            if sum_ == k:
                max_len = max(max_len, j - i + 1)

            # because only positives — if sum_ > k → no need to continue
            elif sum_ > k:
                break

    return max_len

'''Optimal Approach'''
def longest_subarray_with_sum_k(arr, k):
    left = 0
    right = 0
    sum_ = 0
    max_len = 0
    n = len(arr)

    while right < n:
        sum_ += arr[right]

        while sum_ > k and left <= right:
            sum_ -= arr[left]
            left += 1
        if sum_ == k:
            max_len = max(max_len, right - left + 1)

        right += 1
    return max_len