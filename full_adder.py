def full_adder(A, B, Cin):
    Sum = A ^ B ^ Cin  # XOR operation for Sum
    Cout = (A & B) | (B & Cin) | (A & Cin)  # Majority function for Carry-out
    return Sum, Cout

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
    print("Full Adder Program")
    A = get_binary_input("Enter the first binary digit (0 or 1): ")
    B = get_binary_input("Enter the second binary digit (0 or 1): ")
    Cin = get_binary_input("Enter the carry-in binary digit (0 or 1): ")
    
    Sum, Cout = full_adder(A, B, Cin)
    print(f"Sum: {Sum}, Carry-out: {Cout}")

if __name__ == "__main__":
    main()
