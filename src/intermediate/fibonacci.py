def fibonacci(n):
    
    fibSequence = [0, 1]
    for i in range(2, n):
        next_num = fibSequence[-1] + fibSequence[-2]
        fibSequence.append(next_num)
    return fibSequence

# Print first 10 Fibonacci numbers
print(fibonacci(10))