import random

n=random.randint(1,100)
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
    
    Enter your guess 50
too low
Enter your guess 60
too high
Enter your guess 55
too low
Enter your guess 57
too high
Enter your guess 56
Correct guess
Enter your guess
'''