'''reversing a number'''
def reversenumber(n):
    rev = 0
    while n>0:
        last_digit = n % 10
        rev = rev*10 + last_digit
        n = n//10
    return rev
print(reversenumber(1234))
print(reversenumber(10010))

'''counting digits'''
def count_digits(n):
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    while n>0:
        n//=10
        count +=1
    return count
print(count_digits(1001))
'''check palindrome'''
def check_palindrome(n):
    original = n
    rev = 0

    while n > 0:
        last_digit = n%10
        rev = rev * 10 + last_digit
        n = n//10
    return original == rev
print(check_palindrome(121))
print(check_palindrome(1233))

'''reverse'''
def reverse(n):
    rev = 0
    while n>0:
        last_digit = n % 10
        rev = rev*10 + last_digit
        n = n // 10
    return rev
print(reverse(10011))

'''gcd by brute force'''
def gcd_bruteforce(n1,n2):
    gcd = 1
    for i in range(1,min(n1,n2)+1):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i
        return gcd
print(gcd_bruteforce(2,6))

'''gcd by better approach'''
def gcd_better(n1, n2):
    for i in range(min(n1, n2), 0, -1):  # start from smaller number
        if n1 % i == 0 and n2 % i == 0:  # if i divides both
            return i                      # first one found = GCD

# Test
print(gcd_better(20, 15))  # Output: 5

'''Armstrong Number'''
def is_armstrong(n):
    original = n
    sum_of_powers = 0
    n_digits = len(str(n))
    while n>0:
        digit = n % 10
    sum_of_powers += digit ** n_digits
    n = n//10
    return sum_of_powers == original
print(is_armstrong(153))
print(is_armstrong(9474))
print(is_armstrong(123))

'''print all divisors'''
def print_divisors(n):
    divisors = []
    for i in range(1,n+1):
        if n%i == 0:
            divisors.append(i)
    return divisors
N = 12
print("Divisors of",N,"are:",print_divisors(N))

'''Prime number'''
import math
def is_prime(n):
    if n <=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
        return True
print(is_prime(2))
print(is_prime(11))
print(is_prime(23))