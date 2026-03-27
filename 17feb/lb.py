# ----------------------------------------
# Logic Builder - FizzBuzz with Counting
# ----------------------------------------

def fizz_buzz_logic(number):
    """
    Returns Fizz, Buzz, FizzBuzz, or the number
    based on divisibility rules.
    """
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)


def main():
    fizz_count = 0
    buzz_count = 0
    fizzbuzz_count = 0

    print("=== FizzBuzz Output (1–50) ===\n")

    for num in range(1, 51):
        result = fizz_buzz_logic(num)
        print(result)

        # Counting occurrences
        if result == "Fizz":
            fizz_count += 1
        elif result == "Buzz":
            buzz_count += 1
        elif result == "FizzBuzz":
            fizzbuzz_count += 1

    print("\n=== Count Summary ===")
    print(f"Total Fizz: {fizz_count}")
    print(f"Total Buzz: {buzz_count}")
    print(f"Total FizzBuzz: {fizzbuzz_count}")


if __name__ == "__main__":
    main()