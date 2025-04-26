# Write a Python function called is_prime(number) that checks whether a given number is a prime number or not.
# A prime number is a number greater than 1 that has no divisors other than 1 and itself.
# Requirements:
# Create a function is_prime(number).
# Use a loop inside the function.
# The function should return True if the number is prime, else return False.
# Then, ask the user to input a number and print whether it's prime or not using your function.


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2,number):
        if number % i == 0:
            return False
    return True
print(is_prime(7))