

n=int(input("Enter number of terms"))
if n > 0:
    first = 0
    second = 1
    sequence_sum = 0
    next_num = second
    print(first)
    sequence_sum += first
    


    def fibonacci(next_num):
        print(next_num)
        sequence_sum += next_num
        first, second = second, next_num
        while n>0:
            return(fibonacci(next_num = first + second))
    
    