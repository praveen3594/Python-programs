"""There are total n number of Monkeys sitting on the branches of a huge Tree. As travelers offer Bananas and Peanuts, the Monkeys jump down the Tree. If every Monkey can eat k Bananas and j Peanuts. If total m number of Bananas and p number of Peanuts are offered by travelers, calculate how many Monkeys remain on the Tree after some of them jumped down to eat.
At a time one Monkeys gets down and finishes eating and go to the other side of the road. The Monkey who climbed down does not climb up again after eating until the other Monkeys finish eating.
Monkey can either eat k Bananas or j Peanuts. If for last Monkey there are less than k Bananas left on the ground or less than j Peanuts left on the ground, only that Monkey can eat Bananas(<k) along with the Peanuts(<j).
Write code to take inputs as n, m, p, k, j and return  the number of Monkeys left on the Tree.
    Where, n= Total no of Monkeys
        k= Number of eatable Bananas by Single Monkey (Monkey that jumped down last may get less than k Bananas)
        j = Number of eatable Peanuts by single Monkey(Monkey that jumped down last may get less than j Peanuts)
        m = Total number of Bananas
        p  = Total number of Peanuts
Remember that the Monkeys always eat Bananas and Peanuts, so there is no possibility of k and j having a value zero

Example 1:
Input Values    
20
2
3
12
12

Output Values
Number of  Monkeys left on the tree:10
Note: Kindly follow  the order of inputs as n,k,j,m,p as given in the above example. And output must include  the same format  as in above example(Number of Monkeys left on the Tree:)
For any wrong input display INVALID INPUT"""


n=20
print("Total no of Monkeys",n)  
k= 2 
print("number of eatable Bananas by Single Monkey",k)
j=3 
print("number of eatable peanuts",j)
m =1 
print("Total number of Bananas",m)
p=12 
print("Total number of Peanuts",p)
if(k<=0 and p<=0):
    print("invalid input")



  
for i in range(n):
    if m>=1 or p>=1:
        if(m<k):
            print("\n")
            print("monkey eat bananas")
            p=p-(j-m)
            n=n-1
            
            
            m=0
            print("Remaining bananas",m)
            print("monkey eat peanut")
            print("Remaining peanut",p)
            print("Remaining monkeys",n)
        else:
            m=m-k
            n=n-1
            print("\n")
            print("monkey eat bananas",k)
            print("Remaining bananas",m)
            print("Remaining peanut",p)
            print("Remaining monkeys",n)
        
     
    
