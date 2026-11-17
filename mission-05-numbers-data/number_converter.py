# Number Converter - Mission 5
# A simple script written for The Digital Detective assignment
# Converts a positive decimal number into Binary and Hexadecimal

def main():
    print("=== Decimal to Binary & Hexadecimal Converter ===")
    
    user_input = input("Enter a positive decimal number: ")
    
    try:
        # Convert user input string into an integer
        decimal_val = int(user_input)
        
        if decimal_val < 0:
            print("Please enter a positive integer!")
            return
            
        # Built-in conversions
        binary_val = bin(decimal_val)
        hex_val = hex(decimal_val)
        
        print("\n--- Conversion Results ---")
        print(f"Decimal:     {decimal_val}")
        print(f"Binary:      {binary_val} (raw: {binary_val[2:]})")
        print(f"Hexadecimal: {hex_val} (uppercase: {hex_val[2:].upper()})")
        
    except ValueError:
        print("Invalid input! Please enter digits only.")

if __name__ == "__main__":
    main()
