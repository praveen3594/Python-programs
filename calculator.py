
x=input("Choose your operation *,+,-,/,%  : ")
a=int(input("Enter the first number "))
b=int(input("Enter the second number "))

if x=='+':
    print(a+b)

elif x=='-':
    print(a-b)

elif x=='*':
    print(a*b)

elif x=='/':
    if b!=0:
        print(a/b)
    else:
        print("Division by zero")

elif x=='%':
    print(a%b)
else:
    print("invalid operator")


  
    
'''
output
Choose your operation *,+,-,/,%  : +
Enter t
he first number 4
Enter the second number 5
9'''