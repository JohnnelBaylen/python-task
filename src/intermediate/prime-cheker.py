def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Test the function
number = 11
print(f"{number} is a prime number: {isPrime(number)}")