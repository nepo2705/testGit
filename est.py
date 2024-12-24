import random

def generate_random_numbers(count, start, end):
    return [random.randint(start, end) for _ in range(count)]

def main():
    count = 10
    start = 1
    end = 100
    random_numbers = generate_random_numbers(count, start, end)
    print(f"Generated {count} random numbers between {start} and {end}:")
    print("Sum of random numbers:", sum(random_numbers))
    print("Average of random numbers:", sum(random_numbers) / count)
    print("Maximum random number:", max(random_numbers))
    print("Minimum random number:", min(random_numbers))
    print(random_numbers)

if __name__ == "__main__":
    main()