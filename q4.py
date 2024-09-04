
a=["1","2","3","4"]
for i in a:
    print(i)
print("Enter number of times")
n=int(input())
for i in range(n):
    t=a[0]
    a[0]=a[1]
    a[1]=a[2]
    a[2]=a[3]
    a[3]=t
print("new array after left rotation")
for i in a:
        print(i)