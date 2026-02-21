def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

user_num = int(input("Enter a number: "))
print(f"Factorial of {user_num} is: {factorial(user_num)}")