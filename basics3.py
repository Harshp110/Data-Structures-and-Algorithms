is_logged_in = True
has_premium = False
if is_logged_in and has_premium:
    print("Welcome Premium Player! You have full access.")
if not has_premium and is_logged_in:
    print("Welcome! Upgrade to premium for more features.")
if not is_logged_in:
    print("Please log in to continue.")
    is_logged_in = True
has_premium = False

# Write a program to find the sum of items in the list
list = [1,2,3,4,5]
counter = 0
for i in list:
  counter+= i
  print(counter)

#First GUI
picture = [
    [0,0,0,1,1,0],
    [1,0,1,0,0,0],
    [1,1,1,0,0,1],
    [1,1,0,0,0,0],
    [0,1,0,0,1,0],
    [0,1,0,1,0,1],
    ]
for image in picture:
    for pixel in image:
        if pixel:
            print('*', end="")
        else:
            print(' ', end="")
    print('')  # this goes outside the inner loop
