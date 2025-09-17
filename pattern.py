N = int(input("Enter N:"))
for i in range(N):
    print("*" * N)
    '''
    ***
    ***
    ***'''


n = int(input("Enter n"))
for i in range(0,n+1):
    print("*"*i)
    '''
    *
    **
    ***
    '''

x = int(input("ENter x"))
for i in range(1,x+1):
    for j in range(1,i+1):
       print(j,end = "")
       print()


q = int(input("Enter the value of q"))
for i in range(1,n+1):
    for j in range(1,i+1):
       print(i,end = "")
       print()

k = int(input("Enter the value of k"))
for i in range(n,0,-1):
    print("*"*i)
    '''
*****
****
***
**
*'''

u = int(input("Enter the value of u"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()
    '''
12345
1234
123
12
1'''

n = int(input("Enter the value of n: "))

for i in range(1, n+1):
    print(" " * (n - i) + "*" * (2*i - 1))

    '''
     *
    ***
   *****
  *******
 *********
***********'''

n = int(input("Enter the value of n:"))
for i in range(n,0,-1):
    print(" "*(n-i)+ "*"*(2*i-1))
    '''
    Enter the value of n:5
*********
 *******
  *****
   ***
    *
    '''
n = int(input("Enter the value of n: "))

# Top half
for i in range(1, n+1):
    print(" " * (n-i) + "*" * (2*i-1))

# Bottom half
for i in range(n-1, 0, -1):
    print(" " * (n-i) + "*" * (2*i-1))
    '''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *'''

n = int(input("Enter the value of n:"))

# Increasing
for i in range(1, n+1):
    print("*" * i)

# Decreasing
for j in range(n-1, 0, -1):
    print("*" * j)

n = int(input("Enter n: "))

for i in range(1, n+1):         # rows
    for j in range(1, i+1):     # columns in that row
        value = (i + j + 1) % 2
        print(value, end=" ")
    print()
