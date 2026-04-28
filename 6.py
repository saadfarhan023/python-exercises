def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    
    return True

num_to_check = int(input("Enter a number to check if is prime: "))
result = is_prime(num_to_check)

print(result)