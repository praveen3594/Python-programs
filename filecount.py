

def count(filename):
    count={}

    with open(filename,'r') as file:
        for line in file:
            words=line.lower().split()
            for word in words:
                word=''.join(char for char in word if char.isalnum())
                if word:
                    if word in count:
                        count[word]+=1
                    else:
                        count[word]=1

    sortedcount = sorted(count.items())

    for i,j in sortedcount:
        print(f'{i}:{j}')




filename=input("Enter the filename : ")
count(filename)



'''
output

Enter the filename : C:\Users\prave\OneDrive\Desktop\WorkingFolders\Cognifyz\Level 2\file1.txt
bye:1
everybody:1
guys:1
hai:2
hello:2
'''