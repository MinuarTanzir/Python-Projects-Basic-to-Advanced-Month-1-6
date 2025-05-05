#Write a Python program that checks if a number is positive, negative, or zero.

try:
    number = float(input("Enter a number: "))

    # Check the number
    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")
except ValueError:
    print("Invalid input! Please enter a numeric value.")