def strength(password):
    count=0
    if(len(password)>=8):
        count+=1
    if any(char.isupper() for char in password):
        count+=1
    if any(char.islower() for char in password):
        count+=1
    if any(char.isdigit() for char in password):
        count+=1
    if any(char in '!@#$%^&*(),.{}|<>' for char in password):
        count+=1

    if count==5:
        print("Very very Strong")
    elif count==4:
        print("Very Strong")
    elif count==3:
        print("Strong")
    elif count==2:
        print("Weak")
    else:
        print("very weak")



password=input("Enter the password : ")
strength(password)



'''
output
Enter the password : hello@1234#
Very Strong'''