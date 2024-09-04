n=int(input("Enter 1 to convert celsius to Farenheit\nEnter 2 to convert Farenheit to celsius\nEnter your choice :"))

if(n==1):
    c=int(input("Enter the temperature in celsius "))
    print(" Temperature in Farenheit ",c*(9/2)+32)
else:
     f=int(input("Enter the temperature in Farenheit "))
     print(" Temperature in celsius ",(5/9)*(f-32))





'''
output
Enter 1 to convert celsius to Farenheit
Enter 2 to convert Farenheit to celsius
Enter your choice :1
Enter the temperature in celsius 20
Temperature in Farenheit  122.0
 '''