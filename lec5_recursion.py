'''printing n times'''
def rec(n):
    if n == 0:
       return
    print("Harsh")
    rec(n-1)
rec(5)
def iit(n):
    if n == 0:
        return
    print("Harsh in iit")
    iit(n-1)
iit(69)

'''Print Numbers from 1 to n'''
def number(n):
    if n == 0:
        return
    number(n-1)
    print(n)
number(10)

'''Print Numbers from N to 1'''
def reverse(n):
    if n == 0:
        return
    print(n)
    reverse(n-1)
reverse(10)

'''Sum of first n natural numbers USING RECURSION'''
def sumnat(n):
    if n == 0:
        return 0
    return n + sumnat(n-1)
print(sumnat(10))

'''Sum of first n natural numbers using formula'''
def sum(n):
    return n* (n+1)//2
print(sum(10))

'''Factorial using iterative methods'''
def factorial_iterative(n):
    fact = 1
    for i in range(1, n+1): 
        fact *= i
    return fact

print(factorial_iterative(5)) 

'''Factorial using Recursion'''
def fact(n):
    if n == 0 or n == 1:   
        return 1
    return n * fact(n-1)   
print(fact(5))

'''Reverse an Array by iteration'''
def reverse_iterative(arr):
    start, end = 0, len(arr)-1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]  # swap
        start += 1
        end -= 1
    return arr

print(reverse_iterative([1,2,3,4,5]))   # [5,4,3,2,1]

'''Reverse an array by Recursion'''
def reverse_recr(arr,start,end):
    if start >= end:
        return
    arr[start], arr[end] = arr[end],arr[start]
    reverse_recr(arr, start+1, end-1)
arr = [1,2,3,4,5]
reverse_recr(arr, 0, len(arr)-1)
print(arr)

'''Using built in'''
arr = [1,2,3,4,5]
print(arr[::-1])