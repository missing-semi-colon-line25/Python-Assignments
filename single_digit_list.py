def sum_of_digits(n):
    total_sum = 0
    while n > 0:
        total_sum += n % 10
        n //= 10
    return total_sum


numbers = []
digit_sums = []

while True:
    user_input = int(input("Enter a number , enter single digit to stop: "))

    digit_sum = sum_of_digits(user_input)

    if user_input == digit_sum:
        break

    numbers.append(user_input)
    digit_sums.append(digit_sum)

print("Numbers entered:", numbers)
print("Sum of digits for each number:", digit_sums)
