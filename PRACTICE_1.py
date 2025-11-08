def find_minimum(arr):
    min_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
    return min_val


print(find_minimum([9, 3, 4, 5, 6,]))


def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]


# Calculate the 10th Fibonacci number using both methods
n = 5
recursive_result = fibonacci_recursive(n)
iterative_result = fibonacci_iterative(n)
print(f"The {n}th Fibonacci number (Recursive): {recursive_result}")
print(f"The {n}th Fibonacci number (Iterative): {iterative_result}")
