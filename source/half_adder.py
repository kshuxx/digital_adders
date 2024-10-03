def half_adder(A, B):
    Sum = A ^ B  # XOR operation for Sum
    Carry = A & B  # AND operation for Carry
    return Sum, Carry

def get_binary_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value in (0, 1):
                return value
            else:
                print("Error: Input must be 0 or 1. Please try again.")
        except ValueError:
            print("Error: Invalid input. Please enter a binary digit (0 or 1).")

def main():
    print("Half Adder Program")
    A = get_binary_input("Enter the first binary digit (0 or 1): ")
    B = get_binary_input("Enter the second binary digit (0 or 1): ")
    
    Sum, Carry = half_adder(A, B)
    print(f"Sum: {Sum}, Carry: {Carry}")

if __name__ == "__main__":
    main()
