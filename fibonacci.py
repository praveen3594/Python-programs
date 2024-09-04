first=0
second=1
n=int(input("Number of terms : "))
for i in range(n):
    print(first)
    sum=first+second
    first=second
    second=sum



'''
output

Number of terms : 8
0
1
1
2
3
5
8
13
'''