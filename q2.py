"""Joseph is learning digital logic subject which will be for his next semester. He usually tries to solve unit 
assignment problems before the lecture. Today he got one tricky question. The problem statement is “A 
positive integer has been given as an input. Convert decimal value to binary representation. Toggle all bits of 
it after the most significant bit including the most significant bit. Print the positive integer value after toggling 
all bits”.
Constraints :
1<=N<=100
Example 1:
Input :
10 -> Integer
Output :
5 -> result- Integer"""


def toggle_bits(n):
    return n ^ ((1 << n.bit_length()) - 1)

input_n = 12
output = toggle_bits(input_n)
print(output)  # Output: 5


    