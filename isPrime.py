def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

PRIME_CONST = "ES PRIMO";
NOT_PRIME_CONST = "NO ES PRIMO";
NUMBER_TO_TEST=3;


if is_prime(NUMBER_TO_TEST):
    print(PRIME_CONST)
else:
     print(NOT_PRIME_CONST);