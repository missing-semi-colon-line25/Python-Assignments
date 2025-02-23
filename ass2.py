def sum_of_digits(n):
    total_sum = 0
    while n > 0:
        total_sum += n % 10
        n //= 10
    return total_sum


def digital_root(n):
    while n >= 10:
        n = sum_of_digits(n)
    return n


numbers = []
digit_sums = []

while True:
    user_input = int(input("Enter a number, enter '0' to exit: "))

    if user_input == 0:
        break

    numbers.append(user_input)
    digit_sums.append(digital_root(user_input))

print("Numbers entered:", numbers)
print("Sum of digits(until single digit is reached) of each number:", digit_sums)
