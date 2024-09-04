s=input("Enter a string: ")
i=0
j=len(s)-1
flag=0
while (i<j):
    if s[i]!=s[j]:
        flag=1
        break
    else:
        i=i+1
        j=j-1
if flag==1:      
    print("Not Palindrome")
else:
    print("Palindrome")




    '''
    output
    Enter a string: apple
    Not Palindrome'''