import random

i=int(input("Enter the starting range "))
j=int(input("Enter the ending range "))
n=random.randint(i,j)
m=int(input("Enter your guess "))
while True:
    if m==n:
        print("Correct guess")
    elif n<m:
        print("too high")
    else:
        print("too low")
    m=int(input("Enter your guess "))



'''
output

Enter the starting range 2
Enter the ending range 20
Enter your guess 5
too low
Enter your guess 8
too low
Enter your guess 12
too low
Enter your guess 17
too high
Enter your guess 15
Correct guess
Enter your guess 
'''