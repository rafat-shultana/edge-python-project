def generate_fibonacci(limit):
    fibonacci_sequence = [0, 1]
    while True:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        if next_number > limit:
            break
        fibonacci_sequence.append(next_number)
    return fibonacci_sequence

def main():
    try:
        limit = int(input("Enter the limit for Fibonacci sequence: "))
        if limit <= 0:
            print("Please enter a positive integer.")
            return
        fibonacci_sequence = generate_fibonacci(limit)
        print("Fibonacci sequence up to", limit, ":", fibonacci_sequence)
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

if __name__ == "__main__":
    main()