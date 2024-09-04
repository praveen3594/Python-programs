#Stone,Paper,Siscors

"""
import random
c1=0
c2=0


print("Enter 1 for stone\nEnter 2 for paper\nEnter 3 for sissors\nEnter 4 to exit\n..............")
while True:
    n=random.randint(1,3)
    print("\nEnter your number")
    a=int(input())

    if (a==n):
        print("no points")
    elif (a==1 and n==2)or(a==2 and n==3)or(a==3 and n==1):
        c2=c2+1
        print("your number",a,"Systems number",n)
        print("no points")

    elif (a==1 and n==3)or(a==2 and n==1)or(a==3 and n==2):
        c1=c1+1
        print("your number",a,"Systems number",n)
        print("you score")
        
    elif a==4:
        if c1>c2:
            print("Your win....your score",c1, "system's score",c2)
        elif c1==c2:
            print("Tie")
        else:
            print("You lose....your score",c1, "system's score",c2)
        break

    else:
        print("invalid input")
"""

#After reducing space complexity

import random
c1=0
c2=0
print("Enter 0 for stone\nEnter 1 for paper\nEnter 2 for sissors\nEnter >2 to exit\n..............")
while True:
    n=random.randint(0,2)
    print("\nEnter your number")
    a=int(input())


    if(a>=3):
         print("your score",c1, ".....system's score",c2)
         break
         
    elif (a==n):
        print("....Tie....")
        print("your number",a,".....Systems number",n)
        print("your score",c1, ".....system's score",c2)
    elif (a==2 and n==0):
            c2=c2+1
            print("your number",a,".....Systems number",n)
            print("....no points....")
            print("your score",c1, ".....system's score",c2)

    elif (a==0 and n==2):
        

        c1=c1+1
        print("your number",a,".....Systems number",n)
        print("....you score....")
        print("your score",c1, ".....system's score",c2) 

    elif(a<n):
        c2=c2+1
        print("your number",a,".....Systems number",n)
        print("....no points....")
        print("your score",c1, ".....system's score",c2)
        
    elif(a>n):
        c1=c1+1
        print("your number",a,".....Systems number",n)
        print("....you score....")
        print("your score",c1,".....system's score",c2)
    
