import sys

def main():
    # Access command-line arguments
    args = sys.argv[1:]

    if len(args) < 2:
        print("Usage: python 1_Task1.py argument1 argument2")
        return

    argument1 = int(args[0])  # Convert to integer
    argument2 = int(args[1])  # Convert to integer

    result = perform_operation(argument1, argument2)

    print("Result: {}".format(result))

def perform_operation(argument1, argument2):
    result = argument1 + argument2
    return result

if __name__ == "__main__":
    main()
