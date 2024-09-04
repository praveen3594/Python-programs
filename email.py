
def checkemail(s):
    if s.count('@')==1:
        first,second=s.split('@')
        if (second[-4:]=='.com') and (len(first)>=1):
            print("The email is valid")
        else:
            print("The email is invalid")
    else:
            print("The email is invalid")


s=input("Enter the email address: ")
checkemail(s)

        


'''
output
Enter the email address: abc@gmail.com
The email is valid
'''