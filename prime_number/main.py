def prime_number(number):
    is_prime = True
    for i in range(2, number):
        if(number % i == 0):
            is_prime = False
    if (is_prime):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")


prime_number(7)
prime_number(10)
