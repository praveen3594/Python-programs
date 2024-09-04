#find the frequency of digits in a number

a=[1,1,2,2,1,3]


def find_digit_frequencies(my_list):
    # Initialize an empty dictionary to store frequencies
    freq = {}

    for item in my_list:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    # Print the frequencies
    for key, value in freq.items():
        print(f"{key}: {'X ' * value}")

# Example usage
find_digit_frequencies(a)
