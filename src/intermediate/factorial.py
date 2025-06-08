def factorial(n):
    
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

while True:
    num = int(input("Enter factorial :  "))
    print("\nResult : \n")
    print(f" The factorial of {num} is {factorial(num)}\n")
