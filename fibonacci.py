import argparse


def calculate_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for i in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fibonacci sequence calculator")
        
    parser.add_argument(
            "-n",
            type=int,
            help="Calculate the n-th Fibonacci number. n starts from 0."
        )
    parser.add_argument(
            "-s",
            type=int,
            help="Generate the Fibonacci sequence up to n terms"
        )
    args = parser.parse_args()

    if args.n is None and args.s is None:
        print("Please provide either -n or -s.")
        parser.print_help()
        exit(1)
    
    if args.n is not None and args.s is not None:
        print("Please provide only one of -n or -s, not both.")
        parser.print_help()
        exit(1)
    
    elif args.n is not None:
        if args.n < 0:
            print("Please provide a non-negative integer for -n.")
        else:
            result = calculate_fibonacci(args.n)
            print(f"F({args.n}) = {result}")
    
    if args.s is not None:
        if args.s < 0:
            print("Please provide a non-negative integer for -s.")
        else:
            sequence = fibonacci_sequence(args.s)
            print(f"Fibonacci sequence up to {args.s} terms: {sequence}")

