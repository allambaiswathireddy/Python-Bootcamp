def is_prime(num):
    # Initialize a flag variable
    flag = True

    # Numbers less than 2 are not prime
    if num < 2:
        flag = False
    else:
        # Check for factors from 2 to num-1
        for i in range(2, num):
            if num % i == 0:
                flag = False
                break

    # Return the result based on the flag variable
    return flag

# Example usage
number = int(input())
if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")